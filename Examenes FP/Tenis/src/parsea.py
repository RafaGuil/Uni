from collections import *
from datetime import *

Set = namedtuple('Set', 'juegos_j1, juegos_j2')

def parsea_date(fecha: str):
    return datetime.strptime(fecha, '%d/%m/%Y').date()

def parsea_set(parse_set: str):
    set_ = parse_set.split('-')
    tupla = Set(int(set_[0]), int(set_[1]))

    return tupla