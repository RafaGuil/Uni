[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/ewxA2p_5)
# Sistema de Gestión de Citas Médicas para Centros Sanitarios

## Miembros del grupo L1-AFM-2

1. Jiménez Lara, Alejandro.
1. Moreno Eugenio, Bella.
1. Armenteros Venegas, Juan Angel.
1. Marín Delgado, Juan.

## 1. Introducción al problema

- Descripción del problema para poner en contexto el proyecto, incluyendo información sobre los clientes y usuarios, la situación actual, problemas, expectativas, etc. Se valorará la presencia de información multimedia (fotos, gráficos, documentos escaneados, etc.).

Unos centros sanitarios desean automatizar el proceso de solicitar citas a un médico específico en un día y hora concreto. A su vez, se necesita un sistema que almacene los datos de cada paciente y trabajador del centro. Con esto se pretende gestionar a los empleados de una forma más sencilla y que los usuarios que requieran de los servicios de estos centros sanitarios puedan acceder a ellos desde cualquier lugar y en cualquier momento.

En la actualidad, el proceso de administración en algunos casos puede llegar a ser lento y poco eficaz. En contraste a ello, queremos facilitar y agilizar este proceso para la comodidad de nuestros respectivos usuarios.

## 2. Glosario de términos

- Términos específicos del dominio del problema, ordenados alfabéticamente. Se valorará la presencia de información multimedia.

**Agenda**
Estructura de datos organizada para representar el horario de trabajo de un médico, sus citas y la disponibilidad de tiempo para asignación de pacientes.

**Administración de citas:**
Sistema o proceso mediante el cual se gestionan las citas médicas, permitiendo la organización, programación y control de los turnos asignados a los pacientes en un centro de salud.

**Atención Primaria:**
Nivel de atención médica que se brinda en el primer contacto con el paciente, usualmente por un médico de cabecera o médico general. 

**Cita Médica:**
Encuentro programado entre un paciente y un profesional de la salud para la evaluación, diagnóstico y/o tratamiento de un problema de salud. 

**Diagnóstico:**
Proceso por el que se identifica una enfermadad, problema de salud o lesión.

**Especialista:**
Médico que ha recibido formación avanzada en una rama específica de la medicina, como cardiología, dermatología, neurología, etc. 
Los pacientes son derivados a especialistas cuando el problema de salud excede la capacidad del médico general para diagnosticar o tratar.

**Médico de Cabecera:**
Profesional de la salud que brinda atención primaria y tiene el primer contacto con el paciente. Es responsable de evaluar la situación general de salud del paciente y determinar si debe ser derivado a un especialista.

**Enfermero:**
Especialista en el tratamiento de situaciones críticas o urgentes, está capacitado para estabilizar al paciente y tomar decisiones rápidas en casos de emergencias médicas. No tiene una relación continua con los pacientes, sino que trata casos puntuales y graves.

**Paciente:**
Persona que recibe atención médica en un centro de salud. El paciente puede acceder a servicios de atención primaria, especializada o de urgencias, dependiendo de sus necesidades de salud.

**Personal Administrativo:**
Grupo de personas cuyos encargos recaen en tareas no clínicas, como la gestión de citas, organización de expedientes,  atención al cliente y gestiona la agenda, garantizando un flujo eficiente de pacientes.

**Tiempo de Espera:**
Tiempo que un paciente debe esperar desde que solicita una cita médica hasta que se realiza la consulta. 
La optimización del tiempo de espera es uno de los objetivos clave de un sistema de gestión de citas eficiente.

**Triage:**
Proceso de clasificación de pacientes en situaciones de urgencia, con el objetivo de priorizar la atención médica según la gravedad de su condición. El triage se divide en 5 niveles:
- Nivel 1: reanimación, atención inmediata.
- Nivel 2: emergencia, tiempo de espera para atención médica de 7 minutos.
- Nivel 3: urgente, tiempo de atención de 30 minutos.
- Nivel 4: menos urgente, tiempo de atención de 45 minutos.
- Nivel 5: no urgente, tiempo de atención de 60 minutos

