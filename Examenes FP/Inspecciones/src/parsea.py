from datetime import *

def parsea_fecha(fecha: str):
    return datetime.strptime(fecha, '%d/%m/%Y').date()

def parsea_bool(datos):
    if datos == 'S':
        return True
    elif datos == 'N':
        return False