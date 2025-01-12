from datetime import *

def parsea_date(date: str):
    return datetime.strptime(date, "%d/%m/%Y").date()

def parsea_datetime(date: str):
    return datetime.strptime(date, "%d/%m/%Y %H:%M:%S")

def parsea_bool(datos: str):
    res = None
    if datos == 'S':
        res = True
    elif datos == 'N':
        res = False
    return res

def parsea_lista(numeros: str):
    res = []
    for x in numeros.split(','):
        res.append(int(x))

    return res