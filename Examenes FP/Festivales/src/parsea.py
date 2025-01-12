from datetime import *
from typing import *

Artista = NamedTuple("Artista",      
                        [("nombre", str),  
                        ("hora_comienzo", time),  
                        ("cache", int)]) 



def ParseaFecha(fecha):
    return datetime.strptime(fecha, "%Y-%m-%d").date()

def ParseaArtista(artistas: str):
    res = []
    
    limpia1 = artistas.split("-")
    for x in limpia1:
        limpia2 = x.split("_")
        nombre = str(limpia2[0])
        hora = datetime.strptime(limpia2[1], "%H:%M").time()
        cache = int(limpia2[2])*1000
        
        tupla = Artista(nombre, hora, cache)
        res.append(tupla)
        
    return res

def ParseaTop(top):
    res = False
    if top == 'sí':
        res = True
        
    return res