**Urgencias:**
Servicio médico que brinda atención inmediata a pacientes con condiciones que requieren intervención rápida para estabilizar su salud o evitar un deterioro grave.
Las urgencias pueden abarcar desde lesiones físicas hasta problemas médicos agudos, y son gestionadas por los enfermeros en situaciones críticas.

**Ingreso:**
El proceso de admitir a un paciente en un hospital para recibir tratamiento y cuidados, ya sea de manera programada o de emergencia, y requiere la actualización de su expediente médico.

## 3. Visión general del sistema

Este sistema está diseñado para gestionar tanto la información relacionada con los pacientes como la organización del proceso de atención médica en un centro de salud. El sistema debe poder almacenar y gestionar los datos de los pacientes, registrar y organizar citas médicas, así como realizar la derivación de pacientes a especialistas cuando sea necesario.

El sistema contará con varios tipos de usuarios, entre los cuales destacamos el personal administrativo, los enfermeros, personal medico y los pacientes.
El personal administrativo se encargará de gestionar citas, gestionar agendas y actualizar los registros de los pacientes, mientras que los médicos tendrán acceso a herramientas más especializadas, como la revisión de historiales de citas.
El enfermero podrá usar el sistema para priorizar la atención de pacientes en situaciones críticas mediante un sistema de triage. También tendrán acceso al historial de citas para revisar el historial de citas del paciente y registrar el nivel de prioridad de los pacientes en función de su estado de gravedad.
El personal medico podrá consultar y actualizar el historial de citas de los pacientes, incluyendo el historial clínico. Crear y gestionar su propia agenda de citas dentro del sistema para garantizar la organización del tiempo disponible.
Los pacientes podrá solicitar, modificar y cancelar citas médicas.

### 3.1. Requisitos generales

#### **R.G.01. Gestión de citas**
El sistema debe guardar la gestión de citas, permitiendo a los pacientes solicitar, modificar y cancelar citas en línea, mientras que el personal administrativo puede gestionar estas citas a nivel del centro.

**Prueba de aceptación:**
- Un paciente solicita una cita desde la interfaz y recibe una notificación de confirmación. El sistema confirma la cita, envía la notificación al paciente y actualiza la agenda del médico.

- Un paciente intenta modificar una cita en un horario ya ocupado por otro paciente. El sistema rechaza la modificación e informa al paciente de que el horario seleccionado no está disponible.

#### **R.G.02. Registro de Usuarios**
El sistema debe permitir el acceso a diferentes tipos de usuarios (pacientes, médicos, personal administrativo, personal de urgencias) con un usuario, contraseña únicas y su rol definido para cada uno.

**Prueba de aceptación:**
- Un usuario administrativo se registra correctamente con DNI, nombre, apellidos y número de teléfono, y accede al sistema con su DNI y contraseña. El sistema permite el acceso y asigna los permisos correspondientes al rol administrativo.

- Un usuario intenta registrarse sin completar el campo de DNI. El sistema rechaza el registro e informa al usuario de que el DNI es un campo obligatorio.

#### **R.G.03. Gestión de citas de urgencias y triage**
El sistema debe permitir la gestión de urgencias, priorizando a los pacientes en base al nivel de gravedad mediante un sistema de triage.

**Prueba de aceptación:**
- El personal de urgencias registra a un paciente en el sistema, asigna una prioridad alta según el triage y el sistema actualiza el historial del paciente. El sistema almacena el nivel de prioridad y refleja la urgencia en el historial de citas del paciente.

- El personal de urgencias intenta asignar una prioridad de triage sin registrar primero al paciente. El sistema rechaza la asignación y alerta al usuario de que el registro del paciente es obligatorio para clasificar el nivel de prioridad.

#### **R.G.04. Disponibilidad continua**
El sistema debe estar disponible en cualquier momento (24/7) para garantizar que tanto los pacientes como el personal médico y administrativo puedan acceder y gestionar la información de manera oportuna.

**Prueba de aceptación:**
- Un paciente intenta acceder al sistema durante la madrugada y realiza una consulta de su próxima cita. El sistema permite el acceso y muestra la información de dicha cita sin interrupciones.

- Un usuario administrativo intenta acceder al sistema durante una interrupción inesperada del servicio. El sistema muestra un mensaje de error indicando que el servicio no está disponible temporalmente y proporciona opciones de contacto para asistencia.

