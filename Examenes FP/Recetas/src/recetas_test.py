from recetas import *

def test_lee_recetas(datos):
    print(len(datos))
    for x in datos[-2:]:
        print(x)
        
def test_receta_mas_barata(datos):
    print('=== TEST EJERCICIO 2========================================')
    res = receta_mas_barata(datos, {'Postre', 'Entrante'}, None)
    print(res)    
    res2 = receta_mas_barata(datos, 'Plato principal', 5)
    print(res2)
    
def test_obten_ingredientes(datos):
    print('=== TEST EJERCICIO 3========================================')
    res = obten_ingredientes(datos, None, None)
    print(len(res))
    print(res)
    
    res2 = obten_ingredientes(datos, 2, 4)
    print(len(res2))
    print(res2)
    
def test_recetas_con_precio_menor_promedio(datos):
    print('=== TEST EJERCICIO 4========================================')
    res = recetas_con_precio_menor_promedio(datos, 5)
    for x in res:
        print(x)
        
def test_receta_mas_ingredientes(datos):
    print('=== TEST EJERCICIO 5========================================')
    res = receta_mas_ingredientes(datos, None)
    print(res)
    res2 = receta_mas_ingredientes(datos, {'huevos', 'leche'})
    print(res2)

def test_ingredientes_mas_comunes_por_tipo(datos):
    print('=== TEST EJERCICIO 6========================================')
    res = ingredientes_mas_comunes_por_tipo(datos)
    for x in res.items():
        print(f'\t{x}\n')
        
def test_mes_con_precio_medio_mas_alto(datos):
    print('=== TEST EJERCICIO 7========================================')
    res = mes_con_precio_medio_mas_alto(datos, 5)
    print(res)

    
if __name__ == '__main__':
    datos = lee_recetas('data/recetas.csv')
    # test_lee_recetas(datos)
    # test_receta_mas_barata(datos)
    # test_obten_ingredientes(datos)
    # test_recetas_con_precio_menor_promedio(datos)
    # test_receta_mas_ingredientes(datos)
    # test_ingredientes_mas_comunes_por_tipo(datos)
    test_mes_con_precio_medio_mas_alto(datos)