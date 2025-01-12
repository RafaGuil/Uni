from collections import defaultdict
from datetime import date 
from typing import * 
from parsea import * 
import csv 

Reserva = NamedTuple("Reserva",  
                     [("nombre", str), 
                      ("dni", str), 
                      ("fecha_entrada", date), 
                      ("fecha_salida", date), 
                      ("tipo_habitacion", str), 
                      ("num_personas", int), 
                      ("precio_noche", float), 
                      ("servicios_adicionales", List[str]) 
                    ])

def lee_reservas(ruta_fichero: str) -> List[Reserva]:
    reservas = []
    with open (ruta_fichero, encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for nombre,dni,fecha_entrada,fecha_salida,tipo_habitacion,num_personas,precio_noche,servicios_adicionales in lector:
            nombre = str(nombre)
            dni = str(dni)
            fecha_entrada = parseaFecha(fecha_entrada)
            fecha_salida = parseaFecha(fecha_salida)
            tipo_habitacion = str(tipo_habitacion)
            num_personas = int(num_personas)
            precio_noche = float(precio_noche)
            servicios_adicionales = parseaServicios(servicios_adicionales)
            tupla = Reserva(nombre,dni,fecha_entrada,fecha_salida,tipo_habitacion,num_personas,precio_noche,servicios_adicionales)
            reservas.append(tupla)
            
    return reservas

def total_facturado(reservas: List[Reserva],  
             fecha_ini: Optional[date] = None,  
             fecha_fin: Optional[date] = None) -> float:
    res = 0

    for x in reservas:
        if (fecha_ini is None or parseaFecha(fecha_ini) <= x.fecha_entrada) and (fecha_fin is None or parseaFecha(fecha_fin) >= x.fecha_entrada):
            res += diasReserva(x.fecha_entrada, x.fecha_salida)*x.precio_noche
            
    return res

def reservas_mas_largas(reservas:List[Reserva],n:int = 3) -> List[Tuple[str, date]]:
    res = []
    for x in reservas:
        res.append((x.nombre, x.fecha_entrada, diasReserva(x.fecha_entrada, x.fecha_salida)))
        
        res_ord = sorted(res, key=lambda x:x[2], reverse=True)[:3]
        
    res2 = []
    for x, y, _ in res_ord:
        res2.append((x, y))
    
    return res2

def cliente_mayor_facturacion(reservas: List[Reserva],  
                        servicios: Optional[Set[str]] = None 
                        ) -> Tuple[str, float]:
    res = defaultdict(float)
    for x in reservas:
        if servicios in x.servicios_adicionales or servicios is None:
            res[x.dni] += diasReserva(x.fecha_entrada, x.fecha_salida)*x.precio_noche
            
    return max(res.items(), key=lambda x:x[1])

def servicios_estrella_por_mes(reservas: List[Reserva],  
                     tipos_habitacion: Optional[Set[str]] = None) -> Dict[str, str]:
    res = defaultdict(lambda: defaultdict(int))
    
    for x in reservas:
        if tipos_habitacion is None or x.tipo_habitacion in tipos_habitacion:
            for i in x.servicios_adicionales:
                res[meses(x.fecha_entrada)][i] += 1
                
    resultado = {}
    for mes, conteo_servicios in res.items():
        servicio_estrella = max(conteo_servicios.items(), key=lambda x: x[1])[0]
        resultado[mes] = servicio_estrella
    
    return resultado
            
def meses(fecha: datetime):
    mes = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    
    return mes[fecha.month - 1]

def media_dias_entre_reservas(reservas: List[Reserva]) -> float:
    res = 0
    reservas = sorted(reservas, key=lambda x:x.fecha_entrada)
    for x, y in zip(reservas[:-1], reservas[1:]):
        res += (y.fecha_entrada - x.fecha_entrada).days
        
    res = res/(len(reservas)-1)
        
    return res

def cliente_reservas_mas_seguidas(reservas: List[Reserva],  
   min_reservas: int 
   ) -> Tuple[str, float]:
    clientes = defaultdict(list)
    for x in reservas:
        clientes[x.dni].append(x)
        
    res2 = defaultdict(float)
    for x in reservas:
        for clave, valor in clientes.items():
            if min_reservas <= len(valor):
                res2[clave] = media_dias_entre_reservas(valor)
            
    return min(res2.items(), key=lambda x:x[1])