### 3.2. Usuarios del sistema

**Pacientes**
- Solicitar, modificar y cancelar citas médicas.

**Personal Médico**
- Consultar el historial de citas de los pacientes.
- Generar diagnosticos.

**Administrativo**
- Consultar las citas de un paciente.

**Enfermero**
- Evaluar y clasificar a los pacientes según el sistema de triage.

## 4. Catálogo de requisitos

### 4.1. Requisitos funcionales

#### R.F.01. Solicitar citas online

Como paciente y como administrativo
quiero poder solicitar citas online
para no tener que acudir al centro a obtener una cita.

**Prueba de aceptación**
- Un paciente solicita una cita en línea y recibe una notificación de confirmación, además de un recordatorio 24 horas antes de la cita. El sistema confirma la cita, envía la notificación de confirmación y un recordatorio automático 24 horas antes de la cita.

- Un paciente intenta solicitar una cita en una franja horaria ya ocupada. El sistema rechaza la solicitud de cita e informa al paciente de que el horario seleccionado no está disponible.

#### R.F.02. Modifcar citas online

Como paciente y administrativo
quiero poder modificar citas online
para no tener que acudir al centro a modificar dicha cita.

**Prueba de aceptación**
- Un paciente modifica una cita existente a una nueva fecha y hora disponibles. El sistema guarda la modificación y envía una notificación de confirmación del cambio.

- Un paciente intenta modificar su cita a una hora que ya está ocupada. El sistema rechaza la modificación y alerta al paciente de que la hora seleccionada ya está ocupada.

#### R.F.03. Cancelar citas online

Como paciente y administrativo
quiero poder cancelar citas online
para no tener que acudir al centro a anular una cita.

**Prueba de aceptación**
- Un paciente cancela una cita en línea y recibe una confirmación de cancelación. El sistema cancela la cita y envía una notificación de confirmación al paciente.

- Un paciente intenta cancelar una cita que ya ha sido atendida o registrada como completada. El sistema rechaza la cancelación e informa al paciente de que la cita ya no puede cancelarse.

#### R.F.04. Urgencias

Como personal médico y enfermero
quiero poder gestionar urgencias
para que los pacientes puedan acceder fácilmente a estos servicios.

**Prueba de aceptación**
- El enfermero registra a un paciente y asigna un nivel de prioridad basado en el triage. El sistema registra el nivel de prioridad, asigna un identificador único al paciente y actualiza el historial de citas.

- El enfermero intenta asignar una prioridad sin haber completado el registro del paciente. El sistema rechaza el proceso de triage e informa al personal de que el registro del paciente es obligatorio.

#### **R.F.05. Consulta de citas**
Como enfermero, personal médico y administrativo
quiero poder consultar la información sobre una cita de un paciente
para poder estar informado spbre la situación del paciente.

**Prueba de aceptación:**
- Un enfermero consulta la informacion de las citas de un paciete y el sistema registra cuando ha sido consultada esa información.

- Un enfermero no puede consultar la información de una cita de una paciente porque el sistema rechaza la consulta debido a que el usuario consultado no tiene ninguna cita.

### **R.F.06. Creación de agenda**
Como personal médico
quiero crear mi agenda para un margen de tiempo en el que voy a tener una agenda que yo especifique
para que las citas que me soliciten estén en ese margen de tiempo

**Prueba de aceptación:**
- El médico crea su agenda con los horarios que el desee para atender sus citas durante el margen de tiempo que desee.

### **R.F.07. Registrar diagnóstico**
Como personal médico
quiero añadir un diagnóstico a una cita o a una cita de urgencia al finalizar
para que el paciente y los otros tipos de usuario pueda obtener informacion de la cita

**Prueba de aceptación:**
- El personal médico al finalizar la cita actualiza la cita para con el diagnóstico correspondiente al paciente.

- El sistema rechazará la actualización de la cita si el médico está intentando añadir una cita que no corresponde al paciente

### **R.F.08. Aceptación de Cita de Urgencia**
Como personal médico
quiero poder aceptar una cita de urgencia segun la prioridad de triage y el número de personas que haya en ese momento en espera
para que el paciente pase a consulta

