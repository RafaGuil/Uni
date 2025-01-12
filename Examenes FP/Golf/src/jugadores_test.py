from jugadores import *

def test_lee_jugadores(datos):
    print(f'Registros leídos: {len(datos)}')
    print('Los dos primeros:')
    for x in datos[:2]:
        print(x)
    
def test_mejores_jugadores(datos):
    res = mejores_jugadores(datos, 1969, 4)
    print(f'los {res[2]} mejores jugadores nacidos en el {res[1]} son: {res[0]}')
    
def test_jugadores_por_golpes(datos):
    res = jugadores_por_golpes(datos)
    print('Jugadores por golpes')
    for x in res:
        print(x)
        
def test_promedio_ultimos_resultados(datos):
    res = promedio_ultimos_resultados(datos, datetime(2020, 3, 1), datetime(2020, 5, 31))
    print(f'El promedio de cada jugador senior con fecha de actualización entre {res[1]} y {res[2]} son:')
    for x in res[0]:
        print(x)
        
def test_jugador_menor_handicap_por_federacion(datos):
    res = jugador_menor_handicap_por_federacion(datos)
    print('Los mejores jugadores de cada federación son:')
    for x in res.items():
        print(x)
    
if __name__ == '__main__':
    datos = lee_jugadores('data/jugadores.csv')
    # test_lee_jugadores(datos)
    # test_mejores_jugadores(datos)
    # test_jugadores_por_golpes(datos)
    # test_promedio_ultimos_resultados(datos)
    test_jugador_menor_handicap_por_federacion(datos)