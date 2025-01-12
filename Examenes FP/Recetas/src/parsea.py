from datetime import * 


def ParseaIngredientes(lista: str):
    res = []
    if len(lista) == 0:
        return None
    else:
        limpia = lista.split(',')
        for x in limpia:
            a = x.strip()
            res.append(a)
            
    return res

def ParseaFecha(fecha):
    return datetime.strptime(fecha, "%Y-%m-%d").date()