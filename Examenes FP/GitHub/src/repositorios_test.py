from repositorios import *

def test_lee_repositorios(datos):
    print(len(datos))
    for x in datos[:5]:
        print(x)
        
def test_total_commits_por_anyo(datos):
    res = total_commits_por_anyo(datos)
    print(res)
    
def test_n_mejores_repos_por_tasa_crecimiento(datos):
    res = n_mejores_repos_por_tasa_crecimiento(datos)
    print(res)
    
def test_recomendar_lenguajes(datos):
    res = recomendar_lenguajes(datos, datos[0])
    print(res)
    
def test_media_minutos_entre_commits_por_usuario(datos):
    res = media_minutos_entre_commits_por_usuario(datos, None, None)
    for x, i in res.items():
        print(f'{x}: {i}')
    
if __name__ =='__main__':
    datos = lee_repositorios('data/repositorios.csv')
    # test_lee_repositorios(datos)
    # test_total_commits_por_anyo(datos)
    test_n_mejores_repos_por_tasa_crecimiento(datos)
    # test_recomendar_lenguajes(datos)
    # test_media_minutos_entre_commits_por_usuario(datos)