from collections import *
from datetime import *
from typing import *
from parsea import *
import csv

Consumo = namedtuple('Consumo','fecha, id, tipo_edificio, edificio, barrio, clase, grupo, unidad, consumo')

def lee_consumos(csv_filename: str):
    consumos = []
    with open(csv_filename, encoding='utf-8') as f:
        lector = csv.reader(f, delimiter=';')
        next(lector)
        for anyo, mes, id_, tipo_edificio, edificio, barrio, clase, grupo, unidad, consumo in lector:
            fecha = parsea_fecha(f'1/{mes}/{anyo}')
            consumo = parsea_consumo(consumo)
            tupla = Consumo(fecha, id_, tipo_edificio, edificio, barrio, clase, grupo, unidad, consumo)
            consumos.append(tupla)
            
    return consumos

def barrios_top_consumo(consumos: List[Consumo], anyo: float, clase: str, n: int = 3):
    '''
    Recibe  una  lista  de  tuplas  de  tipo  Consumo,  un  año,  una  clase  de  energía  y  un 
    número  entero  n  (con  valor  por  defecto  3),  y  devuelve  una  lista  de  tuplas  de  tipo  (str,  float),  con  los  n 
    barrios que han tenido más consumo medio mensual de la clase de energía dada como parámetro en el 
    año  dado  como  parámetro.  La  lista  resultante  estará  ordenada  de  mayor  a  menor  media  mensual. 
    Considere  que  hay  consumo  los  12  meses  del  año  y  que  no  se  debe  distinguir  entre  mayúsculas  y 
    minúsculas en  el  valor del parámetro clase.  Nota: no debe tener en cuenta los registros con  un valor de 
    consumo igual a None. (2,5 puntos) 
    Por  ejemplo,  si  se  invoca  a  la  función con  la clase ‘ENERGIA ACTIVA’ en  el  año  2020  y  con  n  =  3,  la  lista 
    resultante sería: 
    [('JERÓNIMOS', 314066.2083333333), ('UNIVERSIDAD', 187650.0166666667), 
    ('JUSTICIA', 93032.08333333333)]
    '''
    res = defaultdict(float)
    for x in consumos:
        if x.clase.lower() == clase.lower() and x.fecha.year == anyo:
            if x.consumo != None:
                res[x.barrio] += x.consumo
            
    for x in res:
        res[x] /= 12
        
    return sorted(res.items(), key=lambda x:x[1], reverse=True)[:n]

def media_consumo_edificios(consumos: List[Consumo], clase: str):
    '''
    Recibe una lista de tuplas de tipo Consumo y una clase de energía, y devuelve 
    un  valor  float  que  representa  el  promedio  del  consumo  de  energía  de  la  clase  pasada  como  parámetro 
    entre el número de edificios. Si no se puede calcular la media, la función devuelve 0. Notas: tenga en cuenta 
    que para el cálculo de la media debe reflejar el número de edificios distintos (recuerde que los edificios se 
    identifican por el campo “id”),  que  no  se  debe  distinguir  entre  mayúsculas  y  minúsculas  en  el  valor  del 
    parámetro clase, y que  no debe tener en cuenta los registros con  un valor de  consumo igual a None.  (2 
    puntos) 
    Por ejemplo, si se invoca a la función con la clase ‘ENERGIA REACTIVA’, el resultado sería: 
    78434.95439560444
    '''
    consumo_energia = 0.0
    n_edificios = set()
    for x in consumos:
        if x.clase.lower() == clase.lower() and x.consumo != None:
            consumo_energia += x.consumo
            n_edificios.add(x.id)
            
    res = 0.0
    if len(n_edificios) == 0:
        res = 0
    else:
        res = consumo_energia / len(n_edificios)
        
    return res

def media_consumos_de_edificio_por_tipo_edificio(consumos: List[Consumo], anyo: float, clase: str):
    '''
    Recibe una lista de tuplas de tipo Consumo, un año y una 
    clase  de  energía,  y  devuelve  un  diccionario  de  tipo  {str:  float}  que  a  cada  tipo  de  edificio  le  hace 
    corresponder la media de consumo de la clase de energía y año dados como parámetros. Tenga en cuenta 
    que no se debe distinguir entre mayúsculas y minúsculas en el valor del parámetro clase, y que debe usar 
    la función del apartado anterior para resolver el ejercicio. (2 puntos)  
    Por  ejemplo,  si se invoca a la función con la clase de energía ‘ENERGIA REACTIVA’ y el año 2020, el 
    diccionario resultante sería:  
    {'Centros culturales y bibliotecas': 64857.969999999994,  
    'Centros mixtos': 96293.41666666667,  
    'Centros deportivos':41952.294117647056,  
    'Centros escolares': 678.5750000000003, 
    'Centros administrativos': 84680.0}
    '''
    res = defaultdict(list)
    for x in consumos:
        if x.fecha.year == anyo:
            res[x.tipo_edificio].append(x)
            
    res2 = defaultdict(float)
    for clave, valor in res.items():
        res2[clave] = media_consumo_edificios(valor, clase)
            
    return res2

def incremento_anual_de_consumo_por_unidad(consumos: List[Consumo], unidad: str = 'kWh'):
    '''
    Recibe una lista de tuplas de tipo Consumo y una unidad de 
    medición (con valor por defecto ‘ kWh’), y devuelve una lista de tuplas de tipo (str, float), donde la cadena 
    representa el intervalo de años, y el valor real representa el incremento (o decremento) anual del consumo 
    total de la energía medida en las unidades dadas como parámetro. Nota: el incremento entre dos años se 
    calcula como el porcentaje de la diferencia de sus consumos dividido por el del año menor. También debe 
    tener en cuenta que no debe considerar los registros con un valor de consumo igual a None. (2,5 puntos)  
    Por ejemplo, si la unidad toma el valor ‘kVAr’, el resultado sería: 
    [('2021-2020', 414.79426524724227)]
    '''
    res = defaultdict(float)
    for x in consumos:
        if x.unidad == unidad and x.consumo != None:
            res[x.fecha.year] += x.consumo
            
    res2 = defaultdict(float)
    prev_valor = None
    for clave, valor in res.items():
        if prev_valor != None:
            incremento = 100*(valor - prev_valor)/prev_valor
            res2[clave] = incremento
        prev_valor = valor
        
    res3 = []
    for clave, valor in res2.items():
        res3.append((f'{clave}-{clave-1}', valor))
            
    return res3