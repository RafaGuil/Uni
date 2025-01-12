from tenis import *

def test_lee_partidos_tenis(datos):
    print('EJERCICIO 1---------------------------------------------------------------------------')
    print('Test de lee_partidos_tenis')
    print(f'Número total de partidos leidos: {len(datos)}')
    print('Mostrando los tres primeros registros leídos:')
    for x, i in zip(datos[:3], range(1,4)):
        print(f'{i}-{x}')
        
def test_tenista_mas_victorias(datos):
    print('EJERCICIO 2---------------------------------------------------------------------------')
    print('Test de tenista_mas_victorias fecha1=None, fecha2=None')
    res = tenista_mas_victorias(datos)
    print(f'El tenista con más victorias entre las fechas None y None es {res}')
    print('Test de tenista_mas_victorias fecha1=None, fecha2=2020-01-01')
    res2 = tenista_mas_victorias(datos, f2=date(2020,1,1))
    print(f'El tenista con más victorias entre las fechas None y 2020-01-01 es {res2}')
    print('Test de tenista_mas_victorias fecha1=2020-01-01, fecha2=None')
    res3 = tenista_mas_victorias(datos, f1=date(2020,1,1))
    print(f'El tenista con más victorias entre las fechas 2020-01-01 y None es {res3}')
    print('Test de tenista_mas_victorias fecha1=2013-01-01, fecha2=2020-01-01')
    res4 = tenista_mas_victorias(datos, f1 = date(2013,1,1), f2=date(2020,1,1))
    print(f'El tenista con más victorias entre las fechas 2013-01-01 y 2020-01-01 es {res4}')


    
def test_n_tenistas_con_mas_errores(datos):
    print('EJERCICIO 3---------------------------------------------------------------------------')
    print('Test de n_tenistas_con_mas_errores n=5')
    print('Los 5 tenistas con mas errores son:')
    num=5
    res = n_tenistas_con_mas_errores(datos, num)
    for x, i in zip(res, range(1, num+1)):
        print(f'{i}-{x}')
        
def test_num_tenistas_distintos_por_superficie(datos):
    print('EJERCICIO 4---------------------------------------------------------------------------')
    print('Test de num_tenistas_distintos_por_superficie')
    print('El número de tenistas distintos segun cada superficie es')
    res = num_tenistas_distintos_por_superficie(datos)
    for clave, valor in res.items():
        print(f'{clave} --> {valor}')
        
def test_partido_mas_errores_por_mes(datos):
    print('EJERCICIO 5 --------------------------------------------------------------------------')
    print('Test de partido_mas_errores_por_mes superficies=[Sintética]')
    print('Los partidos con mas errores para las superificies [Sintética] son')
    res = partido_mas_errores_por_mes(datos, ['Sintética'])
    for clave, valor in res.items():
        print(f'{clave} --> {valor}')
    print('\n')
    
    print('Los partidos con mas errores para las superificies [Sintética, Tierra] son')
    res = partido_mas_errores_por_mes(datos, ['Sintética', 'Tierra'])
    for clave, valor in res.items():
        print(f'{clave} --> {valor}')
    print('\n')
    
    print('Los partidos con mas errores para las superificies=None son')
    res = partido_mas_errores_por_mes(datos)
    for clave, valor in res.items():
        print(f'{clave} --> {valor}')


        
if __name__ == '__main__':
    datos = lee_partidos_tenis('data/partidos.csv')
    # test_lee_partidos_tenis(datos)
    # test_tenista_mas_victorias(datos)
    # test_n_tenistas_con_mas_errores(datos)
    # test_num_tenistas_distintos_por_superficie(datos)
    test_partido_mas_errores_por_mes(datos)