**Prueba de aceptación:**
- El personal médico acepta una cita de urgencias según el nivel del triage y el tiempo que haya pasado desde la llegada del paciente, añadiendose una fecha de atención a la cita de urgencias, que puede ser anterior a la asignada según el triage dependeiend del flujo de pacientes en urgencias.

#### 4.1.1. Requisitos de información

**R.I.01. Consulta de Pacientes**

Como personal administrativo y personal médico 
quiero consultar la información básica de un paciente en el sistema 
para gestionar su historal de citas y permitir el seguimiento.

**Prueba de aceptación**
- Un miembro del personal administrativo con credenciales válidas intenta acceder a la información básica de un paciente registrado en el sistema. El sistema permite el acceso a la información del paciente, incluyendo nombre, apellidos y fecha de nacimiento, y permite gestionar el historial de citas.

- Un usuario sin autorización intenta acceder a la información de un paciente en el sistema. El sistema rechaza el acceso e informa al usuario de que no tiene permisos suficientes para ver la información del paciente.

**R.I.02. Consulta de la Agenda del Personal**

Como personal administrativo y personal médico 
quiero poder revisar la agenda y horarios 
para organizar de manera eficaz los recursos del centro y mejorar la calidad del servicio.

**Prueba de aceptación**
- Un médico inicia sesión en el sistema y consulta su horario laboral y recibe una notificación de un cambio en su agenda. El sistema muestra correctamente el horario del médico y envía la notificación del cambio. 

- Un médico intenta acceder al horario de otro profesional sin permisos suficientes. El sistema bloquea el acceso y notifica al usuario de que no tiene permisos para ver el horario de otros empleados.

**R.I.03. Revisión del Proceso de Triage en Urgencias**

Como enfermero 
quiero almacenar los datos de triaje 
para clasificar a los pacientes según la su situación, para priorizar la atención de los pacientes más graves.

**Prueba de aceptación**
- Un miembro del enfermero realiza el triaje de un paciente y clasifica su nivel de prioridad en el sistema. El sistema almacena y muestra correctamente el nivel de prioridad del paciente, permitiendo un seguimiento adecuado para priorizar su atención.

- Un miembro del enfermero intenta registrar un nivel de prioridad sin especificar los datos de ingreso del paciente. El sistema rechaza el proceso de triaje e indica que los datos de ingreso son obligatorios para la clasificación.

#### 4.1.2. Reglas de negocio 

##### R.N.01. Registro de fecha de nacimiento

- La fecha de nacimiento no puede ser posterior a la fecha actual.

**Pruebas de aceptación**

- El paciente intenta registrarse con todos los campos obligatorios completos y una fecha de nacimiento válida. El sistema registra exitosamente al paciente y permite el acceso a los servicios de citas médicas.
- El paciente intenta registrarse con una fecha de nacimiento posterior a la fecha actual. El sistema rechaza el registro del paciente, indicando que la fecha de nacimiento no puede ser posterior a la fecha actual.

##### R.N.02. Registro de contraseña

- La contraseña debe contener al menos un carácter especial.

**Pruebas de aceptación**

- El paciente intenta registrarse con todos los campos obligatorios completos y una contraseña válida. El sistema registra exitosamente al paciente y permite el acceso a los servicios de citas médicas.
- El paciente intenta registrarse con una contraseña sin ningún carácter especial. El sistema rechaza el registro del paciente, indicando que la contraseña necesita al menos un carácter especial para poder ser válida.


##### R.N.03. Registro de DNI

- El DNI debe estar formado por 8 números y 1 letra.

**Pruebas de aceptación**

- El paciente intenta registrarse con todos los campos obligatorios completos y un DNI válido. El sistema registra exitosamente al paciente y permite el acceso a los servicios de citas médicas.
- El paciente intenta registrarse con un DNI sin ninguna letra. El sistema rechaza el registro del paciente, indicando que el DNI necesita una letra para poder ser válido.

##### R.N.04. Registro Usuario

- Si el tipo de usuario es medico la especialidad no puede ser una cadena vacia o un valor NULL.

**Pruebas de aceptación**

- Un usuario inserta al registrare el tipo medico y en la especialidad le da un valor null. El sistema rechaza el registro del usuario.
- Un usuario inserta al registrare el tipo medico y en la especialidad le da una cadena vacia. El sistema rechaza el registro del usuario.

