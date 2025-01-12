from datetime import *

def parsea_fecha(fecha: str):
    return datetime.strptime(fecha, '%d/%m/%Y').date()

def parsea_consumo(consumo: str):
    if consumo == 'NO DATA' or consumo == '':
        res = None
    else:
        res = float(consumo.replace(',', '.'))
        
    return res