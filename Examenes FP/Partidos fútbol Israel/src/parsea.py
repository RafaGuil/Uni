def parsea_partidos(partido: str):
    local = partido.split(' v ')[0]
    visitante = partido.split(' v ')[1]
    
    return local.strip(), visitante.strip()

def parsea_goles(goles: str):
    local = goles.split('-')[0]
    visitante = goles.split('-')[1]
    
    return int(local), int(visitante)