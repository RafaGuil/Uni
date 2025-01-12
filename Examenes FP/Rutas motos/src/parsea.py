from collections import *
from datetime import *

Coordenada = namedtuple('Coordenada', 'latitud, longitud')

def parsea_coordenada(latitud_longitud: str):
    latitud = latitud_longitud.split('/')[0]
    longitud  = latitud_longitud.split('/')[1]
    
    return Coordenada(float(latitud), float(longitud))

def parsea_fecha(fecha):
    if len(fecha) > 0:
        return datetime.strptime(fecha, "%m/%d/%Y").date()
    else:
        return datetime.today().date()