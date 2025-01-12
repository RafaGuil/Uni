from reservas import *

def test_lee_reservas(datos):
    print('Test lee_reservas')
    print(f'Total reservas: {len(datos)}')
    for x in datos[:3]:
        print(f'\t{x}\n')
        
def test_total_facturado(datos):
    print('Test total_facturado')
    res = total_facturado(datos, None, None)
    print(f'En todo el periodo de datos: {res}')
    res2 = total_facturado(datos, '2022-02-01', '2022-02-28')
    print(f'En todo el periodo de datos: {res2}')
    
def test_reservas_mas_largas(datos):
    print('Test reservas_mas_largas')
    res = reservas_mas_largas(datos, 3)
    print(res)
    
def test_cliente_mayor_facturacion(datos):
    print('Test cliente_mayor_facturacion')
    res = cliente_mayor_facturacion(datos, None)
    print(f'Sin filtrar por servicios: {res}')
    res2 = cliente_mayor_facturacion(datos, 'Parking')
    print(f'Con Parking: {res2}')
    # res3 = cliente_mayor_facturacion(datos, ('Parking', 'Spa'))
    # print(f'Con Parking: {res3}')
    
def test_servicios_estrella_por_mes(datos):
    print('Test servicios_estrella_por_mes')
    print('Todos los tipos de habitación:')
    res = servicios_estrella_por_mes(datos, None)
    for x in res.items():
        print(x)
    
    print('Habitación familiar o deluxe:')
    res2= servicios_estrella_por_mes(datos, ('Familiar', 'Deluxe'))
    for x in res2.items():
        print(x)
        
def test_media_dias_entre_reservas(datos):
    res = media_dias_entre_reservas(datos)
    print(res)
    
def test_cliente_reservas_mas_seguidas(datos):
    res = cliente_reservas_mas_seguidas(datos, 5)
    print(res)
    
if __name__ == '__main__':
    datos = lee_reservas('data/data.csv')
    # test_lee_reservas(datos)
    # test_total_facturado(datos)
    # test_reservas_mas_largas(datos)
    # test_cliente_mayor_facturacion(datos)
    # test_servicios_estrella_por_mes(datos)
    # test_media_dias_entre_reservas(datos)
    test_cliente_reservas_mas_seguidas(datos)