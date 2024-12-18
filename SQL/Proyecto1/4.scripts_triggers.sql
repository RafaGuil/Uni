--- Validar fecha nacimiento ---
DELIMITER //

CREATE TRIGGER validar_fecha_nacimiento
BEFORE INSERT ON usuarios
FOR EACH ROW
BEGIN
    IF NEW.fechaNacimiento > CURDATE() THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'La fecha de nacimiento no puede ser posterior a la fecha actual.';
    END IF;
END;
//

DELIMITER ;

--- Validar fecha cita de urgencias ---
DELIMITER //

CREATE TRIGGER validar_fechas_cita_urgencias
BEFORE INSERT ON citaUrgencias
FOR EACH ROW
BEGIN
    IF NEW.fechahoraLlegada > NOW() THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'La fecha y hora de llegada no puede ser posterior a la fecha y hora actual.';
    END IF;

    IF NEW.fechaHoraAtencion IS NOT NULL AND NEW.fechaHoraAtencion <= NEW.fechahoraLlegada THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'La fecha y hora de atención debe ser posterior a la fecha y hora de llegada.';
    END IF;
END;
//

DELIMITER ;

--- Validar fecha de inicio de agenda ---
DELIMITER //

CREATE TRIGGER validar_fecha_inicio_agenda
BEFORE INSERT ON agenda
FOR EACH ROW
BEGIN
    IF NEW.fechaInicio <= NOW() THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'La fecha de inicio debe ser posterior a la fecha y hora actual.';
    END IF;
END;
//

DELIMITER ;

--- Validar que la especialidad cuando se registre un médico nunca sea una cadena vacía ni nulo

DELIMITER //

CREATE OR REPLACE TRIGGER especilidadMedico
BEFORE INSERT ON usuarios
FOR EACH ROW
BEGIN
	IF ((NEW.especialidad = '' OR NEW.especialidad IS NULL) AND (NEW.tipoUsuario = 'Médico')) THEN 
			SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Un médico es obligatorio añadir una especialidad';
	END IF;

END//
DELIMITER ;