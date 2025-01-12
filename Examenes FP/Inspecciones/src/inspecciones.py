from collections import *
from parsea import *
from typing import *
import csv

Inspeccion = namedtuple('Inspeccion', 'fecha_inspeccion, estacion, numero, fecha_limite, matricula, tipo, fecha_matriculacion, favorable')

def lee_inspecciones(csv_filename: str):
    inspecciones = []
    with open (csv_filename, encoding='utf-8') as f:
        lector = csv.reader(f, delimiter=';')
        next(lector)
        for fecha_inspeccion, estacion, numero, fecha_limite, matricula, tipo, fecha_matriculacion, favorable in lector:
            fecha_inspeccion = parsea_fecha(fecha_inspeccion)
            estacion = str(estacion)
            numero = int(numero)
            fecha_limite = parsea_fecha(fecha_limite)
            matricula = str(matricula)
            tipo = str(tipo)
            fecha_matriculacion = parsea_fecha(fecha_matriculacion)
            favorable = parsea_bool(favorable)
            tupla = Inspeccion(fecha_inspeccion, estacion, numero, fecha_limite, matricula, tipo, fecha_matriculacion, favorable)
            inspecciones.append(tupla)
            
    return inspecciones

def vehiculos_mas_antiguos(inspecciones: List[Inspeccion], año: int, n: int):
    res = []
    for x in inspecciones:
        if x.favorable and x.fecha_inspeccion.year == año:
            res.append((x.matricula, x.fecha_matriculacion))
            
    res_ord = sorted(res, key=lambda x:x[1], reverse=True)[:n]
    
    res2 = []
    for x, _ in res_ord:
        res2.append(x)
        
    return res2