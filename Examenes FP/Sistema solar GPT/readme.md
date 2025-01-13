# Examen de Parsea
Este repositorio contiene la implementación de las soluciones propuestas para el examen de Fundamentos de Programación del curso 2024/25 (cuarta convocatoria).

Descripción
El proyecto se centra en la lectura y procesamiento de datos de sistemas solares observados. Utiliza estructuras de datos avanzadas, como NamedTuple, y promueve la modularidad y la reutilización de funciones a través de pruebas unitarias.

### Archivos incluidos:

- sistemas_solares.csv: Archivo de entrada con información sobre sistemas solares y sus planetas.

- sistemas_solares.py: Contiene las funciones principales para procesar los datos.

- sistemas_solares_test.py: Archivo para las pruebas unitarias de cada función implementada.

- README.md: Este archivo, que explica la estructura del proyecto y cómo ejecutarlo.

- parsea.py(Opcional): Archivo para añadir funciones auxiliares para parsear.

### Funciones principales:

- lee_sistemas_solares(csv_filename: str) -> List[SistemaSolar]:
Lee un archivo CSV y devuelve una lista de sistemas solares procesados como objetos de tipo SistemaSolar.

### Funciones auxiliares:

- parsea_planetas(planetas_str: str) -> List[Planeta]: 
Procesa cadenas de texto que describen planetas.

- parsea_distancia_luz(distancia_str: str) -> float: 
Convierte y redondea a 2 decimales la distancia de los sistemas a la Tierra.

Podrían hacer falta más funciones