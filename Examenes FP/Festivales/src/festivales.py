from datetime import *
from typing import *
from collections import *
from parsea import *
import csv
  
Artista = NamedTuple("Artista",      
                        [("nombre", str),  
                        ("hora_comienzo", time),  
                        ("cache", int)]) 
 
Festival = NamedTuple("Festival",  
                        [("nombre", str), 
                        ("fecha_comienzo", date), 
                        ("fecha_fin", date), 
                        ("estado", str),                       
                        ("precio", float), 
                        ("entradas_vendidas", int), 
                        ("artistas", List[Artista]), 
                        ("top", bool) 
                    ])

def lee_festivales (archivo:str)->List[Festival]:
    festivales = []
    with open (archivo, encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for nombre,fecha_comienzo,fecha_fin,estado,precio,entradas_vendidas,artistas,top in lector:
            nombre =str(nombre)
            fecha_comienzo = ParseaFecha(fecha_comienzo)
            fecha_fin = ParseaFecha(fecha_fin)
            estado = str(estado.upper())
            precio = float(precio)
            entradas_vendidas = int(entradas_vendidas)
            artistas = ParseaArtista(artistas)
            top = ParseaTop(top)
            tupla = Festival(nombre,fecha_comienzo,fecha_fin,estado,precio,entradas_vendidas,artistas,top)
            festivales.append(tupla)
            
    return festivales

#4.2
def total_facturado(festivales:List[Festival], fecha_ini:Optional[date]=None, fecha_fin:Optional[date]=None)->float:
    '''
    Esta función devuelve el importe total facturado de los festivales que se han
    celebrado entre dos fechas dadas. La función recibe una lista de tuplas de tipo Festival y dos fechas,
    cuyos valores por defecto son None. La función devuelve un número real con el total facturado por los
    festivales celebrados entre las dos fechas dadas. Si la fecha inicial es None se hace el cálculo sin limitar
    la fecha mínima de los festivales. Si la fecha final es None se hace el cálculo sin limitar la fecha máxima
    de los festivales. Para calcular el total facturado por festival hay que multiplicar el número de entradas
    por el precio de la entrada del festival. Nota: tenga en cuenta que la función debe tomar la facturación
    de los festivales con estado celebrado en el rango de fechas, es decir, solo se tendrán en cuenta
    aquellos festivales que empiezan y acaban dentro del rango de fechas. (1.25 punto)

    '''
    res = 0.0
    for x in festivales:
        if (fecha_ini is None or fecha_ini <= x.fecha_comienzo) and (fecha_fin is None or fecha_fin >= x.fecha_comienzo) and x.estado == 'CELEBRADO':
            res += x.entradas_vendidas*x.precio
            
    return res

#4.3
def artista_top(festivales: List[Festival]) -> Tuple[int, str]:
    '''
    Recibe una lista de tuplas de tipo Festival y devuelve una tupla compuesta por un
    número entero y una cadena de texto, que representan el número de festivales y el nombre del artista
    que haya participado en más festivales que finalmente se han celebrado, respectivamente. (1.75
    puntos)
    '''
    res = defaultdict(int)
    for x in festivales:
        if x.estado == "CELEBRADO":
            for i in x.artistas:
                res[i.nombre] += 1
        
    res2 = max(res.items(), key=lambda x:x[1])
    
    return res2

#4.4
def mes_mayor_beneficio_medio(festivales: List[Festival]) -> str:
    '''
    Recibe una lista de tuplas de tipo Festival y devuelve una cadena de
    texto que será el nombre del mes, en español, de aquel que haya obtenido un mayor beneficio medio.
    Es decir, cada festival tiene un beneficio que se calcula a partir de las entradas vendidas menos el caché
    de los artistas. Pues esta función debe calcular el beneficio medio que se ha obtenido cada mes y
    devolver aquel cuyo beneficio haya sido el mayor. Nota: Si hubiera algún festival que se celebra entre
    dos meses, se imputará al mes en el que comienza. Por ejemplo, un festival que comience el 30 de junio
    y acabe el 4 de julio será imputado al mes de junio. (2.25 puntos)
    '''
    res = defaultdict(int)
    cache = defaultdict(int)
    n_fest = defaultdict(int)
    for x in festivales:
        n_fest[meses(x.fecha_comienzo.month)] += 1
        for i in x.artistas:
            cache[meses(x.fecha_comienzo.month)] += i.cache
        res[meses(x.fecha_comienzo.month)] += x.entradas_vendidas*x.precio
            
            
    for x in res:
        res[x] -= cache[x]
        res[x] /= n_fest[x]
    return max(res.items(), key=lambda x:x[1])[0]

def meses(mes):
    m = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    
    return m[mes - 1]

#4.5
def artistas_comunes(festivales: List[Festival], festi1: str, festi2:str) -> List[str]:
    '''
    Recibe una lista de tuplas de tipo Festival y dos cadenas de texto festi1 y
    festi2, y devuelve una lista con los nombres de aquellos artistas que se repitan entre festi1 y
    festi2. Nota: se considera que no hay festivales repeidos. (1.75 puntos)
    '''
    res = defaultdict(int)
    for x in festivales:
        if x.nombre == festi1 or x.nombre == festi2:
            for i in x.artistas:
                res[i.nombre] += 1
         
    res2 = []       
    for clave, valor in res.items():
        if valor > 1:
            res2.append(clave)
            
    return res2

#4.6 
def festivales_top_calidad_por_duracion(festivales: List[Festival], n: int=3) -> Dict[int, List[str]]:
    ''' Cada festival duración =[2, 8] días. Recibiendo lista tuplas de tipo Festival, y un número n, 
    devuelva diccionario: 
    - Claves = duraciones de los festivales; 
    - Valores = listas con los nombres de los  n festivales de más calidad (ordenados de más a menos calidad). 
    
    Calidad = ratio entre entradas vendidas 
    y número de artistas participantes. Cuanto más alto es este ratio, más calidad tiene el festival.'''
    res = defaultdict(lambda: defaultdict(int))
    for x in festivales:
        res[(x.fecha_fin - x.fecha_comienzo).days][x.nombre] = x.entradas_vendidas/len(x.artistas)
        
    res2 = defaultdict(list)
    for clave, dic2 in res.items():
        res_ord = sorted(dic2.items(), key=lambda x:x[1], reverse=True)[:n]
        for x in res_ord:
            res2[clave].append(x[0])
        
    return sorted(res2.items(), key=lambda x:x[0])

