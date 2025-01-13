from typing import NamedTuple, List, Set, Tuple, Dict, Optional
from collections import *
from datetime import *
from parsea import *
import csv

Planeta = NamedTuple("Planeta", [
    ("nombre", str),          # Nombre del planeta
    ("distancia_ua", float),  # Distancia al sol del sistema en UA
    ("con_lunas", bool)       # Si tiene lunas o no
])

SistemaSolar = NamedTuple("SistemaSolar", [
    ("nombre", str),           # Nombre del sistema solar
    ("observador", str),       # Nombre del observador
    ("planetas", List[Planeta]), # Lista de planetas
    ("distancia_luz", float),  # Distancia a la Tierra en años luz
    ("notas", Optional[str])   # Notas adicionales (pueden estar vacías)
])

def lee_sistemas_solares(csv_filename: str) -> List[SistemaSolar]:
    sistemas = []
    with open(csv_filename, encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for sistema,observador,planetas,distancia_luz,notas in lector:
            nombre = str(sistema)
            observador = str(observador)
            planetas = parsea_planetas(planetas)
            distancia_luz = parsea_distancia_luz(distancia_luz)
            notas = parsea_notas(notas)
            tupla = SistemaSolar(nombre,observador,planetas,distancia_luz,notas)
            sistemas.append(tupla)
            
    return sistemas