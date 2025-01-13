from collections import *
from datetime import *
from typing import *
from parsea import *
import csv

Pelicula = namedtuple('Pelicula', ['id', 'title', 'original_language', 'release_date', 'vote_average', 'popularity', 'adult', 'genres']) 

def leer_peliculas(nombre_archivo_peliculas, nombre_archivo_generos):
    peliculas = []
    with open(nombre_archivo_peliculas, encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for id,title,original_language,release_date,vote_average,popularity,adult in lector:
            release_date = parsea_date(release_date)
            vote_average = float(vote_average)
            popularity = int(popularity)
            adult = bool(adult)
            for clave, valor in leer_diccionario_generos(nombre_archivo_generos).items():
                if clave == id:
                    genres = valor
            tupla = Pelicula(id,title,original_language,release_date,vote_average,popularity,adult,genres)
            peliculas.append(tupla)
    return peliculas
    
    
def leer_diccionario_generos(nombre_archivo_generos):
    res = defaultdict(set)
    with open(nombre_archivo_generos, encoding='utf-8') as c:
        lector2 = csv.reader(c, delimiter=':')
        next(lector2)
        for clave, valor in lector2:
            valor2 = valor.split(',')
            for x in valor2:
                res[clave].add(x.strip())
            
    return res

def genero_mas_frecuente(peliculas: List[Pelicula]):
    '''
    Implemente  una  función  genero_mas_frecuente que  tome  una  lista  de  tuplas  de  tipo  Pelicula y  genere 
    una tupla con el nombre del género más frecuente y su frecuencia.
    '''
    res = defaultdict(int)
    for x in peliculas:
        for i in x.genres:
            res[i] += 1
        
    return max(res.items(), key=lambda x:x[1])

def mejor_valorada_por_idioma(peliculas: List[Pelicula]):
    '''
    Escriba una función mejor_valorada_por_idioma que tome una lista de tuplas de tipo Pelicula y genere 
    un  diccionario  en  el  que  las  claves  sean  los  idiomas  y  el  valor  asociado  a  cada  clave  sea  la  película  mejor 
    valorada en el idioma al que hace referencia la clave. 
    La película mejor valorada en un idioma se define como aquella que tenga la mayor popularidad, y en caso de 
    empate  en  popularidad,  se  seleccionará  la  película  con  la  mejor  calificación  promedio  otorgada  por  los 
    usuarios.
    '''
    res = defaultdict(list)
    for x in peliculas:
        res[x.original_language].append(x)
        
    res2 = defaultdict(str)
    for clave, valor in res.items():
        res2[clave] = max(valor, key=lambda x: (x.popularity, x.vote_average))
        
    return res2

def media_calificaciones(peliculas: List[Pelicula], generos: Set[str]):
    '''
    Escriba una función llamada media_calificaciones que tome como entrada lista de tuplas de tipo Pelicula 
    y un conjunto de géneros, y devuelva la media de las calificaciones promedio (vote_average) de las películas 
    que contengan todos los géneros dados como parámetro. 
    '''
    res = []
    for x in peliculas:
        if generos.issubset(x.genres): #Lo del issubset es de hijo de puta. No hace falta saberse todas las funcioncitas de los set, pa saberlo he escrito if generos. y me puesto a leer lo que hacía cada función
            res.append(x.vote_average)
                
    return sum(res)/len(res) if len(res) > 0 else 0.0

def top_n_por_genero(peliculas: List[Pelicula], n: int):
    '''
    Escriba una función llamada top_n_por_genero que tome como entrada lista de tuplas de tipo Pelicula y un 
    valor entero n, y devuelva un diccionario en el que las claves sean los géneros y el valor asociado a cada clave 
    sea una lista con las n películas de ese género con mayor calificación promedio (vote_average). 
    '''
    res = defaultdict(list)
    for x in peliculas:
        for i in x.genres:
            res[i].append(x)
            
    res2 = {}
    for clave, valor in res.items():
        valor_ord = sorted(valor, key=lambda x:x.vote_average, reverse=True)[:n]
        res2[clave] = valor_ord
            
    return res2