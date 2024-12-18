-- Llamada para crear un usuario
--Registrar Paciente
CALL registro('123456789', '12367898a', 'Antonio', 'García', 'Marqués', 'Anton$oChulo', '2003-04-16', '', 'Paciente');
--- Registrar Médico
CALL registro('698477122', '59664301F', 'Juan', 'Pérez', 'López', 'soyUnM%dico', '1978-09-12', 'Cardiólogo', 'Médico');
--- Registrar enfermero
CALL registro('601365524', '49256431P', 'Alejandro', 'Gutiérrez', 'Moreno', 'soyUnEnf$ermero', '1985-12-23', '', 'Enfermero');
--- Registrar administrativo
CALL registro('676315859', '52322574I', 'Lucía', 'Martínez', 'Gómez', 'Lucia345_', '1970-04-05', '', 'Administrativo');
--- Registro que salta error por la longitud del número de teléfono
CALL registro('6013655245', '49256431U', 'María', 'Fernández', 'Ruiz', 'Maria1234.)', '1995-03-11', 'Obstreticia', 'Médico');
--- Registro que salta error por que le falta la letra al DNI
CALL registro('601365524', '49256431', 'María', 'Fernández', 'Ruiz', 'Maria1234.)', '1995-03-11', 'Obstreticia', 'Médico');
--- Registro que salta error porque la contraseña no contiene ningun carácter especial
CALL registro('601365524', '49256431U', 'María', 'Fernández', 'Ruiz', 'Maria1234', '1995-03-11', 'Obstreticia', 'Médico');
--- Registro que salta error porque pone que la fecha de nacimiento es posterior a la actual
CALL registro('601365524', '49256431U', 'María', 'Fernández', 'Ruiz', 'Maria1234.)', '2026-03-11', 'Obstreticia', 'Médico');
--- Registro que salta error al no poner una especialidad y ser médico
CALL registro('601365524', '49256431U', 'María', 'Fernández', 'Ruiz', 'Maria1234.)', '1995-03-11', '', 'Médico');

--- Llamada para crear una agenda
--- Crear Agenda
CALL crearAgenda(1, '2025-01-01',  '2025-01-31', 'Martes', '10:00:00', '14:00:00', '00:20:00');
--- Agenda que salta error porque la fecha de inicio es anterior o igual a la actual
CALL crearAgenda(1, '2024-01-01', '2024-01-31', 'Martes', '10:00:00', '14:00:00', '00:20:00');

-- Llamada para crear un lugar
CALL crearLugar('Edificio Cardiología', '1', '38');

-- Llamada para solictar una cita
-- Solicitar Cita
CALL solicitaCita(2, 1, 1, 1, '2024-12-17 10:35:00', 'Dolor fuerte en el corazón');

-- Salta error al solicitar una cita porque la hora de la cita no esta en la agenda del médico
CALL solicitaCita(2, 1, 1, 1, '2024-12-17 17:55:00', 'Dolor fuerte en el corazón');

-- Llamada para modificar una cita
-- Modificar una cita
CALL modificarCita(1, '2024-12-16 12:30:00');

-- Salta error al modificar una cita porque ya existe una cita en ese tramo de hora
CALL modificarCita(1, '2024-12-16 10:40:00');

-- Llamada para crear una cita de urgencias
-- Crear cita de urgencias
CALL crearCitaUrgencias(1, 3, 'Me duele mucho la barriga', 5);

-- Salta error al crear la cita de urgencias porque el valor del triage no es correcto
CALL crearCitaUrgencias(1, 3, 'Me duele mucho la barriga', 7);

-- Salta error al crear la cita de urgencias porque no existe el enfermero
CALL crearCitaUrgencias(1, 6, 'Me duele mucho la barriga', 7);

-- Llamada para que el médico atienda la cita de urgencia
-- Actualiza la cita de urgencia con el medico y la fecha de atención
CALL aceptarCitaUrgencias(1, 2, NOW());

-- Llamada para insertar el diagnóstico de una cita
-- Actualiza la cita para añadiendo el diagnóstico
CALL insertarDiagnostico(1, 'El problema puede ser causado por colesterol alto, se le recomienda hacerse una analítica de sangre');

-- Salta error porque la cita no existe
CALL insertarDiagnostico(4, 'El problema puede ser causado por colesterol alto, se le recomienda hacerse una analítica de sangre');

-- Lamada para insertar diagnóstico en una cita de urgencias
-- Actualiza la cita de urgencias añadiendo el diagnóstico
CALL insertarDiagnosticoCitaUrgencias(1, 'Reposo durante una semana y un ibuprofeno');

-- Salta error porque la cita de urgencias no existe
CALL insertarDiagnosticoCitaUrgencias(6, 'Reposo durante una semana y un ibuprofeno');

-- Llamada para la consulta de una cita 
-- Conuslta de citas
CALL registrarAccesoConsultaCita(2, NULL, NULL, 1, NULL);
CALL registrarAccesoConsultaCita(NULL, 3, NULL, NULL, 2);
CALL registrarAccesoConsultaCita(NULL, NULL, 4, 1, NULL);

-- Llamada para cancelar cita 
-- Cancelar una cita
CALL eliminarCita(1);

-- Salta error si la cita que se intenta eliminar no existe
CALL eliminarCita(18);