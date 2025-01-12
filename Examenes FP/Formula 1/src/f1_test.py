from f1 import *

def test_lee_carreras(datos):
    print(datos[:1])
    
def test_media_tiempo_boxes(datos):
    res = media_tiempo_boxes(datos, 'Barcelona')
    print(res)
    
def test_pilotos_menor_tiempo_medio_vueltas_top(datos):
    res = pilotos_menor_tiempo_medio_vueltas_top(datos, 4)
    print(res)
    
def test_ratio_tiempo_boxes_total(datos):
    res = ratio_tiempo_boxes_total(datos)
    print(res)

def test_puntos_piloto_anyos(datos):
    res = puntos_piloto_anyos(datos)
    print(res)
    
def test_mejor_escuderia_anyo(datos):
    res = mejor_escuderia_anyo(datos, 2022)
    print(res)
    
if __name__ == '__main__':
    datos = lee_carreras('data/f1.csv')
    # test_lee_carreras(datos)
    # test_media_tiempo_boxes(datos)
    # test_pilotos_menor_tiempo_medio_vueltas_top(datos)
    # test_ratio_tiempo_boxes_total(datos)
    test_puntos_piloto_anyos(datos)
    # test_mejor_escuderia_anyo(datos)