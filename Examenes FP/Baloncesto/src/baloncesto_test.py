from baloncesto import *

def test_lee_partidos(datos):
    print(len(datos))
    for x in datos[:3]:
        print(x)
        
    print(datos[0])
    print(datos[10])
        
def test_equipo_con_mas_faltas(datos):
    res = equipo_con_mas_faltas(datos)
    print('Test de equipo_mas_faltas:')
    print(res)
    
def test_media_puntos_por_equipo(datos):
    res = media_puntos_por_equipo(datos, 'Copa del Rey')
    print('Test de media_puntos_por_equipo (competicion=Copa del Rey): ')
    print(res)
    
def test_diferencia_puntos_anotados(datos):
    res = diferencia_puntos_anotados(datos, 'Barcelona')
    print('Test de diferencia_puntos_anotados (equipo=Barcelona)')
    print(res)
    
def test_victorias_por_equipo(datos):
    res = victorias_por_equipo(datos)
    print('Test de victorias_por_equipo')
    print(res)
    
def test_equipos_minimo_victorias(datos):
    res = equipos_minimo_victorias(datos, 8)
    print('Test de equipos_minimo_victorias (n=8)')
    print(res)

def test_equipos_mas_victorias_por_año(datos):
    res = equipos_mas_victorias_por_año(datos, 8)
    print('Test de equipos_mas_victorias_por_año (n=8)')
    print(res)

    
if __name__ == '__main__':
    datos = lee_partidos('data/resultados_baloncesto.csv')
    # test_lee_partidos(datos)
    # test_equipo_con_mas_faltas(datos)
    # test_media_puntos_por_equipo(datos)
    # test_diferencia_puntos_anotados(datos)
    # test_victorias_por_equipo(datos)
    # test_equipos_minimo_victorias(datos)
    test_equipos_mas_victorias_por_año(datos)