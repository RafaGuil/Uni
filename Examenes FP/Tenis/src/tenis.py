from collections import *
from datetime import *
from parsea import *
from typing import *
import csv

PartidoTenis = namedtuple('PartidoTenis', 'fecha,jugador1,jugador2,superficie,resultado,errores_nf1,errores_nf2')

Set = namedtuple('Set', 'juegos_j1, juegos_j2')


#EJERCICIO 1
def lee_partidos_tenis(csv_filename: str):
    partidos = []
    with open(csv_filename, encoding='utf-8') as f:
        lector = csv.reader(f, delimiter=';')
        for fecha,jugador1,jugador2,superficie,primer_set,segundo_set,tercer_set,errores_nf1,errores_nf2 in lector:
            fecha = parsea_date(fecha)
            jugador1 = str(jugador1)
            jugador2 = str(jugador2)
            superficie = str(superficie)
            set1 = parsea_set(primer_set)
            set2 = parsea_set(segundo_set)
            set3 = parsea_set(tercer_set)
            resultado = [set1, set2, set3]
            errores_nf1 = int(errores_nf1)
            errores_nf2 = int(errores_nf2)
            tupla = PartidoTenis(fecha,jugador1,jugador2,superficie,resultado,errores_nf1,errores_nf2)
            partidos.append(tupla)
            
    return partidos


#EJERCICIO 2
def tenista_mas_victorias(partidos: List[PartidoTenis], f1: Optional[date] = None, f2: Optional[date] = None):
    '''
    Recibe una lista de tuplas de tipo PartidoTenis, y dos fechas, ambas de tipo date, y 
    con valor por defecto None.  Devuelve el nombre  del tenista que ha tenido más victorias en los partidos 
    jugados entre las fechas (ambas inclusive). Si la primera fecha es None, la función  devuelve el tenista con 
    más victorias hasta esa fecha (inclusive). Si la segunda fecha es  None,  la función devuelve el tenista con 
    más victorias  desde  esa  fecha  (inclusive).  Finalmente,  si  las  dos  fechas  son  None,  la  función  devuelve  el 
    tenista con más victorias de toda la lista, independientemente de la fecha. 
    '''
    res = defaultdict(int)
    for x in partidos:
        if (f1 is None or x.fecha >= f1) and (f2 is None or x.fecha <= f2):
            if x.jugador1 == ganador(x):
                res[x.jugador1] += 1
            elif x.jugador2 == ganador(x):
                res[x.jugador2] += 1
            
    return max(res.items(), key=lambda x:x[1])

def ganador(partido: PartidoTenis):
    '''
    Recibe  una  tupla de  tipo PartidoTenis y  devuelve  el  nombre  del  jugador  que  ganó 
    ese partido.
    '''
    local = 0
    visitante = 0
    ganador = None
    for x in range(0, 3):
        if partido.resultado[x].juegos_j1 > partido.resultado[x].juegos_j2:
            local += 1
        elif partido.resultado[x].juegos_j1 < partido.resultado[x].juegos_j2:
            visitante += 1
        else:
            local += 0
            visitante += 0
            
    if local > visitante:
        ganador = partido.jugador1
    else:
        ganador = partido.jugador2
        
    return ganador


#EJERCICIO 3
def n_tenistas_con_mas_errores(partidos: List[PartidoTenis], n: Optional[int] = None):
    '''
    Recibe una lista de tuplas de tipo PartidoTenis y un número n, con valor por 
    defecto None, y devuelve una lista con los nombres de los n tenistas que han acumulado más errores no 
    forzados en el total de partidos que han jugado. Si n es None, entonces devuelve todos los tenistas de la 
    lista de tuplas ordenados de mayor a menor número de errores no forzados.
    '''
    res = defaultdict(int)
    for x in partidos:
        res[x.jugador1] += x.errores_nf1
        res[x.jugador2] += x.errores_nf2
        
    return sorted(res.items(), key=lambda x:x[1], reverse=True)[:n]


#EJERCICIO 4
def num_tenistas_distintos_por_superficie(partidos: List[PartidoTenis]):
    '''
    Recibe  una  lista  de  tuplas  de  tipo  PartidoTenis,  y  devuelve  un 
    diccionario tal que a cada superficie (clave) le hace corresponder el número de jugadores distintos que han 
    jugado partidos en ese tipo de superficie.
    '''
    res = defaultdict(set)
    for x in partidos:
        res[x.superficie].add(x.jugador1)
        res[x.superficie].add(x.jugador2)
        
    res2 = defaultdict(int)
    for clave, valor in res.items():
        res2[clave] = len(valor)
        
    return res2


#EJERCICIO 5
def partido_mas_errores_por_mes(partidos: List[PartidoTenis], tipo_superficie: Optional[List[str]] = None):
    '''
    Recibe una lista de tuplas de tipo PartidoTenis, y una lista de cadenas con 
    tipos de superficie, que toma como valor por defecto None, y devuelve un diccionario que asocia a cada 
    mes, una tupla (fecha del partido, jugador1, jugador2) que representa al partido de ese mes jugado en una 
    de  las  superficies  de  la  lista  dada  como  parámetro  en  el  que  se  han  cometido más  errores  no  forzados, 
    teniendo en cuenta los errores de ambos jugadores. Si la lista de superficies dada como parámetro tiene 
    como  valor  None,  entonces  se  tendrán  en  cuenta  todas  las  superficies  para  generar  el  diccionario 
    resultante.
    '''
    res = {}
    for x in partidos:
        if tipo_superficie is None or x.superficie in tipo_superficie:
            errores_acum = x.errores_nf1 + x.errores_nf2
            if x.fecha.month not in res or errores_acum > res[x.fecha.month][3]:
                res[x.fecha.month] = (x.fecha, x.jugador1, x.jugador2, errores_acum)
    res2 = {}
    for clave, valor in res.items():
        res2[clave] = valor[:3]
    return res2