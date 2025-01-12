from olimpiadas import *

def test_lee_registros_olimpiadas(datos):
    print('TEST EJERCICIO 1 ########################################')
    print(f'Se han leído {len(datos)} registros')
    print(datos[:2])
    
def test_deportes_ambos_generos(datos):
    print('TEST EJERCICIO 2 ########################################')
    res = deportes_ambos_generos(datos, 1984)
    print(res)
    
def test_deportes_mas_frecuentes(datos):
    print('TEST EJERCICIO 3 ########################################')
    res = deportes_mas_frecuentes(datos, 4, 'HOMBRE')
    print(res)
    res2 = deportes_mas_frecuentes(datos, 5, 'MUJER')
    print(res2)
    
def test_deporte_con_mas_paises_distintos_con_oro(datos):
    print('TEST EJERCICIO 4 ########################################')
    res = deporte_con_mas_paises_distintos_con_oro(datos, None)
    print(res)
    res2 = deporte_con_mas_paises_distintos_con_oro(datos, 'HOMBRE')
    print(res2)
    res3 = deporte_con_mas_paises_distintos_con_oro(datos, 'MUJER')
    print(res3)
    
def test_deportes_mas_participantes_de_genero_por_juego(datos):
    print('TEST EJERCICIO 5 ########################################')
    res = deportes_mas_participantes_de_genero_por_juego(datos, 'ESPAÑA', 'MUJER')
    for x in res:
        print(x)
        
def test_deporte_con_todos_los_paises(datos):
    print('TEST EJERCICIO 6 ########################################')
    res = deporte_con_todos_los_paises(datos)
    print(res)
    
def test_anyo_con_mayor_incremento_participantes_de_pais(datos):
    print('TEST EJERCICIO 7 ########################################')
    res = anyo_con_mayor_incremento_participantes_de_pais(datos, 'ESPAÑA')
    print(res)

if __name__ == '__main__':
    datos = lee_registros_olimpiadas('data/olimpiadas.csv')
    # test_lee_registros_olimpiadas(datos)
    # test_deportes_ambos_generos(datos)
    # test_deportes_mas_frecuentes(datos)
    # test_deporte_con_mas_paises_distintos_con_oro(datos)
    # test_deportes_mas_participantes_de_genero_por_juego(datos)
    # test_deporte_con_todos_los_paises(datos)
    test_anyo_con_mayor_incremento_participantes_de_pais(datos)