##### R.N.05. Intervalo de Triage

- El triage debe estar comprendido entre 1 y 5.

**Pruebas de aceptación**

- El enfermero intenta registrar un triage con un valor entre 1 y 5. El sistema lo acepta y registra exitosamente.
- El enfermero intenta registrar un triage con un valor menor que 1 o mayor que 5. El sistema rechaza el registro, indicando que el triage debe estar entre 1 y 5.

##### R.N.06. Fecha y hora de llegada en las Citas de Urgencias

- La fecha y hora de llegada no puede ser posterior a la fecha y hora actual.

**Pruebas de aceptación**

- El enfermero intenta registrar una cita de urgencia con una fecha y hora de llegada válida. El sistema registra exitosamente la cita.
- El enfermero intenta registrar una cita de urgencia con una fecha y hora de llegada posterior a la fecha y hora actual. El sistema rechaza el registro, indicando que la fecha y hora de llegada no pueden ser posteriores a la fecha y hora actual.

##### R.N.07. Fecha y hora de atención en las Citas de Urgencias

- La fecha y hora de atención no puede ser posterior a la fecha y hora de llegada.

**Pruebas de aceptación**

- El enfermero intenta registrar una cita de urgencia con una fecha y hora de atención válida. El sistema registra exitosamente la cita.
- El enfermero intenta registrar una cita de urgencia con una fecha y hora de atención posterior a la fecha y hora de llegada. El sistema rechaza el registro, indicando que la fecha y hora de atención no pueden ser posteriores a la fecha y hora de llegada.

##### R.N.08. Fechas de inicio y fin en Citas y Agenda

- Las fechas de fin deben ser posteriores a las fechas de inicios.
- Las fechas de inicio deben ser posteriores a la fecha actual.

**Pruebas de aceptación**

- El paciente intenta registrar una cita con una fecha de inicio anterior a la fecha de fin, ambas válidas. El sistema registra exitosamente la cita.
- El paciente intenta registrar una cita con una fecha de fin anterior a la fecha de inicio. El sistema rechaza el registro, indicando que la fecha de fin debe ser posterior a la fecha de inicio.
- El paciente intenta registrar una cita con una fecha de inicio anterior a la fecha actual. El sistema rechaza el registro, indicando que la fecha de inicio debe ser posterior a la fecha actual.

##### R.N.09. Hora inicio y fin de la Agenda

- La hora de fin debe ser posterior a la hora de inicio. 
- La hora de inicio debe ser posterior a la hora actual.

**Pruebas de aceptación**

- El administrador intenta registrar una agenda con una hora de inicio posterior a la hora de fin. El sistema registra exitosamente la agenda.
- El administrador intenta registrar una agenda con una hora de fin anterior a la hora de inicio. El sistema rechaza el registro, indicando que la hora de fin debe ser posterior a la hora de inicio.
- El administrador intenta registrar una agenda con una hora de inicio anterior a la hora actual. El sistema rechaza el registro, indicando que la hora de inicio debe ser posterior a la hora actual.

### 4.2. Mapa de historias de usuario (opcional)
![Mapa de historias de usuario](./images/mapaHistoralDeUsuario.jpg)

### 4.3. Requisitos no funcionales (opcional)

**R.N.F. 01. Accesibilidad**

Como cualquier usuario de la página
quiero que la página sea intuitiva y accesible, además de ser multiplataforma
para que sea sencilla de usar y se pueda utilizar en cualquier plataforma.

**R.N.F. 02. Disponibilidad**

Como cualquier usuario de la página
quiero poder acceder a la página en cualquier momento
para que todas las funciones estén disponibles cuando se desee.

-- fin entregable 1 --

## 5. Modelo conceptual

### 5.1. Diagramas de clases UML

![Diagrama de clases UML](./images/diagramaUML.svg)

### 5.2. Escenarios de prueba
![EscenarioDePrueba](./images/EscenarioPrueba.svg)

