-- Prueba 1: Insertar Persona como Team Leader (debería ser exitoso)
SET @usuario_actual_id = 1;
INSERT INTO Persona (nombre, correo, departamento) VALUES
('Juan Pérez', 'juanperez@alum.us.es', 'Control');
INSERT INTO Rol (personaId, rol) VALUES
(LAST_INSERT_ID(), 'Team Leader');

-- Prueba 2: Insertar Persona como Miembro (debería fallar)
-- SET @usuario_actual_id = 6;
-- INSERT INTO Persona (nombre, correo, departamento) VALUES
-- ('María López', 'marialopez@alum.us.es', 'Marketing');
-- INSERT INTO Rol (personaId, rol) VALUES
-- (LAST_INSERT_ID(), 'Miembro');

-- Prueba 3: Insertar Tarea como Team Leader (debería ser exitoso)
-- SET @usuario_actual_id = 1;
-- INSERT INTO Tarea (asignacionId, nombre, descripcion, estado, comentario, fechaEntrega) VALUES
-- (1, 'Revisar sistema de control', 'Verificar el funcionamiento del sistema de control', 'Pendiente', '', '2024-12-15 12:00:00');

-- Prueba 4: Insertar Tarea como Miembro (debería fallar)
-- SET @usuario_actual_id = 6;
-- INSERT INTO Tarea (asignacionId, nombre, descripcion, estado, comentario, fechaEntrega) VALUES
-- (2, 'Actualizar software de monitoreo', 'Realizar actualizaciones necesarias', 'Empezado', '', '2024-12-20 18:00:00');

-- Prueba 5: Actualizar Tarea como Team Leader (debería ser exitoso)
-- SET @usuario_actual_id = 1;
-- UPDATE Tarea SET estado = 'Completado' WHERE id = 4;

-- Prueba 6: Actualizar Tarea como Team Leader (debería ser exitoso)
-- SET @usuario_actual_id = 6;
-- UPDATE Tarea SET estado = 'Completado' WHERE id = 5;

-- Prueba 7: Actualizar Tarea como Miembro (modificar campo permitido, debería ser exitoso)
-- SET @usuario_actual_id = 6;
-- UPDATE Tarea SET comentario = 'Actualización realizada correctamente.' WHERE id = 6;

-- Prueba 8: Actualizar Tarea como Miembro (modificar campo no permitido, debería fallar)
-- SET @usuario_actual_id = 6;
-- UPDATE Tarea SET nombre = 'Nombre Modificado' WHERE id = 2;

-- Prueba 9: Eliminar Tarea como Team Leader (debería ser exitoso)
-- SET @usuario_actual_id = 1;
-- DELETE FROM Tarea WHERE id = 10;

-- Prueba 10: Eliminar Tarea como Miembro (debería fallar)
-- SET @usuario_actual_id = 6;
-- DELETE FROM Tarea WHERE id = 2;

-- Prueba 11: Añadir 2 Team Leaders en el mismo departamento (debería fallar)
-- SET @usuario_actual_id = 1;
-- INSERT INTO Persona (nombre, correo, departamento) VALUES
-- ('Ana Novas', 'ananovas@alum.us.es', 'Control');
-- INSERT INTO Rol (personaId, rol) VALUES
-- (LAST_INSERT_ID(), 'Team Leader');

-- Prueba 12: Añadir a un Team Leader de otro departamento como Team Leader (debería ser exitoso)
-- SET @usuario_actual_id = 1;
-- INSERT INTO Persona (nombre, correo, departamento) VALUES
-- ('Antonio Mayo', 'antoniomayo@alum.us.es', 'Marketing');
-- INSERT INTO Rol (personaId, rol) VALUES
-- (LAST_INSERT_ID(), 'Team Leader');

-- Prueba 13: Actualizar estado de las tareas (debería ser exitoso)
-- UPDATE Tarea SET estado = estado;

-- Prueba 14: Correo electrónico válido (debería fallar)
-- SET @usuario_actual_id = 1;
-- INSERT INTO Persona (nombre, correo, departamento) VALUES
-- ('Rafael Jiménez Llamas', 'rafa@us.es', 'Dinámica');
-- INSERT INTO Rol (personaId, rol) VALUES
-- (LAST_INSERT_ID(), 'Team Leader');

-- Prueba 15: Correo electrónico válido (debería ser exitoso)
-- SET @usuario_actual_id = 1;
-- INSERT INTO Persona (nombre, correo, departamento) VALUES
-- ('Rafael Jiménez Llamas', 'rafa@alum.us.es', 'Dinámica');
-- INSERT INTO Rol (personaId, rol) VALUES
-- (LAST_INSERT_ID(), 'Team Leader');