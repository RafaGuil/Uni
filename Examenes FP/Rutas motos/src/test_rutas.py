from rutas import *

def test_lee_rutas(datos):
    print(len(datos))
    print(datos[:2])
    
def test_acumular_kms_por_meses(datos):
    res = acumular_kms_por_meses(datos)
    print(res)
    
def test_diferencias_kms_meses_anyo(datos):
    res = diferencias_kms_meses_anyo(datos)
    print(res)
    
def test_top_rutas_lejanas(datos):
    res = top_rutas_lejanas(datos, 2, (35.15, -8.76), None)
    for x in res:
        print(x)
        
def test_ciudades_top_tiempo_dificultad(datos):
    res = ciudades_top_tiempo_dificultad(datos, 3)
    for clave, valor in res.items():
        print(f'{clave}: {[x for x in valor]}')
    
if __name__ =='__main__':
    datos = lee_rutas('data/rutas_motos.csv')
    # test_lee_rutas(datos)
    # test_acumular_kms_por_meses(datos)
    # test_diferencias_kms_meses_anyo(datos)
    # test_top_rutas_lejanas(datos)
    test_ciudades_top_tiempo_dificultad(datos)