En el escenario de prueba podemos observar como el usuario se registra con su nombre, apellidos, introduce una contraseña que cumpla con la regla de negocio 1, su fecha de nacimiento, su teléfono y su DNI. Este usuario puede ser de personal médico, paciente y administrativo. El personal médico es de un tipo, urgencias, cabecera, cirujano ... El triaje es evaluado por el personal médico que sea de urgencias,el cuál evalúa la gravedad del paciente y la cuál es asignada a la cita de urgencias en las que asignamos un médico también de urgencias, la cita de urgencias tiene un motivo, una fecha y hora de llega y la fecha y hora de atención de la cita.
Un paciente puede solicitar y cancelar citas, las cuales tienen un id, una fecha y hora a la que elige la cita, fecha y hora de solicitud, el motivo y el estado de la cita. A la cita, se le asigna un lugar del hospital al que acudir para que el paciente sea atendido. Los administrativos pueden solicitar y consultar citas en nombre del paciente y pueden gestionar y consultar la agenda del personal médico, en el cual los médico pueden consultar su fecha de inicio y fecha fin del turno.

## 6. Matrices de trazabilidad

- Matriz de trazabilidad entre los elementos del modelo conceptual y los requisitos.

|       |   Cita   | Paciente | Administrativo | Cita Urgencia | PersonalMédico | Agenda | Registro | Enfermero |
|:------|:---------|:---------|:---------------|:--------------|:---------------|:-------|:---------|:----------|
| RI-1  |    X     |    X     |       X        |               |                |        |          |     X     |
| RI-2  |          |          |                |               |       X        |   X    |          |           |
| RI-3  |          |    X     |                |       X       |                |        |     X    |     X     |
| RF-1  |    X     |    X     |       X        |               |                |        |          |           |
| RF-2  |    X     |    X     |       X        |               |                |        |          |           |
| RF-3  |    X     |    X     |       X        |               |                |        |          |           |
| RF-4  |          |    X     |                |       X       |       X        |        |          |     X     |
| RF-5  |    X     |          |       X        |       X       |       X        |        |     X    |     X     |
| RF-6  |          |          |                |               |       X        |   X    |          |           |
| RF-7  |    X     |          |       X        |               |       X        |        |          |           |
| RF-8  |          |    X     |                |       X       |       X        |        |          |           |
| RN-1  |          |    X     |       X        |               |       X        |        |          |     X     |
| RN-2  |          |    X     |       X        |               |       X        |        |          |     X     |
| RN-3  |          |    X     |       X        |               |       X        |        |          |     X     |
| RN-4  |          |          |                |               |       X        |        |          |           |
| RN-5  |          |          |                |       X       |                |        |          |           |
| RN-6  |          |          |                |       X       |                |        |          |           |
| RN-7  |          |          |                |       X       |                |        |          |           |
| RN-8  |    X     |          |                |               |                |   X    |          |           |
| RN-9  |          |          |                |               |                |   X    |          |           |
| RNF-1 |          |    X     |       X        |               |       X        |        |          |     X     |
| RNF-2 |    X     |    X     |       X        |       X       |       X        |   X    |     X    |     X     |

-- fin entregable 2 --

## 7. Modelo relacional en 3FN

- Relaciones obtenidas al aplicar la transformación del modelo conceptual.
![Modelo Relacional](./images/Relacional.svg)


### 7.1.  Justificación de la estrategia de transformación de jerarquías

Tenemos una relación para toda la jerarquía 
Para la transformación de la generalización hemos realizado una relación para toda la jerarquía en la que usuario, es la tabla en la que hemos añadido todos los atributos.
Para las asociaciones 1:* hemos representado la clave ajena en la relación de la entidad del rol *
Para las asociaciones de consultas *:* hemos creado una tabla auxiliar llamada registroAcceso en la que representamos las claves ajenas de las dos relaciones de la entidad.

-- fin entregable 3 --

## Referencias
- Referencia para la información del triage
https://www.lavozdegalicia.es/noticia/lavozdelasalud/botiquin/2022/11/21/van-tardar-atenderme-urgencias-guia-base-problema-tengas/00031669043862671939813.html

- Referencia de páginas web de citas médicas
https://www.asisa.es/seguros-de-salud

https://www.sspa.juntadeandalucia.es/servicioandaluzdesalud/clicsalud/pages/portada.jsf?caducada=1
