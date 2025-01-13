from sistemas_solares import *

def test_lee_sistemas_solares(datos):
    print(len(datos))
    for x in datos[:6]:
        print(x)
        
if __name__ == '__main__':
    datos = lee_sistemas_solares('data/sistemas_solares.csv')
    test_lee_sistemas_solares(datos)