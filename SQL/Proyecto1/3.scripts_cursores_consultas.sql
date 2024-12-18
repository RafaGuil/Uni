# Consultas generales

# Consultar todas las citas atendidas por un médico específico
SELECT *
FROM citas
WHERE medicoId = 1;

# Consultar todas las citas atendidas por un enfermero específico
SELECT *
FROM citaUrgencias
WHERE enfermeroId = 1;

# Consultar las citas de urgencias que un médico ha atendido
SELECT *
FROM citaUrgencias
WHERE medicoId = 1;

# Consultar la agenda de un médico para un día específico
SELECT *
FROM agenda
WHERE medicoId = 1 AND DATE(fechaInicio) = '2024-12-15';

# Consultar todas las citas urgentes que se han realizado y su triage
SELECT citaUrgenciasId, fechahoraLlegada, triage, diagnostico
FROM citaUrgencias
WHERE fechaHoraAtencion IS NOT NULL;

# Consultar las citas programadas para un paciente específico
SELECT *
FROM citas
WHERE pacienteId = 1;

# Consultar las citas urgentes de un paciente específico
SELECT *
FROM citaUrgencias
WHERE pacienteId = 1;

# Consultar la cantidad de citas de urgencias atendidas por cada médico
SELECT nombre, apellido1, apellido2, COUNT(citaUrgenciasId) AS cantidadCitas
FROM usuarios
JOIN citaUrgencias ON usuarios.usuarioId = citaUrgencias.medicoId
WHERE citaUrgencias.fechaHoraAtencion IS NOT NULL
GROUP BY usuarios.usuarioId;

# Consultar citas programadas para un día específico y ver quién las atenderá
SELECT fechaHoraCita, nombre AS medicoNombre, apellido1 AS medicoApellido
FROM citas
JOIN usuarios ON citas.medicoId = usuarios.usuarioId
WHERE DATE(fechaHoraCita) = '2024-12-15';

# Consultar si un médico tiene citas en una hora específica
SELECT *
FROM citas
WHERE medicoId = 1 AND '2024-12-15 10:00:00' BETWEEN fechaHoraCita AND fechaHoraFinCita;

# Consultar citas atendidas por un enfermero en una fecha específica
SELECT *
FROM citaUrgencias
WHERE enfermeroId = 1 AND DATE(fechahoraLlegada) = '2024-12-15';

# Consultar todos los usuarios de tipo 'Paciente'
SELECT *
FROM usuarios
WHERE tipoUsuario = 'Paciente';

# Consultar todos los lugares disponibles
SELECT *
FROM lugar;

# Consultar la agenda completa de un médico
SELECT *
FROM agenda
WHERE medicoId = 1;

# Consultar citas con diagnóstico pendiente para un médico específico
SELECT *
FROM citas
WHERE medicoId = 1 AND diagnostico IS NULL;

# Consultar urgencias atendidas con triage de nivel 3 o superior
SELECT *
FROM citaUrgencias
WHERE triage >= 3;

# Consultar accesos registrados por un administrativo específico
SELECT *
FROM registroAcceso
WHERE administrativoId = 1;

# Consultar citas realizadas en un lugar específico
SELECT *
FROM citas
WHERE lugarId = 1;

# Consultar pacientes que tienen más de una cita programada
SELECT pacienteId, COUNT(*) AS cantidadCitas
FROM citas
GROUP BY pacienteId
HAVING COUNT(*) > 1;

# Consultar los detalles de las citas programadas junto con el lugar y el médico
SELECT citas.citaId, citas.fechaHoraCita, lugar.edificio, lugar.planta, lugar.puerta, usuarios.nombre AS medicoNombre, usuarios.apellido1 AS medicoApellido
FROM citas
JOIN lugar ON citas.lugarId = lugar.lugarId
JOIN usuarios ON citas.medicoId = usuarios.usuarioId;

# Consultar las urgencias con triage mayor a 2 y el médico asignado
SELECT citaUrgencias.citaUrgenciasId, citaUrgencias.fechahoraLlegada, citaUrgencias.triage, usuarios.nombre AS medicoNombre, usuarios.apellido1 AS medicoApellido
FROM citaUrgencias
JOIN usuarios ON citaUrgencias.medicoId = usuarios.usuarioId
WHERE citaUrgencias.triage > 2;

# Consultar la agenda y los días disponibles de cada médico
SELECT agenda.medicoId, usuarios.nombre AS medicoNombre, usuarios.apellido1 AS medicoApellido, agenda.diaSemana, agenda.horaInicio, agenda.horaFin
FROM agenda
JOIN usuarios ON agenda.medicoId = usuarios.usuarioId;

# Consultar el número de citas urgentes atendidas en cada lugar
SELECT lugar.edificio, lugar.planta, lugar.puerta, COUNT(citaUrgencias.citaUrgenciasId) AS cantidadCitasUrgentes
FROM citaUrgencias
JOIN citas ON citaUrgencias.citaUrgenciasId = citas.citaId
JOIN lugar ON citas.lugarId = lugar.lugarId
GROUP BY lugar.lugarId;

# Cantidad de citas de urgencias atendidas por un médico por mes
SELECT MONTH(citaUrgencias.fechaHoraAtencion) AS mes, YEAR(citaUrgencias.fechaHoraAtencion) AS año, usuarios.nombre AS medicoNombre,usuarios.apellido1 AS medicoApellido, COUNT(citaUrgencias.citaUrgenciasId) AS cantidadCitasUrgencias
FROM citaUrgencias
JOIN usuarios ON citaUrgencias.medicoId = usuarios.usuarioId
WHERE citaUrgencias.fechaHoraAtencion IS NOT NULL
GROUP BY usuarios.usuarioId, YEAR(citaUrgencias.fechaHoraAtencion), MONTH(citaUrgencias.fechaHoraAtencion)
ORDER BY año, mes, usuarios.usuarioId;

#Cantidad de citas de urgencias atendidas por un enfermero por mes
SELECT MONTH(citaUrgencias.fechaHoraAtencion) AS mes,YEAR(citaUrgencias.fechaHoraAtencion) AS año,usuarios.nombre AS enfermeroNombre,usuarios.apellido1 AS enfermeroApellido,COUNT(citaUrgencias.citaUrgenciasId) AS cantidadCitasUrgencias
FROM citaUrgencias
JOIN usuarios ON citaUrgencias.enfermeroId = usuarios.usuarioId
WHERE citaUrgencias.fechaHoraAtencion IS NOT NULL
GROUP BY usuarios.usuarioId, YEAR(citaUrgencias.fechaHoraAtencion), MONTH(citaUrgencias.fechaHoraAtencion)
ORDER BY año, mes, usuarios.usuarioId;
