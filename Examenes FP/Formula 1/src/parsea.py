from datetime import *

def ParseaFecha(fecha_carrera):
    return datetime.strptime(fecha_carrera, '%d-%m-%y').date()

def ParseaLiquido(nivel_liquido):
    if nivel_liquido == '1':
        return True
    else:
        return False