-- Eliminar datos previos
-- DELETE FROM Turno;
-- DELETE FROM Asignacion;
-- DELETE FROM Tarea;
-- DELETE FROM Pago;
-- DELETE FROM Persona;

SET @usuario_actual_id =1;

-- Insertar datos en la tabla Persona
INSERT INTO Persona (nombre, correo, departamento) VALUES
('Alvaro Landero Plaza', 'landero@alum.us.es', 'Control'),
('David López Mangas', 'davidlopezmangas@alum.us.es', 'Cost'),
('Rafael Guil Valero', 'rafaguilvalero@alum.us.es', 'Percepción'),
('Pablo Ruiz Vidal', 'ruizvidalpablo08@alum.us.es', 'Aerodinámica'),
('Alvaro Martinez Ocaña', 'alvaromartinezocaña@alum.us.es', 'Chasis');

-- Insertar datos en la tabla Rol
INSERT INTO Rol (personaId, rol) VALUES
(3, 'Team Leader'),
(4, 'Miembro'),
(5, 'Miembro'),
(6, 'Miembro'),
(7, 'Miembro');

-- Insertar datos en la tabla Pago
INSERT INTO Pago (personaId, cantidad, concepto, realizado) VALUES
(1, 150.00, 'Pago de la cuota de la competición', TRUE),
(3, 100.00, 'Pago de la cuota de la competición', TRUE),
(4, 100.00, 'Pago de la cuota de la competición', FALSE),
(5, 100.00, 'Pago de la cuota de la competición', TRUE);

-- Insertar datos en la tabla Asignacion
INSERT INTO Asignacion (personaId, fechaAsignacion, numeroHoras) VALUES
(3, '2023-10-01 09:00:00', 5),
(4, '2023-10-01 09:00:00', 3),
(3, '2023-10-02 10:00:00', 4),
(5, '2023-10-02 10:00:00', 2),
(3, '2023-10-03 11:00:00', 6),
(4, '2023-10-04 12:00:00', 5),
(3, '2023-10-05 13:00:00', 7),
(4, '2023-10-06 14:00:00', 3),
(3, '2023-10-07 15:00:00', 4),
(4, '2023-10-08 16:00:00', 6);

-- SET @usuario_actual_id = 2;
-- Insertar datos en la tabla Tarea
INSERT INTO Tarea (asignacionId, nombre, descripcion, estado, comentario, fechaEntrega) VALUES
(1, 'Desarrollar algoritmo de visión', 'Implementar algoritmo de detección de obstáculos', 'Pendiente', '', '2024-12-01 23:59:59'),
(1, 'Optimizar diseño del alerón trasero', 'Mejorar eficiencia aerodinámica del alerón', 'Empezado', 'Es urgente', '2024-12-02 23:59:59'),
(2, 'Crear campaña en redes sociales', 'Aumentar presencia en línea del equipo', 'Completado', 'Es urgente', '2024-12-03 23:59:59'),
(2, 'Diseñar nuevo chasis', 'Proponer estructura liviana y resistente', 'Con retraso', 'Es urgente', '2024-12-04 23:59:59'),
(1, 'Coordinar equipo de percepción', 'Supervisar integración de sensores', 'Pendiente', 'Es urgente', '2024-12-05 23:59:59'),
(2, 'Planificar evento promocional', 'Organizar feria para atraer patrocinadores', 'Empezado', 'Es urgente', '2024-12-06 23:59:59'),
(3, 'Crear sistema de monitoreo', 'Implementar software para seguimiento de tareas', 'Pendiente', '', '2024-12-07 23:59:59'),
(4, 'Desarrollar plan de negocio', 'Preparar documento para inversores', 'Con retraso', 'Es urgente', '2024-12-08 23:59:59'),
(5, 'Supervisar ensamblaje del chasis', 'Asegurar calidad en construcción', 'Pendiente', 'Es urgente', '2024-12-09 23:59:59'),
(5, 'Implementar control de vehículo', 'Desarrollar software para manejo autónomo', 'Empezado', 'Es urgente', '2024-12-10 23:59:59');

-- Insertar datos en la tabla Turno
INSERT INTO Turno (tareaId, fecha, ubicacion, duracion, comentario, asiste) VALUES
(2, '2023-11-02 13:00:00', 'Sala de Aerodinámica', 2, 'Revisión del alerón', FALSE),
(3, '2023-11-03 15:00:00', 'Oficina de Marketing', 2, 'Planificación de campaña', TRUE),
(4, '2023-11-04 10:00:00', 'Sala de Control', 3, 'Revisión de chasis', TRUE),
(5, '2023-11-05 16:00:00', 'Taller de Monitoreo', 3, 'Implementación de sistema', FALSE),
(8, '2023-11-06 11:00:00', 'Sala de Negocios', 4, 'Desarrollo del plan', TRUE);