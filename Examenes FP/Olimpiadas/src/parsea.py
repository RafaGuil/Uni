from collections import *
from datetime import *
from typing import * 
from parsea import *
import csv

Medallas = NamedTuple('Medallas', [('oro', int), ( 'plata', int),  ('bronce', int)]) 

def ParseaFecha(fecha: str):
    return datetime.strptime(fecha, '%Y-%m-%d').date()

def ParseaMedallas(medallas: str):
    x = medallas.split('-')
    oro = int(x[0])
    plata = int(x[1])
    bronce = int(x[2])
        
    return Medallas(oro, plata, bronce)

def ParseaSede(sede: str):
    if sede == 'SI':
        return True
    else:
        return False
    
def idPais(ciudad_olimpica: str, año: str):
    return str(ciudad_olimpica) + str(año)[-2:]