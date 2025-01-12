from datetime import *

def parsea_precio(precio: str):
    limpia = precio.split('/')
    
    if len(limpia) > 1:
        return float(limpia[0]), float(limpia[1])
    elif len(limpia) == 1:
        return float(limpia[0]), float(limpia[0])
    
def parsea_fecha(fecha: str):
    return datetime.strptime(fecha, "%Y-%m-%d")