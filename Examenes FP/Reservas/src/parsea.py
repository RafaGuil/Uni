from datetime import *

def parseaFecha(fecha):
    return datetime.strptime(fecha, '%Y-%m-%d').date()

def parseaServicios(servicios: str):
    res = []
    if len(servicios) == 0:
        return res
    elementos = servicios.split(',')
    for x in elementos:
        res.append(x)
        
    return res

def diasReserva(fecha_entrada: datetime, fecha_salida: datetime):
    return (fecha_salida - fecha_entrada).days
