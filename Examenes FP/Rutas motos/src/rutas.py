from collections import *
from datetime import *
from parsea import *
import csv

Ruta = namedtuple('Ruta', 'ciudad_inicio, coordenada, fecha_ruta, km, gasolineras, dificultad, zona_descanso, vel_max, vel_min')
Coordenada = namedtuple('Coordenada', 'latitud, longitud')

def lee_rutas(csv_file):
    rutas = []
    with open(csv_file, encoding='utf-8') as f:
        lector = csv.reader(f, delimiter=';')
        next(lector)
        for ciudad_inicio, latitud_longitud, fecha_ruta, km, gasolineras, dificultad, zona_descanso, vel_max, vel_min in lector:
            ciudad_inicio = str(ciudad_inicio).strip()
            coordenada = parsea_coordenada(latitud_longitud)
            fecha_ruta = parsea_fecha(fecha_ruta)
            km = float(km)
            gasolineras = int(gasolineras)
            dificultad = str(dificultad)
            zona_descanso = True if zona_descanso == 'True' else False
            vel_max = int(vel_max)
            vel_min = int(vel_min)
            tupla = Ruta(ciudad_inicio, coordenada, fecha_ruta, km, gasolineras, dificultad, zona_descanso, vel_max, vel_min)
            rutas.append(tupla)
            
    return rutas

def acumular_kms_por_meses(rutas: list[Ruta]):
    '''
    Recibe una lista de tuplas de tipo Ruta, y devuelve un diccionario que asocia a 
    cada año una lista con el total de kilómetros que se han recorrido en cada mes. Si en alguno de los meses 
    no se ha realizado ninguna ruta, debe aparecer el valor 0.0. Los valores en la lista deben estar ordenados 
    cronológicamente,  es  decir,  el  primer  valor  se  corresponde  con  enero,  el  segundo  con  febrero,  y  así 
    sucesivamente.
    '''
    res = {}
    for x in rutas:
        año = x.fecha_ruta.year
        mes = x.fecha_ruta.month
        if año not in res:
            res[año] = [0] * 12
        res[año][mes - 1] += x.km
    return res

def diferencias_kms_meses_anyo(rutas: list[Ruta]):
    '''
     recibe una lista de tuplas de tipo Ruta, y devuelve un diccionario que asocia 
    cada año con una lista con las diferencias en kilómetros recorridos de cada mes de ese año con respecto al 
    mes  anterior.  Las  diferencias  deben  estar  ordenadas  cronológicamente,  es  decir,  el  primer  valor  es  la 
    diferencia entre febrero y enero, el segundo la diferencia entre marzo y febrero, y así sucesivamente. Tiene 
    que usar de forma obligatoria la función del apartado anterior.
    '''
    res = acumular_kms_por_meses(rutas)
    dic = {}
    for clave, valor in res.items():
        dic[clave] = incremento_km(valor)
        
    return dic

def incremento_km(total_meses):
    res = []
    for x in range(len(total_meses)-1):
        res.append(total_meses[x+1] - total_meses[x])
        
    return res

def top_rutas_lejanas(rutas: list[Ruta], n: int, c: tuple[Coordenada], km_min: int):
    '''
     Dada una lista de tuplas de tipo Ruta, un valor entero n, un valor c de tipo Coordenada, 
    y  un  entero  km_min,  obtener  una  lista  con  las  n  rutas  cuya  ciudad  de  inicio  está  más  lejana  a  las 
    coordenadas que se pasan como parámetro de entrada y cuyo número de kilómetros sea mayor al valor 
    km_min.  La  variable  km_min  tomará  como  valor  por  defecto  None,  en  cuyo  caso  se  tendrán  en  cuenta 
    todas las rutas. Para calcular la distancia entre las distintas ciudades, deberá usar la distancia Manhattan. 
    Dadas dos coordenadas c1, y c2, la distancia Manhattan se calcula como d = |lat1-lat2| + |long1-long2|. 
    Donde  lat1  y  long1  son  la  latitud  y  longitud  de  c1,  y  lat2  y  long2  son  la  latitud  y  longitud  de  c2.  
    Use  el método abs para obtener el valor absoluto.
    '''
    res = []
    lat1 = c[0]
    long1 = c[1]
    for x in rutas:
        lat2 = x.coordenada.latitud
        long2 = x.coordenada.longitud
        d = abs(lat1-lat2) + abs(long1-long2)
        if km_min is None or d > km_min:
            res.append((x, d))
            
    res_ord = sorted(res, key=lambda x:x[1], reverse = True)[:n]
    res2 = []
    for x in res_ord:
        res2.append(x[0])
        
    return res2

def ciudades_top_tiempo_dificultad(rutas: list[Ruta], n: int):
    '''
    Dada  una  lista  de  tuplas  de  tipo  Ruta  y  un  valor  entero  n, obtener  un 
    diccionario que relacione cada dificultad con las ciudades de inicio de las n rutas con zona de descanso que 
    han tardado más tiempo en hacerse, ordenadas de mayor a menor tiempo. Si suponemos que la velocidad 
    de las rutas ha sido siempre constante y con valor vel_min, podemos calcular el tiempo usando la fórmula 
    t = km/vel_min. El parámetro n tendrá un valor por defecto igual a 3.
    '''
    res = defaultdict(list)
    for x in rutas:
        if x.zona_descanso:
            t = x.km/x.vel_min
            res[x.dificultad].append((x.ciudad_inicio, t))
                
    output = {}
    for dificultad, ciudades_t in res.items():
        sorted_ciudades = sorted(ciudades_t, key=lambda x: x[1])[:n]
        output[dificultad] = [ciudad for ciudad, _ in sorted_ciudades]
    return output

