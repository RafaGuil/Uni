from consumo_electrico import *

def test_lee_facturas(datos):
    print(len(datos))
    for x in datos[:2]:
        print(x)
    for x in datos[-2:]:
        print(x)    
        
def test_extrae_precio_por_mes(datos):
    res = extrae_precio_por_mes(datos, 'única')
    res2 = extrae_precio_por_mes(datos, 'tramos')
    print('Precio por mes (tarifa única)')
    for clave, valor in res.items():
        print(f'\t{clave}: {valor}')
        
    print('')
    print('Precio por mes (tarifa por tramos)')
    for clave2, valor2 in res2.items():
        print(f'\t{clave2}: {valor2}')
        
def test_busca_vivienda_mayor_consumo_acumulado(datos):
    res = busca_vivienda_mayor_consumo_acumulado(datos)
    print('Test busca_vivienda_mayor_consumo_acumulado')
    print(f'La vivienda con mayor consumo acumulado es la {res[0]} con un consumo total de {res[1]} kWh.')

def test_barrios_mayor_consumo_valle_medio(datos):
    res = barrios_mayor_consumo_valle_medio(datos, 3)
    print('Test barrios_mayor_consumo_valle_medio')
    print('Los tres barrios con mayor consumo medio en horario valle son:')
    for x in res:
        print(f'\t{x}')
        
def test_compara_importe_tipos_factura(datos):
    res = compara_importe_tipos_factura(datos, '005')
    print('Test compara_importe_tipos_factura')
    print(res)
    
def test_calcula_mes_incremento_maximo_consumo_acumulado(datos):
    res = calcula_mes_incremento_maximo_consumo_acumulado(datos, 'Casa')
    print(res)
    
def test_busca_cambios_beneficiosos(datos):
    res = busca_cambios_beneficiosos(datos)
    print(res)

if __name__ == '__main__':
    datos = lee_facturas('data/consumos_sevilla_2023.csv')
    # test_lee_facturas(datos)
    # test_extrae_precio_por_mes(datos)
    # test_busca_vivienda_mayor_consumo_acumulado(datos)
    # test_barrios_mayor_consumo_valle_medio(datos)
    # test_compara_importe_tipos_factura(datos)
    # test_busca_cambios_beneficiosos(datos)
    test_calcula_mes_incremento_maximo_consumo_acumulado(datos)