from typing import NamedTuple, List, Set, Tuple, Dict, Optional
from collections import *
from datetime import *
from parsea import *

Planeta = NamedTuple("Planeta", [
    ("nombre", str),          # Nombre del planeta
    ("distancia_ua", float),  # Distancia al sol del sistema en UA
    ("con_lunas", bool)       # Si tiene lunas o no
])


def parsea_planetas(planetas_str: str) -> List[Planeta]: 
    planetas = []
    limpia = planetas_str.split(';')
    for x in limpia:
        limpia2 = x.split('#')
        nombre = limpia2[0]
        distancia_ua = limpia2[1]
        con_lunas = parsea_lunas(limpia2[2])
        tupla = Planeta(nombre, float(distancia_ua), con_lunas)
        planetas.append(tupla)
    return planetas

def parsea_lunas(n: str) -> bool:
    res = None
    if n == '0':
        res = False
    else:
        res = True
    return res

def parsea_distancia_luz(distancia_str: str) -> float:
    res = float(distancia_str)
    return round(res, 2)

def parsea_notas(notas: str) -> Optional[str]:
    return notas.strip('[]')