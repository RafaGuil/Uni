from collections import *
from datetime import *
from typing import *
from parsea import *
import csv

Jugador = namedtuple('Jugador', 'ape_nom, licencia, fecha_ncto, federacion, handicap, fec_hor_act, senior, resultados')

#Ejercicio 1
def lee_jugadores(csv_filename: str):
    jugadores = []
    with open(csv_filename, encoding='utf8') as f:
        lector = csv.reader(f, delimiter=';')
        next(lector)
        for ape_nom, licencia, fecha_ncto, federacion, handicap, fec_hor_act, senior, resultados in lector:
            ape_nom = str(ape_nom)
            licencia = str(licencia)
            fecha_ncto = parsea_date(fecha_ncto)
            federacion = str(federacion)
            handicap = float(handicap)
            fec_hor_act = parsea_datetime(fec_hor_act)
            senior = parsea_bool(senior)
            resultados = parsea_lista(resultados)
            tupla = Jugador(ape_nom, licencia, fecha_ncto, federacion, handicap, fec_hor_act, senior, resultados)
            jugadores.append(tupla)
            
    return jugadores


#Ejercicio 2
def mejores_jugadores(jugadores: List[Jugador], año: int, n: int):
    res = []
    for x in jugadores:
        if año == x.fecha_ncto.year:
            res.append((x.licencia, x.ape_nom, x.handicap))
            
    return sorted(res, key=lambda x:x[-1])[:n], año, n


#Ejercicio 3
def jugadores_por_golpes(jugadores: List[Jugador]):
    res = defaultdict(set)
    for x in jugadores:
        for i in x.resultados:
            res[i].add(x.licencia)
        
    return sorted(res.items(), key=lambda x:x[0], reverse=True)


#Ejercicio 4
def promedio_ultimos_resultados(jugadores: List[Jugador], f1: Optional[date] = None, f2: Optional[date] = None):
    res = []
    for x in jugadores:
        if x.senior:
            if (f1 is None or x.fec_hor_act >= f1) and (f2 is None or x.fec_hor_act <= f2):
                res.append((x.licencia, sum(x.resultados)/len(x.resultados)))
                
    return res, f1, f2


#Ejercicio 5
def jugador_menor_handicap_por_federacion(jugadores: List[Jugador]):
    '''
     recibe  una  lista  de  tuplas  de  tipo  Jugador,  y  devuelve  un  diccionario  que  a  
     cada federación  le  haga  corresponder  una  tupla  con  el  nombre  y  apellidos  y  el 
     hándicap  del  mejor  jugador  de  dicha  federación. 
    '''
    res = {}
    for x in jugadores:
        if x.federacion not in res or x.handicap <= res[x.federacion][1]:
            res[x.federacion] = (x.ape_nom, x.handicap)
    return res


#Ejercicio 6
def comparativa_de_mejores_resultados_segun_handicap(jugadores: List[Jugador]):
    '''
    recibe una lista de tuplas de tipo Jugador y devuelve una lista de tuplas (hándicaps, diferencia), donde hándicaps es una cadena que representa 
    los dos hándicaps que se comparan y diferencia es un real,  que  se  calcula  como  la  diferencia  de  los  promedios  de  los  mejores 
    resultados  de  todos  los  jugadores  que  tienen  esos hándicaps. Para resolver este ejercicio descomponga el problema en dos problemas, 
    definiendo una función auxiliar para cada uno de ellos: 
        a) Defina una función auxiliar que construya un diccionario donde las claves sean los hándicaps y los valores del diccionario, el 
        promedio  de  los  mejores  resultados  de  cada  uno  de  los  jugadores  que  tienen  ese  hándicap.  Por  ejemplo,  si  solo  hay  dos 
        jugadores con hándicap 28.9
    
        b) Defina otra función auxiliar que a partir del diccionario anterior devuelva una lista con las diferencias entre cada valor promedio 
        y el anterior. Por ejemplo, si para el hándicap 29.0 el valor promedio es 75, en la lista de diferencias habría un valor (“28.9 vs 
        29.0”, -4)
    '''
    res = []