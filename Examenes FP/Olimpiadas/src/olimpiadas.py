from collections import *
from datetime import *
from typing import * 
from parsea import *
import csv

Medallas = NamedTuple('Medallas', [('oro', int), ( 'plata', int),  ('bronce', int)]) 
Registro = NamedTuple('Registro', [ 
   ('ciudad_olimpica', str),  
   ('fecha_inicio', date),  
   ('pais', str),  
   ('deporte', str), 
   ('num_participantes', int),  
   ('genero', str),  
   ('medallas', Medallas),   
   ('sede', bool)])


def lee_registros_olimpiadas(filename: str) -> List[Registro]:
    registros = []
    with open (filename, encoding= 'utf-8') as f:
        lector =csv.reader(f)
        next(lector)
        for ciudad_olimpica, fecha_inicio, pais, deporte, num_participantes, genero, medallas, sede in lector:
            ciudad_olimpica = str(ciudad_olimpica)
            fecha_inicio = ParseaFecha(fecha_inicio)
            pais = str(pais)
            deporte = str(deporte)
            num_participantes = int(num_participantes)
            genero = str(genero)
            medallas = ParseaMedallas(medallas)
            sede = ParseaSede(sede)
            tupla = Registro(ciudad_olimpica, fecha_inicio, pais, deporte, num_participantes, genero, medallas, sede)
            registros.append(tupla)
            
    return registros

def deportes_ambos_generos(registros: List[Registro], anyo: int) -> Set[str]:
    res = defaultdict(set)
    for x in registros:
        if anyo == x.fecha_inicio.year:
            res[x.deporte].add(x.genero)
            
    res2 = set()
    for clave, valor in res.items():
        if len(valor) == 2:
            res2.add(clave)
            
    return res2

def deportes_mas_frecuentes(registros: List[Registro], n: int, genero: str) ->  Dict[str, List[Tuple[str, int]]]:
    res = defaultdict(int)
    for x in registros:
        if x.genero == genero:
            res[x.deporte] += 1
            
    res_ord = sorted(res.items(), key=lambda x:x[1], reverse=True)[:n]
    
    return res_ord

def deporte_con_mas_paises_distintos_con_oro(registros: List[Registro], genero: Optional[str] = None) -> str :
    res = defaultdict(set)
    for x in registros:
        if (genero is None or x.genero == genero) and x.medallas.oro > 0:
            res[x.deporte].add(x.pais)
            
    res_max = max(res.items(), key=lambda x:len(x[1]))
            
    return res_max[0]

def deportes_mas_participantes_de_genero_por_juego(registros: List[Registro], pais: str, genero: str) -> Dict[str, List[str]]:
    res = defaultdict(list)
    for x in registros:
        if x.pais == pais and x.genero == genero:
            res[idPais(x.ciudad_olimpica, x.fecha_inicio.year)].append((x.deporte, x.num_participantes))
            
    res_ord = {}
    for clave, valor in res.items():
        res_ord[clave] = sorted(valor, key=lambda x:x[1], reverse=True)[:3]
            
    return res_ord.items()

def deporte_con_todos_los_paises(registros: List[Registro]) -> bool:
    res = defaultdict(set)
    paises = set()
    for x in registros:
        paises.add(x.pais)
        res[x.deporte].add(x.pais)
        
    for _, valor in res.items():
        if len(paises) == len(valor):
            return True
        else:
            return False
        
def anyo_con_mayor_incremento_participantes_de_pais(registros: List[Registro], pais: str) -> Tuple[int, int]:
    res = defaultdict(int)
    for x in registros:
        if x.pais == pais:
            res[x.fecha_inicio.year] += x.num_participantes

    res_ord = sorted(res.items(), key=lambda x:x[0])
    res2 = []
    for x, y in zip(res_ord, res_ord[1:]):
        res2.append((y[0], y[1] - x[1]))
        
    return max(res2, key=lambda x:x[1])