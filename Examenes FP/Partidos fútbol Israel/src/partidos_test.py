from partidos import *

def test_lee_resultados(datos):
    print(len(datos))
    for x in datos[:2]:
        print(x)
        
def test_selecciones_enfrentadas_israel(datos):
    res = selecciones_enfrentadas_israel(datos)
    print(res)
    
def test_lista_diferencias_goles(datos):
    res = lista_diferencias_goles(datos, None, None)
    print(res)
    
def test_partidos_por_mes(datos):
    res = partidos_por_mes(datos)
    print(res)
    
def test_partidos_mensuales_por_anyo(datos):
    res = partidos_mensuales_por_anyo(datos)
    for x in res:
        print(x)
    
if __name__ == '__main__':
    datos = lee_resultados('data/resultadosIsrael.csv')
    # test_lee_resultados(datos)
    # test_selecciones_enfrentadas_israel(datos)
    # test_lista_diferencias_goles(datos)
    # test_partidos_por_mes(datos)
    test_partidos_mensuales_por_anyo(datos)