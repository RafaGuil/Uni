DELIMITER //

-- R.N.01. Registro de persona
CREATE OR REPLACE TRIGGER tInsertPersona
BEFORE INSERT ON Persona FOR EACH ROW
BEGIN
    DECLARE pRol VARCHAR(20);
    SET pRol = (SELECT rol FROM Rol R WHERE R.personaId = @usuario_actual_id);
    IF pRol != 'Team Leader' THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'ERROR: Solo los Team Leaders pueden agregar usuarios.';
    END IF;
END //

-- R.N.02. Añadir tareas
CREATE OR REPLACE TRIGGER tTareaInsert
BEFORE INSERT ON Tarea FOR EACH ROW
BEGIN
    DECLARE pRol VARCHAR(20);
    SET pRol = (SELECT rol FROM Rol R WHERE R.personaId = @usuario_actual_id);
    IF pRol != 'Team Leader' THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'ERROR: Solo los Team Leaders pueden añadir tareas.';
    END IF;
END //

-- R.N.02. Eliminar tareas
CREATE OR REPLACE TRIGGER tTareaDelete
BEFORE DELETE ON Tarea FOR EACH ROW
BEGIN
    DECLARE pRol VARCHAR(20);
    SET pRol = (SELECT rol FROM Rol R WHERE R.personaId = @usuario_actual_id);
    IF pRol != 'Team Leader' THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'ERROR: Solo los Team Leaders pueden eliminar tareas.';
    END IF;
END //

-- R.N.02. Editar tareas
CREATE OR REPLACE TRIGGER tUpdateTarea
BEFORE UPDATE ON Tarea FOR EACH ROW
BEGIN
    DECLARE pRol VARCHAR(20);
    SET pRol = (SELECT rol FROM Rol R WHERE R.personaId = @usuario_actual_id);
    
    IF pRol = 'Miembro' AND
    ((NEW.nombre != OLD.nombre) OR 
    (NEW.descripcion != OLD.descripcion) OR 
    (NEW.fechaEntrega != OLD.fechaEntrega) OR 
    (NEW.asignacionId != OLD.asignacionId)) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'ERROR: Los miembros solo pueden editar el estado y los comentarios.';
    END IF;

END //

-- R.N.02. Cambiar estado de tareas al insertar
CREATE OR REPLACE TRIGGER tTareaUpdateEstado
BEFORE UPDATE ON Tarea FOR EACH ROW
BEGIN
    IF OLD.fechaEntrega < NOW() THEN
        SET NEW.estado = 'Con retraso';
    END IF;
END //

-- R.N.03. Número de TLs
CREATE OR REPLACE TRIGGER tNumeroTLPorDepartamento
BEFORE INSERT ON Persona FOR EACH ROW
BEGIN
    DECLARE pNumeroTL INT;
    SET pNumeroTL = (SELECT COUNT(*) FROM Rol R JOIN Persona P ON R.personaId = P.id 
        WHERE R.rol = 'Team Leader' AND P.departamento = NEW.departamento);
    IF pNumeroTL > 1 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Un departamento no puede tener más de un Team Leader';
    END IF;
END //

DELIMITER ;
