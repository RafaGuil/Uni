from collections import *
from datetime import * 
from typing import *
from parsea import *
import csv

Receta = NamedTuple("Receta",  
                    [("nombre", str), 
                     ("tipo", str), 
                     ("dificultad", str), 
                     ("ingredientes", Optional[List[str]]), 
                     ("tiempo_preparacion", int), 
                     ("calorias", int), 
                     ("fecha_creacion", date), 
                     ("precio_estimado", float) 
                    ])

def lee_recetas(filename: str) -> List[Receta]:
    recetas = []
    with open (filename, encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for nombre,tipo,dificultad,ingredientes,tiempo_preparacion,calorias,fecha_creacion,precio_estimado in lector:
            nombre = str(nombre)
            tipo = str(tipo)
            dificultad = str(dificultad)
            ingredientes = ParseaIngredientes(ingredientes)
            tiempo_preparacion = int(tiempo_preparacion)
            calorias = int(calorias)
            fecha_creacion = ParseaFecha(fecha_creacion)
            precio_estimado = float(precio_estimado)
            tupla = Receta(nombre,tipo,dificultad,ingredientes,tiempo_preparacion,calorias,fecha_creacion,precio_estimado)
            recetas.append(tupla)
            
    return recetas

def receta_mas_barata(recetas: List[Receta], 
                        tipos: Set[str],  
                        n: Optional[int] = None) -> Receta:
    res = []
    for x in recetas:
        if x.tipo in tipos:
            res.append(x)
    
    if n is None:
        res_ord = sorted(res, key=lambda x:x[5])[:n]
    else:
        res_ord = sorted(res, key=lambda x:x[5])
    
    return min(res_ord, key=lambda x:x[-1])

def obten_ingredientes(recetas: List[Receta],  
                          mes1: Optional[int] = None, 
                          mes2: Optional[int] = None) -> Set[str]:
    res = set()
    for x in recetas:
        if (mes1 == None or mes1 <= x.fecha_creacion.month) and (mes2 == None or mes2 > x.fecha_creacion.month) and x.ingredientes != None:
            for i in x.ingredientes:
                res.add(i)
                
    return res

def recetas_con_precio_menor_promedio(recetas: List[Receta], n: int) -> List[Tuple[str, int]]:
    res = []
    for x in recetas:
        if x.precio_estimado <= MediaPrecio(recetas):
            res.append((x.nombre, x.calorias))
            
    res_ord = sorted(res, key=lambda x:x[1])[:n]
    
    return res_ord
            
def MediaPrecio(recetas: List[Receta]):
    media = 0
    count = 0
    for x in recetas:
        media += x.precio_estimado
        count += 1
        
    return media / count

def receta_mas_ingredientes(recetas: List[Receta],  
                           ingredientes: Optional[Set[str]] = None) -> Tuple[str, List[str]]:
    res = []
    for x in recetas:
        if x.ingredientes != None and (ingredientes is None or ingredientes.intersection(x.ingredientes)):
            res.append((x.nombre, x.ingredientes))
            
    res_ord = max(res, key=lambda x:len(x[1]))
            
    return res_ord

def ingredientes_mas_comunes_por_tipo(recetas: List[Receta]) -> Dict[str, List[str]]:
    res = defaultdict(lambda: defaultdict(int))
    for x in recetas:
        if x.ingredientes is not None:
            for i in x.ingredientes:
                res[x.tipo][i] += 1
     
    res_ord = {}   
    for clave, valor in res.items():
        valor_ord = sorted(valor.items(), key=lambda x:x[1], reverse=True)[:3]
        res_ord[clave] = valor_ord
        
    return res_ord

def mes_con_precio_medio_mas_alto(recetas: List[Receta], n: int) -> int:
    res = defaultdict(float)
    count = defaultdict(int)
    for x in recetas:
        res[x.fecha_creacion.month] += x.precio_estimado
        count[x.fecha_creacion.month] += 1
        
    for x in res:
        res[x] /= count[x]
         
    return res