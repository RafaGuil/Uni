from typing import NamedTuple,List,Set,Tuple,Dict,Optional 
from datetime import datetime,date 
from collections import *
import csv
 
Commit = NamedTuple("Commit",      
       [("id", str), # Identificador alfanumérico del commit 
        ("mensaje", str), # Mensaje asociado al commit 
        ("fecha_hora", datetime) # Fecha y hora en la que se registró el commit 
       ]) 
Repositorio = NamedTuple("Repositorio",      
      [("nombre", str),  # Nombre del repositorio 
       ("propietario", str), # Nombre del usuario propietario 
       ("lenguajes", Set[str]),  # Conjunto de lenguajes usados 
       ("privado", bool),  # Indica si es privado o público 
       ("commits", List[Commit])  # Lista de commits realizados 
       ])

def lee_repositorios(csv_filename: str) -> List[Repositorio]:
    repositorios = []
    with open (csv_filename, encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for repositorio, propietario, lenguajes, privado, commits in lector:
            nombre = str(repositorio)
            propietario = str(propietario)
            lenguajes = parsea_lenguajes(lenguajes)
            privado = True if privado == 'True' else False
            commits = parsea_commits(commits)
            tupla = Repositorio(nombre, propietario, lenguajes, privado, commits)
            repositorios.append(tupla)
    return repositorios

def parsea_commits(commits_str: str) -> List[Commit]:
    '''
    Dada una cadena de texto con los identificadores, los mensajes y las fechas/horas 
    de una lista de commits, devuelve la información como una lista de tuplas de tipo Commit. Un ejemplo 
    de esta cadena puede ser: 
    "[b789101#Initial commit#2023-10-06 12:00:00;c567891#Added main 
    functionality3#2023-10-06 13:00:00]" 
    Note que el formato esperado de la cadena recibida como parámetro separa la información de cada 
    commit por punto y coma (;). Además, para cada commit, el identificador, el mensaje y la fecha/hora 
    están separados por #. Si la cadena recibida es “[]”, la función devuelve una lista vacía.   
    Ayuda: Para "parsear" las fechas use el formato "%Y-%m-%d %H:%M:%S"
    '''
    commits = []
    if commits_str == '[]':
        return []
    limpia = commits_str.strip('[]')
    limpia2 = limpia.split(';')
    for x in limpia2:
        partes = x.split('#')
        id_ = partes[0]
        mensaje = partes[1]
        fecha_hora = datetime.strptime(partes[2], "%Y-%m-%d %H:%M:%S")
        commit = Commit(id_, mensaje, fecha_hora)
        commits.append(commit)
    return commits 
        
def parsea_lenguajes(lenguajes: str) -> Set[str]:
    set_lenguajes = set()
    for x in lenguajes.split(','):
        set_lenguajes.add(x)
        
    return set_lenguajes

def total_commits_por_anyo(repositorios:List[Repositorio])->Dict[int, int]:
    '''
    Dada una lista de tuplas de tipo Repositorio, devuelve un diccionario en el que 
    las claves son los años, y los valores el número total de commits registrados en el año dado como clave para 
    los repositorios públicos. 
    '''
    res = defaultdict(int)
    for x in repositorios:
        if x.privado == False:
            for i in x.commits:
                res[i.fecha_hora.year] += 1
                
    return res

def n_mejores_repos_por_tasa_crecimiento(repositorios: List[Repositorio], n:Optional[int]=3)->List[Tuple[str,float]]:
    '''
    Dada  una  lista  de  tuplas  de  tipo  Repositorio  y  un  número 
    entero n (con valor por defecto igual a 3), devuelve una lista con los n nombres de los repositorios y sus tasas 
    de crecimiento más altas. 
    '''
    res = defaultdict(float)
    for x in repositorios:
        res[x.nombre] = calcular_tasa_crecimiento(x)
        
    res_ord = sorted(res.items(), key=lambda x:x[1], reverse=True)[:n]
        
    return res_ord

def calcular_tasa_crecimiento(repositorio: Repositorio) -> float:
    '''
    Dado un Repositorio, devuelve su tasa de crecimiento. La tasa de 
    crecimiento de  un repositorio  se  define  como la  ratio entre  el número de  commits y el número de 
    días transcurridos entre el primer y el último commit (los commits están ordenados en el archivo). Si 
    el repositorio tiene menos de 2 commits, o si tiene 2 o más commits pero no ha pasado al menos un 
    día entre el primero y el último, la tasa se considera cero.
    '''
    res = 0.0
    if len(repositorio.commits) < 2:
        return res
    else:
        dt2 = repositorio.commits[-1].fecha_hora
        dt1 = repositorio.commits[0].fecha_hora
        if (dt2-dt1).days == 0:
            return res
        else:
            res = len(repositorio.commits) / (dt2-dt1).days
            
    return res

def recomendar_lenguajes (repositorios:List[Repositorio], repositorio:Repositorio)->Set[str]:
    '''
    Dada una lista de tuplas de tipo Repositorio y un repositorio específico, devuelve 
    un  conjunto  con  los  lenguajes  de  programación  recomendados  para  dicho  repositorio.  Los  lenguajes 
    recomendados  son  aquellos  que  se  usan  en  repositorios  similares  al  repositorio  dado. Se  considera  que  un 
    repositorio es similar al dado si comparte al menos uno de los lenguajes de programación con el repositorio 
    dado. Por ejemplo, si queremos hacer una recomendación para el repositorio "LAB-FP", cuyo lenguaje es Java, 
    podemos  considerar  similar  el  repositorio  "LAB-Calificaciones",  que  utiliza  Java  y  Python,  ya  que  ambos
    comparten el lenguaje Java. En este caso, se recomendaría Python como nuevo lenguaje para el repositorio 
    "LAB-FP".
    '''
    res = set()
    lenguajes_repo = set()
    for x in repositorios:
        if x == repositorio:
            lenguajes_repo = x.lenguajes
            
        if lenguajes_repo.intersection(x.lenguajes):
            for i in x.lenguajes:
                res.add(i)
            
    return res

def media_minutos_entre_commits_por_usuario (repositorios:List[Repositorio],  
                         fecha_ini:Optional[date]=None, 
                         fecha_fin:Optional[date]=None)->Dict[str, float]:
    '''
    Dada una lista de tuplas de tipo Repositorio, una 
    fecha inicial y una fecha final (ambas opcionales con valor por defecto None), devuelve un diccionario en el 
    que las claves son los nombres de los propietarios de los repositorios, y los valores la media de minutos entre 
    los  commits  realizados  en  los  repositorios  de  cada  propietario  dentro  del  intervalo  de  fechas  dado  por 
    [fecha_ini, fecha_fin). Si fecha_ini es None no se restringe el inicio del intervalo, y si fecha_fin es None, no se 
    limita  el  final  del  intervalo.  Si  ambas  fechas  son  None,  se  consideran  todos  los  commits  sin  restricción 
    temporal.  
    Es  importante  tener  en  cuenta  que  un  mismo  propietario  puede  tener  varios  repositorios,  por  lo  que  los 
    cálculos  abarcarán  todos  los  commits  realizados  en  los  repositorios  de  ese  propietario  dentro  del  intervalo 
    especificado. 
    '''
    res = defaultdict(list)
    for x in repositorios:
        for i in x.commits:
            if (fecha_ini is None or fecha_ini <= i.fecha_hora.date()) and (fecha_fin is None or i.fecha_hora.date() < fecha_fin):
                res[x.propietario].append(i)
                   
    res2 = {}
    for propietario, commits in res.items():
        media = media_minutos_entre_commits(commits)
        if media is not None:
            res2[propietario] = media
                
    return res2

def media_minutos_entre_commits(lista_commits: List[Commit]) -> float:
    '''
    media_minutos_entre_commits: recibe una lista de tuplas de tipo Commit, y devuelve la media 
    de  minutos  entre  cada  dos  commits  consecutivos  en  el  tiempo,  por  lo  que,  previamente,
    deberá ordenar dichos commits . Si la lista tiene menos de dos elementos, la función devolverá None.
    '''
    if len(lista_commits) < 2:
        return None

    lista_commits_ord = sorted(lista_commits, key=lambda x:x.fecha_hora)
    total = 0.0
    count = 0
    dt1 = lista_commits_ord[0].fecha_hora
    
    for x in lista_commits_ord[1:]:
        dt2 = x.fecha_hora
        delta = (dt2 - dt1).total_seconds() / 60
        total += delta
        count += 1
        dt1 = dt2
            
    return total / count if count > 0 else None