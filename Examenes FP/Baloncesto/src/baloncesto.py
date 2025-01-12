from collections import *
from datetime import *
from typing import *
import csv

PartidoBasket = namedtuple('PartidoBasket','fecha, equipo1, equipo2, competicion, puntos_eq1, puntos_eq2, faltas_eq1, faltas_eq2')

def lee_partidos(csv_filename: str):
    partidos = []
    with open(csv_filename, encoding='utf-8') as f:
        lector = csv.reader(f, delimiter=';')
        next(lector)
        for fecha,equipo_1,equipo_2,torneo,cuartos,faltas_1,faltas_2 in lector:
            fecha = datetime.strptime(fecha, "%d/%m/%Y").date()
            equipo_1 = str(equipo_1)
            equipo_2 = str(equipo_2)
            competicion = str(torneo)
            puntos_eq1 = parsea_y_suma_resultados(cuartos)[0]
            puntos_eq2 = parsea_y_suma_resultados(cuartos)[1]
            faltas_eq1 = int(faltas_1)
            faltas_eq2 = int(faltas_2)
            tupla = PartidoBasket(fecha,equipo_1,equipo_2,competicion,puntos_eq1,puntos_eq2,faltas_eq1,faltas_eq2)
            partidos.append(tupla)
            
    return partidos

def parsea_y_suma_resultados(cuartos: str):
    '''
    Recibe una cadena de texto con los resultados de los cuatro cuartos de 
    un partido, y devuelve una tupla con dos enteros, correspondientes a los puntos totales anotados por 
    el primer y el segundo equipo. Por ejemplo, si recibe la cadena '18-20*15-18*24-17*20-17', debe 
    devolver (77, 72). (0,5 puntos)
    '''
    local = 0
    visitante = 0
    
    parse1 = cuartos.split('*')
    for x in range(4):
        parse2 = parse1[x].split('-')
        local += int(parse2[0])
        visitante += int(parse2[1])


    return (local, visitante)

def equipo_con_mas_faltas(partidos: List[PartidoBasket], equipos: Optional[Set[str]] = None):
    '''
    Recibe una lista de tuplas PartidoBasket, y un conjunto de cadenas de texto 
    equipos,  con  valor  por  defecto  None,  y  devuelve  el  nombre  del  equipo  que  acumula  más  faltas 
    personales, de entre los equipos incluidos en el parámetro equipos. Si el parámetro equipos es None, 
    se  devolverá  el  equipo  con  más  faltas  personales  de  entre  todos  los  que  aparezcan  en  la  lista  de 
    partidos recibida. (1,5 puntos) 
    '''
    res = defaultdict(int)
    for x in partidos:
        if (equipos is None or x.equipo1 in equipos):
            res[x.equipo1] += x.faltas_eq1
        if (equipos is None or x.equipo2 in equipos):
            res[x.equipo2] += x.faltas_eq2
            
    return max(res.items(), key=lambda x:x[1])

def media_puntos_por_equipo(partidos: List[PartidoBasket], competicion: str):
    '''
    Recibe una lista de  tuplas PartidoBasket y una cadena de texto 
    competicion, y devuelve un diccionario en el que se relaciona cada equipo con la media de puntos 
    anotados por el equipo en todos los partidos disputados de la competición indicada por el parámetro 
    competicion. (1,5 puntos) 
    '''
    res = defaultdict(float)
    count_partidos = defaultdict(int)
    for x in partidos:
        if x.competicion == competicion:
            res[x.equipo1] += x.puntos_eq1
            res[x.equipo2] += x.puntos_eq2
            count_partidos[x.equipo1] += 1
            count_partidos[x.equipo2] += 1

            
    for x, i in zip(res, count_partidos):
        res[x] /= count_partidos[i]
        
    return res

def diferencia_puntos_anotados(partidos: List[PartidoBasket], equipo: str):
    '''
    Recibe  una  lista  de  tuplas  PartidoBasket  y  una  cadena  de  texto 
    equipo, y devuelve una lista de enteros con la diferencia de puntos anotados entre cada dos partidos 
    consecutivos  del  equipo  indicado  por  el  parámetro  equipo.  Por  ejemplo,  si  el  equipo  indicado  ha 
    jugado  tres  partidos  consecutivos  en  el  tiempo,  anotando  60,  64  y  58  respectivamente,  la  lista 
    devuelta debería ser [4, -6]. Tenga en cuenta que los partidos no tienen por qué venir ordenados 
    cronológicamente en la lista de tuplas recibida. (1,5 puntos)
    '''
    partidos_ord = sorted(partidos, key=lambda x:x.fecha)
    puntos_acumulados = []
    for x in partidos_ord:
        if x.equipo1 == equipo:
            puntos_acumulados.append(x.puntos_eq1)
        elif x.equipo2 == equipo:
            puntos_acumulados.append(x.puntos_eq2)
            
    res = []
    for x in range(len(puntos_acumulados)-1):
        diff = puntos_acumulados[x+1] - puntos_acumulados[x]
        res.append(diff)
        
    return res

def victorias_por_equipo(partidos: List[PartidoBasket]):
    '''
    Recibe una lista de tuplas PartidoBasket y devuelve un diccionario que hace 
    corresponder cada equipo con el número de victorias del mismo.
    '''
    res = defaultdict(int)
    for x in partidos:
        if x.puntos_eq1 > x.puntos_eq2:
            res[x.equipo1] += 1
        elif x.puntos_eq2 > x.puntos_eq1:
            res[x.equipo2] += 1
            
    return res

def equipos_minimo_victorias(partidos: List[PartidoBasket], n: int):
    '''
    Recibe una lista de tuplas PartidoBasket y un entero n, y devuelve una 
    lista  con  los  equipos  con  n  o  más  victorias.  La  lista  estará  ordenada  de  mayor  a  menor  número  de 
    victorias. (1 puntos) 
    '''
    res = []
    for clave, valor in victorias_por_equipo(partidos).items():
        if valor >= n:
            res.append(clave)
            
    return res

def equipos_mas_victorias_por_año(partidos: List[PartidoBasket], n: int):
    '''
    Recibe una lista de tuplas PartidoBasket y un entero n, y devuelve 
    un diccionario en el que las claves son los años en los que se han disputado los partidos, y los valores 
    son listas con los equipos con n o más victorias acumuladas en los partidos disputados cada año. Las 
    listas estarán ordenadas de mayor a menor número de victorias. (1 punto)
    '''
    partidos_por_año = defaultdict(list)
    for p in partidos:
        partidos_por_año[p.fecha.year].append(p)
        
    res = {}
    for año, partidos_año in partidos_por_año.items():
        res[año] = equipos_minimo_victorias(partidos_año, n)
    return res