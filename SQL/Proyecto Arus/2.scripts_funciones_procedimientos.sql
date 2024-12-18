-- R.F.01. Agregar tareas
DELIMITER //

DROP PROCEDURE IF EXISTS pInsertTarea;
CREATE PROCEDURE
    pInsertTarea(
        pAsignacionId INT,
        pNombre VARCHAR(255),
        pDescripcion VARCHAR(255),
        pEstado VARCHAR(20),
        pComentario VARCHAR(255),
        pFechaEntrega DATETIME
    )
BEGIN
    -- Validaciones
    IF pNombre IS NULL OR TRIM(pNombre) = '' THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'ERROR: La tarea tiene que tener un nombre.';
    END IF;

    IF NOT EXISTS (SELECT * FROM Asignacion WHERE id = pAsignacionId) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'ERROR: No se ha encontrado la asignación.';
    END IF;

    INSERT INTO Tarea(asignacionId, nombre, descripcion, estado, comentario, fechaEntrega)
    VALUES(pAsignacionId, pNombre, pDescripcion, pEstado, pComentario, pFechaEntrega);
END //

-- R.F.02. Eliminar tareas
DROP PROCEDURE IF EXISTS pDeleteTarea;
CREATE PROCEDURE
    pDeleteTarea(pId INT)
BEGIN
    IF NOT EXISTS (SELECT * FROM Tarea WHERE id = pId) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'ERROR: No se ha encontrado la tarea.';
    END IF;

    DELETE FROM Tarea WHERE id = pId;
END //

-- R.F.03. Agregar usuarios al sistema

DROP PROCEDURE IF EXISTS pInsertUsuario;
CREATE PROCEDURE
    pInsertUsuario(
        pNombre VARCHAR(255),
        pCorreo VARCHAR(255),
        pDepartamento VARCHAR(50),
        pRol VARCHAR(20)
    )
BEGIN
    -- Validaciones
    IF pNombre IS NULL OR TRIM(pNombre) = '' THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'ERROR: El usuario tiene que tener un nombre.';
    END IF;

    IF EXISTS (SELECT * FROM Persona WHERE nombre = pNombre) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'ERROR: Ya hay una persona con ese nombre';
    END IF;

    IF pCorreo IS NULL OR TRIM(pCorreo) = '' THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'ERROR: El usuario tiene que tener un correo.';
    END IF;

    IF pDepartamento IS NULL OR TRIM(pDepartamento) = '' THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'ERROR: El usuario tiene que tener un departamento.';
    END IF;

    IF pRol IS NULL OR (pRol != 'Miembro' AND pRol != 'Team Leader') THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'ERROR: El rol tiene que ser Miembro o Team Leader.';
    END IF;

    -- Insertar en Persona
    INSERT INTO Persona(nombre, correo, departamento)
    VALUES(pNombre, pCorreo, pDepartamento);

    -- Insertar en Rol
    INSERT INTO Rol(personaId, rol)
    VALUES(LAST_INSERT_ID(), pRol);
END //

-- R.F.04. Eliminar usuarios del sistema
DROP PROCEDURE IF EXISTS pDeleteUsuario;
CREATE PROCEDURE
    pDeleteUsuario(pId INT)
BEGIN
    IF NOT EXISTS (SELECT * FROM Persona WHERE id = pId) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'ERROR: No se ha encontrado el usuario.';
    END IF;

    DELETE FROM Persona WHERE id = pId;
END //

DELIMITER ;

-- Insertar datos de prueba
CALL pInsertUsuario('Ángel García', 'angel@alum.us.es', 'Percepcion', 'Team Leader');
CALL pInsertUsuario('David Guil', 'david@alum.us.es', 'Percepcion', 'Miembro');
INSERT INTO Asignacion (personaId, fechaAsignacion, numeroHoras) VALUES
(1, DEFAULT, 5),
(2, '2023-10-01 09:00:00', 4);
CALL pInsertTarea(1, 'Desarrollar algoritmo de visión', 'Implementar algoritmo de detección de obstáculos', 'Pendiente', '', '2024-12-01 23:59:59');
CALL pInsertTarea(2, 'Desarrollar algoritmo del simulador', 'Implementar algoritmo de tiempo por vuelta', 'Empezado', '', '2024-12-05 23:59:59');
CALL pDeleteTarea(1);
-- CALL pDeleteUsuario(2);