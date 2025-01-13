from peliculas import *

def test_leer_peliculas(datos):
    print(len(datos))
    for x in datos[:10]:
        print(x)
                
def test_genero_mas_frecuente(datos):
    res = genero_mas_frecuente(datos)
    print(res)  
          
def test_mejor_valorada_por_idioma(datos):
    res = mejor_valorada_por_idioma(datos)
    for clave, valor in res.items():
        print(f'mejor en {clave}: {valor}')
        
def test_media_calificaciones(datos):
    generos1 = {'Action', 'Adventure', 'Fake'}
    generos2 = {'Action', 'Thriller'}

    res = media_calificaciones(datos, generos1)
    print(generos1,':',res)
    res2 = media_calificaciones(datos, generos2)
    print(generos2,':',res2)
    
def test_top_n_por_genero(datos):
    res = top_n_por_genero(datos, 2)
    for clave, valor in res.items():
        print(f'{clave}: {valor}\n')
        
if __name__ == '__main__':
    datos = leer_peliculas('data/movies_fp.csv', 'data/movies_fp_genres.csv')
    # test_leer_peliculas(datos)
    # test_genero_mas_frecuente(datos)
    # test_mejor_valorada_por_idioma(datos)
    # test_media_calificaciones(datos)
    test_top_n_por_genero(datos)