from inspecciones import *

def test_lee_inspecciones(datos):
    print(len(datos))
    for x in datos[:2]:
        print(x)
        
def test_vehiculos_mas_antiguos(datos):
    res = vehiculos_mas_antiguos(datos, 2022, 3)
    print(res)
    
if __name__ == '__main__':
    datos = lee_inspecciones('data/inspecciones.csv')
    # test_lee_inspecciones(datos[:2])
    test_vehiculos_mas_antiguos(datos)