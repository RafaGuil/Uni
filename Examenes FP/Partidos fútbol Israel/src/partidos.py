from collections import *
from datetime import *
from parsea import *
import csv

Partido = namedtuple('Partido', 'fecha, equipoloc, equipovis, ganador, golesloc, golesvis, competicion, espectadores')

def lee_resultados(csv_file):
    partidos = []
    with open (csv_file, encoding='utf-8') as f:
        lector = csv.reader(f, delimiter=';')
        next(lector)
        for Date, Match, Result, Score, Competition, Spectators in lector:
            fecha = datetime.strptime(Date, '%d/%m/%Y')
            equipoloc, equipovis = parsea_partidos(Match)
            ganador = str(Result)
            golesloc, golesvis = parsea_goles(Score)
            competicion = str(Competition)
            espectadores = int(Spectators)
            tupla = Partido(fecha, equipoloc, equipovis, ganador, golesloc, golesvis, competicion, espectadores)
            partidos.append(tupla)
    return partidos

def selecciones_enfrentadas_israel(partidos: list[Partido], n=3):
    '''
    los  nombres  de  las  selecciones  que  se  han  enfrentado  a  Israel  al  menos  una  vez  en  las  n 
    competiciones en las que Israel ha jugado más encuentros.
    '''
    n_partidos_competi_israel = defaultdict(int)
    
    for x in partidos:
        n_partidos_competi_israel[x.competicion]+=1
        
    top_comps = sorted(n_partidos_competi_israel.items(), key=lambda x: x[1], reverse=True)[:n]
    top_comp_names = {comp for comp, _ in top_comps}
    
    equipos_efrentados = set()
    for x in partidos:
        if x.competicion in top_comp_names:
            if x.equipoloc != 'Israel':
                equipos_efrentados.add(x.equipoloc)
            else:
                equipos_efrentados.add(x.equipovis)

    return equipos_efrentados

def lista_diferencias_goles(partidos: list[Partido], fecha_ini: date, fecha_fin: date):
    '''
    una lista con la diferencia de goles a favor de Israel de cada partido con respecto al anterior 
    (en orden cronológico) en el rango de fechas dado. Por ejemplo, si en los cuatro primeros partidos 
    Israel marcó 1 gol, 2 goles, 3 goles y 0 goles, respectivamente, entonces los primeros valores de 
    la lista devuelta serán 1 (2 menos 1), 1 (3 menos 2) y -3 (0 menos 3).

    '''
    res = []
    partidos_ord = sorted(partidos, key=lambda x:x.fecha)
    prev_goles_Israel = 0
    for x in partidos_ord:
        if (fecha_ini is None or fecha_ini <= x.fecha) and (fecha_fin is None or fecha_fin >= x.fecha):
            if x.equipoloc == 'Israel':
                res.append(x.golesloc - prev_goles_Israel)
                prev_goles_Israel = x.golesloc
            elif x.equipovis == 'Israel':
                res.append(x.golesvis - prev_goles_Israel)
                prev_goles_Israel = x.golesvis
                
    return res

def partidos_por_mes(partidos: list[Partido]):
    '''
    recibe  una  lista  de  tuplas  de  tipo  Partido,  y  devuelve  una  lista  de  tuplas  de  tipo  (mes, 
    frecuencia)  donde  para  cada  mes  en  el  que  se  haya  jugado  al  menos  un  partido,  habrá  una  tupla
    con  el  número del mes y el número de partidos jugados en ese mes. La lista debe estar ordenada por mes.
    '''
    res = defaultdict(int)
    for x in partidos:
        res[x.fecha.month] += 1
        
    return sorted(res.items(), key=lambda x:x[0])

def partidos_mensuales_por_anyo(partidos: list[Partido]):
    '''
    usando la función del apartado anterior, implemente una función que recibe una 
    lista de tuplas de tipo Partido, y devuelve un diccionario tal que a cada año  como clave le hace corresponder una 
    lista ordenada por mes  de tuplas de tipo (mes, frecuencia) con el número de partidos por mes jugados por Israel 
    en el año dado por la clave.
    '''
    res = defaultdict(list)
    for x in partidos:
        res[x.fecha.year].append(x)
        
    for clave, valor in res.items():
        res[clave] = partidos_por_mes(valor)
        
    return sorted(res.items(), key=lambda x:x[0])

