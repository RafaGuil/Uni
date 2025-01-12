from festivales import *

def test_lee_festivales(datos):
    print('Test Ej1: lee_festivales')
    print(f'Total festivales: {len(datos)}')
    print(datos[:2])
    print('========================================')
    
def test_total_facturado(datos):
    print('Test Ej2: total_facturado')
    res = total_facturado(datos, None, None)
    print(res)
    res2 = total_facturado(datos, None, date(2024, 6, 15))
    print(res2)
    res3 = total_facturado(datos, date(2024, 6, 15), None)
    print(res3)
    res4 = total_facturado(datos, date(2024, 6, 1), date(2024, 6, 15))
    print(res4)
    res5 = total_facturado(datos, date(2024, 6, 1), date(2024, 6, 23))
    print(res5)
    print('========================================')
    
def test_artista_top(datos):
    print('Test Ej3: artista_top')
    res = artista_top(datos)
    print(res)
    print('========================================')
    
def test_mes_mayor_beneficio_medio(datos):
    print('Test Ej4: mes_mayor_beneficio_medio')
    res = mes_mayor_beneficio_medio(datos)
    print(res)
    print('========================================')

def test_artistas_comunes(datos):
    print('Test Ej5: artistas_comunes')
    res = artistas_comunes(datos, 'Creamfields', 'Tomorrowland')
    print(res)
    res2 = artistas_comunes(datos, 'Primavera Sound', 'Coachella')
    print(res2)
    
def test_festivales_top_calidad_por_duracion(datos):
    print('Test 6: festivales_top_mejor_ratio')
    res = festivales_top_calidad_por_duracion(datos, n=3)
    for x in res:
        print(x)
    
if __name__ == '__main__':
    datos = lee_festivales('data/fichero.csv')
    # test_lee_festivales(datos)
    # test_total_facturado(datos)
    # test_artista_top(datos)
    # test_mes_mayor_beneficio_medio(datos)
    # test_artistas_comunes(datos)
    test_festivales_top_calidad_por_duracion(datos)