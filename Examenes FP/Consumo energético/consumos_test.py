from consumos import *

def test_lee_consumos(datos):
    print(len(datos))
    for x in datos[:10]:
        print(x)
        
def test_barrios_top_consumo(datos):
    res = barrios_top_consumo(datos, 2020, "Energia activa", 3)
    print(res)
    
def test_media_consumo_edificios(datos):
    clase = "Energia reactiva"
    res = media_consumo_edificios(datos, clase)
    print(f'si se invoca a la función con la clase {clase.upper()}, el resultado sería: {res}')
     
def test_media_consumos_de_edificio_por_tipo_edificio(datos):
    clase = "Energia reactiva"
    res = media_consumos_de_edificio_por_tipo_edificio(datos, 2020, clase)
    for x in res.items():
        print(x)
        
def test_incremento_anual_de_consumo_por_unidad(datos):
    res = incremento_anual_de_consumo_por_unidad(datos, 'kVAr')
    print(res)

        
if __name__ == '__main__':
    datos = lee_consumos('data/consumo_energia_edificios.csv')
    # test_lee_consumos(datos)
    # test_barrios_top_consumo(datos)
    # test_media_consumo_edificios(datos)
    # test_media_consumos_de_edificio_por_tipo_edificio(datos)
    test_incremento_anual_de_consumo_por_unidad(datos)