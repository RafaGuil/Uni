import csv
from parsea import *
from collections import *

Carrera = namedtuple("Carrera", "nombre,escuderia,fecha_carrera,temperatura_min,vel_max,duracion,posicion_final,ciudad,top_6_vueltas,tiempo_boxes,nivel_liquido")

def lee_carreras(archivo):
    carreras = []
    with open(archivo, encoding='utf-8') as f:
        lector = csv.reader(f, delimiter=';')
        next(lector)
        for nombre,escuderia,fecha_carrera,temperatura_min,vel_max,duracion,posicion_final,ciudad,top_6_vueltas,tiempo_boxes,nivel_liquido in lector:
            nombre = str(nombre)
            escuderia = str(escuderia)
            fecha_carrera = ParseaFecha(fecha_carrera)
            temperatura_min = int(temperatura_min)
            vel_max = float(vel_max)
            duracion = float(duracion)
            posicion_final = int(posicion_final)
            ciudad = str(ciudad)
            lista_top6 = []
            top_6_vueltas = top_6_vueltas.strip('[')
            top_6_vueltas = top_6_vueltas.strip(']')
            top_6vueltas = top_6_vueltas.split('/ ')
            for x in top_6vueltas:
                if x == '-':
                    x = 0
                    lista_top6.append(x)
                lista_top6.append(float(x))
            tiempo_boxes = float(tiempo_boxes)
            nivel_liquido = ParseaLiquido(nivel_liquido)
            tupla = Carrera(nombre,escuderia,fecha_carrera,temperatura_min,vel_max,duracion,posicion_final,ciudad,lista_top6,tiempo_boxes,nivel_liquido)
            carreras.append(tupla)
    return carreras
                    
def media_tiempo_boxes(carreras, ciudad, fecha=None):
    '''
    Recibe una lista de tuplas de tipo Carrera, una ciudad y una fecha (con valor por 
    defecto None), y devuelve la media de tiempo que los pilotos han pasado en boxes en la fecha y ciudad 
    seleccionadas.  Si  la  fecha  es  None,  se  sumarán  todos  los  tiempos  de  la  ciudad  sin  tener  en  cuenta  la 
    fecha. Por otro lado, si no ha habido carreras en la fecha y ciudad seleccionada, la media debe ser 0.
    '''
    res = 0
    cont = 0
    for x in carreras:
        if x.ciudad == ciudad and (fecha is None or x.fecha_carrera == fecha):
            res += x.tiempo_boxes
            cont += 1
        
    return res/cont

def pilotos_menor_tiempo_medio_vueltas_top(carreras, n):
    '''
    Recibe una lista de tuplas de tipo Carrera y un 
    número entero n, y devuelve una lista de tuplas (nombre, fecha) con los n nombres y fechas de carrera de 
    los pilotos cuya media de tiempo en sus 6 vueltas top sea menor. No se tendrán en cuenta aquellos pilotos 
    que han sufrido un accidente y no han podido completar las 6 vueltas. (1.5 puntos)
    '''
    res = []
    for x in carreras:
        if 0 not in x.top_6_vueltas:
            res.append((x.nombre, x.fecha_carrera, sum(x.top_6_vueltas)/6))
            
    res_ord = sorted(res, key=lambda x:x[2])[:n]
    
    res2 = []
    for x in res_ord:
        res2.append((x[0], x[1]))
        
    return res2

def ratio_tiempo_boxes_total(carreras):
    '''
    Recibe una lista de tuplas de tipo Carrera, y devuelve una lista de tuplas 
    (nombre, fecha, ratio) con el nombre del piloto, la fecha de la carrera y la ratio entre su tiempo en boxes 
    con respecto al total de tiempo en boxes de todos los pilotos que han participado ese día en la carrera. La 
    lista de tuplas resultante deberá estar ordenada de mayor a menor ratio. (2 puntos)
    ''' 
    res = defaultdict(float)
    tiempo_box = defaultdict(lambda: defaultdict(float))
    
    for x in carreras:
        res[x.fecha_carrera] += x.tiempo_boxes
        tiempo_box[x.nombre][x.fecha_carrera] = x.tiempo_boxes
       
    res2 = []
    for clave, dic2 in tiempo_box.items():
        for clave2, valor3 in dic2.items():
            ratio = valor3 / res[clave2]
            res2.append((clave, clave2, ratio))
        
    return sorted(res2, key=lambda x:x[2], reverse=True)

def puntos_piloto_anyos(carreras):
    '''
    Recibe una lista de tuplas de tipo Carrera, y devuelve un diccionario que asocia 
    cada  piloto  (clave)  con  una  lista  con  los  puntos  totales  obtenidos  cada  año.  La  lista  de  puntos  estará 
    ordenada  por  año.  Para  calcular  los  puntos  obtenidos  en  cada  carrera,  debe  tener  en  cuenta  que 
    solamente obtienen puntos aquellos pilotos que quedan en las 3 primeras posiciones. Si el puesto es el 
    primero, los puntos serían 50, el segundo puesto son 25 y el tercero 10. Para esta función tiene que utilizar 
    obligatoriamente una función auxiliar que, dada una carrera, calcula el número de puntos obtenidos por 
    el piloto en esa carrera. (2 puntos)
    '''
    res = defaultdict(lambda: defaultdict(int))
    for x in carreras:
        res[x.nombre][x.fecha_carrera.year] += puntos(x.posicion_final)
            
    return res

def puntos(posicion):
    # Vaya puta peruanada el que se ha inventao las puntuaciones estas
    puntuacion = 0
    if posicion == 1:
        puntuacion = 50
    elif posicion == 2:
        puntuacion = 25
    elif posicion == 3:
        puntuacion = 10
        
    return puntuacion
            
def mejor_escuderia_anyo(carreras, a):
    '''
    Recibe una lista de tuplas de tipo Carrera y un año a, y devuelve la escudería 
    que más victorias haya conseguido en el año a. Se considera victoria cuando algún piloto de la escudería 
    queda en el primer puesto. (1.5 puntos)
    '''
    res = defaultdict(int)
    for x in carreras:
        if x.fecha_carrera.year == a and x.posicion_final == 1:
            res[x.escuderia] += 1
            
    return max(res.items(), key=lambda x:x[1])[0]