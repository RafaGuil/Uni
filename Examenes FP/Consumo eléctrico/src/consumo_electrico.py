from collections import *
from datetime import *
from typing import * 
from parsea import *
import csv
 
IntervaloFechas = NamedTuple("IntervaloFechas",  
                     [("inicio", date), ("fin", date)]) 
 
Factura = NamedTuple("Factura",  
                     [("id_vivienda", str), 
                      ("tipo_vivienda", str), 
                      ("barrio", str), 
                      ("tipo_tarifa", str), 
                      ("periodo_facturado", IntervaloFechas), 
                      ("coste_potencia", float), 
                      ("consumo_punta", float), 
                      ("consumo_valle", float), 
                      ("precio_punta", float), 
                      ("precio_valle", float), 
                      ("importe_total", float)])

def lee_facturas(ruta_fichero: str) -> List[Factura]:
    facturas = []
    with open(ruta_fichero, encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for ID_Vivienda,Tipo_Vivienda,Barrio,Tipo_Tarifa,Periodo_Inicio,Periodo_Fin,Coste_Potencia_EUR,Consumo_Punta_kWh,Consumo_Valle_kWh,Precio_kWh,Importe_Total_EUR in lector:
            id_vivienda = str(ID_Vivienda)
            tipo_vivienda = str(Tipo_Vivienda)
            barrio = str(Barrio)
            tipo_tarifa = str(Tipo_Tarifa)
            periodo_facturado = IntervaloFechas(parsea_fecha(Periodo_Inicio), parsea_fecha(Periodo_Fin))
            coste_potencia = float(Coste_Potencia_EUR)
            consumo_punta = float(Consumo_Punta_kWh)
            consumo_valle = float(Consumo_Valle_kWh)
            precio_punta = parsea_precio(Precio_kWh)[0]
            precio_valle = parsea_precio(Precio_kWh)[1]
            importe_total = float(Importe_Total_EUR)
            tupla = Factura(id_vivienda,tipo_vivienda,barrio,tipo_tarifa,periodo_facturado,coste_potencia,consumo_punta,consumo_valle,precio_punta,precio_valle,importe_total)
            facturas.append(tupla)
            
    return sorted(facturas, key=lambda x:x.periodo_facturado.inicio)

def extrae_precio_por_mes(facturas: List[Factura], tipo_tarifa: str) -> Dict[str, Tuple[float, float]]:
    '''
    Recibe una lista de facturas y un tipo de tarifa, y devuelve un diccionario en el
    que las claves son cadenas "año-mes" (por ejemplo, "2023-01") y los valores son tuplas con el precio
    por kWh en horario punta y valle para dicho tipo de tarifa de cada mes. Tenga en cuenta que el precio
    del kWh es igual para todos los clientes del mismo tipo de contrato para cada mes. (1 punto)
    Nota: Para obtener la cadena "año-mes" puede utilizar el método strftime del tipo date, pasándole
    la cadena de formato "%Y-%m".
    '''
    res = {}
    for x in facturas:
        if x.tipo_tarifa == tipo_tarifa:
            res[datetime.strftime(x.periodo_facturado.inicio, "%Y-%m")] = (x.precio_punta, x.precio_valle)
            
    return res

def busca_vivienda_mayor_consumo_acumulado(facturas: List[Factura]) -> Tuple[str, float]:
    '''
    Recibe una lista de facturas y devuelve una tupla con el
    identificador de la vivienda con mayor consumo acumulado, y el valor de dicho consumo acumulado. El
    consumo acumulado de una vivienda es la suma de los consumos tanto de horario punta como de
    horario valle de todas las facturas de esa vivienda contenidas en la lista recibida. (1 punto)
    '''
    res = defaultdict(float)
    for x in facturas:
        res[x.id_vivienda] += x.consumo_punta
        res[x.id_vivienda] += x.consumo_valle
        
    return max(res.items(), key=lambda x:x[1])

def barrios_mayor_consumo_valle_medio(facturas: List[Factura], top_n: int) -> List[str]:
    '''
    Recibe una lista de facturas y un entero top_n, y devuelve una
    lista con los top_n barrios con mayor consumo medio en horario valle. (1,5 puntos)
    '''
    res = defaultdict(float)
    count = defaultdict(int)
    for x in facturas:
        res[x.barrio] += x.consumo_valle
        count[x.barrio] += 1
        
    for x in res:
        res[x] /= count[x]
        
    res_ord = sorted(res.items(), key=lambda x:x[1], reverse=True)[:top_n]
    
    res2 = []
    for clave, _ in res_ord:
        res2.append(clave)
        
    return res2

def compara_importe_tipos_factura(facturas: List[Factura], id_vivienda: str) -> Optional[Tuple[str, float, float]]:
    '''
    Compara_importe_tipos_factura: recibe una lista de facturas y un identificador de vivienda, y permite
    comparar el importe total pagado por esa vivienda con el que se hubiera pagado con el otro tipo de
    tarifa. Devuelve una tupla con el cambio de tipo de contrato contemplado ("tramos->única" o
    "única->tramos"), el importe total actual y el importe total que se habría facturado con el cambio de
    tarifa. Si no se encontrara la vivienda indicada en la lista de facturas, la función devuelve None.
    Recuerde cómo se calcula el importe total de una factura:
    En la tarifa única, se multiplica el consumo en kWh por el precio por kWh, y se le suma el coste
    de la potencia contratada.
    En la tarifa por tramos, se multiplican y suman el consumo en kWh de cada tramo (punta y valle)
    por el precio por kWh de cada tramo, y se le suma el coste de la potencia contratada.
    Tenga en cuenta que cada vivienda mantiene un mismo tipo de tarifa en todo el periodo para el que se
    están analizando los datos. (1,5 puntos)
    '''
    res = tuple()
    precio_actual = 0.0
    precio_contr = 0.0
    facturas_vivienda = [x for x in facturas if x.id_vivienda == id_vivienda]
    if not facturas_vivienda:
        return None
            
    tarifa_actual = facturas_vivienda[0].tipo_tarifa
    tarifa_contraria = 'tramos' if tarifa_actual == 'única' else 'única'
    
    precio_mes_t_contr = extrae_precio_por_mes(facturas, tarifa_contraria)
    
    for x in facturas_vivienda:
        mes = datetime.strftime(x.periodo_facturado.inicio, "%Y-%m")
        precio_punta, precio_valle = precio_mes_t_contr[mes]
        cambio = tarifa_actual+'->'+tarifa_contraria
        precio_actual += x.importe_total
        precio_contr += calc_precio(x.consumo_punta,x.consumo_valle,precio_punta,precio_valle,x.coste_potencia)
        res = (cambio, precio_actual, round(precio_contr, 2))
                    
    return res

def calc_precio(consumo_punta, consumo_valle, precio_punta, precio_valle, potencia):
    return (consumo_punta*precio_punta)+(consumo_valle*precio_valle)+potencia

def busca_cambios_beneficiosos(facturas: List[Factura]) -> List[Tuple[str, int, float]]:
    '''
    Recibe una lista de facturas y calcula para cuántas viviendas resulta
    beneficioso hacer un cambio de tarifa (es decir, hubieran pagado menos en total si hubieran tenido la
    otra tarifa). Devuelve una lista con el tipo de cambio de tarifa, el número de cambios beneficiosos de
    ese tipo encontrados y el total que habrían ahorrado por esos cambios. Por ejemplo, si la función
    devolviera [('tramos->única', 33, 190.3615), ('única->tramos', 23, 127.0188)],
    significaría que se han encontrado 33 viviendas que habrían ahorrado dinero si hubieran tenido la tarifa
    única en lugar de la tarifa por tramos (el ahorro total habría sido de 190,3615 euros), y que se han
    encontrado 23 viviendas que habrían ahorrado dinero si hubieran tenido la tarifa por tramos en lugar
    de la tarifa única (el ahorro total habría sido de 127,0188 euros). (2 puntos)
    '''
    res_tu = []
    res_ut = []
    prev_viv = None
    for x in sorted(facturas, key=lambda x:x.id_vivienda):
        if x.id_vivienda != prev_viv:
            resultado = compara_importe_tipos_factura(facturas, x.id_vivienda)
            if resultado is not None:
                cambio, precio_actual, precio_contr = resultado
                if precio_actual > precio_contr:
                    if x.tipo_tarifa == 'tramos':
                        res_tu.append(precio_actual - precio_contr)
                    else:
                        res_ut.append(precio_actual - precio_contr)
        prev_viv = x.id_vivienda
    
    res = [('tramos->única', len(res_tu), sum(res_tu)), ('única->tramos', len(res_ut), sum(res_ut))]
    return res

def calcula_mes_incremento_maximo_consumo_acumulado(facturas: List[Factura], tipo_vivienda: Optional[str] = None) -> Tuple[str, float]:
    '''
    Calcula_mes_incremento_maximo_consumo_acumulado: recibe una lista de facturas y devuelve el
    "año-mes"(por ejemplo, "2023-04") en el que se ha producido el mayor incremento en el consumo
    acumulado de todas las viviendas del tipo indicado con respecto al mes anterior, y el valor de dicho
    consumo acumulado. Si no se indica ningún tipo de vivienda (se deja el valor None) se contemplarán
    todos los tipos de vivienda. El consumo acumulado de las viviendas de un tipo es la suma de los
    consumos en horario punta y valle de todas las viviendas de ese tipo. (2 puntos)
    Nota: Para obtener la cadena "año-mes" puede utilizar el método strftime del tipo date, pasándole
    la cadena de formato "%Y-%m".
    '''
    res = defaultdict(float)
    for x in facturas:
        if (tipo_vivienda is None or x.tipo_vivienda == tipo_vivienda):
            res[x.periodo_facturado.inicio.strftime("%Y-%m")] += (x.consumo_punta + x.consumo_valle)
            
    res2 = defaultdict(float)
    meses = sorted(res.keys())
    for x in range(1, len(meses)):
        res2[meses[x]] = res[meses[x]] - res[meses[x-1]]
        
    return max(res2.items(), key=lambda x:x[1])

