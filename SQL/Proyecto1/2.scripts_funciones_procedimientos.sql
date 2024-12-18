--- CONFIGURA EL IDIOMA DE LA SESIÓN DE INGLÉS A ESPAÑOL

DELIMITER //

SET lc_time_names = 'es_ES';

DELIMITER ;

--- PROCEDIMIENTO PARA REGISTRAR UN USUARIO
DELIMITER //

CREATE OR REPLACE PROCEDURE registro (
    IN p_telefono VARCHAR(15),
    IN p_dni VARCHAR(10),
    IN p_nombre VARCHAR(50),
    IN p_apellido1 VARCHAR(50),
    IN p_apellido2 VARCHAR(50),
    IN p_contrasena VARCHAR(255),
    IN p_fechaNacimiento DATE,
    IN p_especialidad VARCHAR(100),
    IN p_tipoUsuario ENUM('Médico', 'Paciente', 'Administrativo', 'Enfermero')
)
BEGIN
    DECLARE v_especialidad VARCHAR(100);
    
    START TRANSACTION;
    
   IF ((p_tipoUsuario = 'Enfermero') OR (p_tipoUsuario = 'Paciente') OR (p_tipoUsuario = 'Administrador')) THEN
   	SET v_especialidad = NULL;
   END IF;
   
   if ((p_especialidad != '') AND (p_tipoUsuario = 'Médico')) THEN 
   	SET v_especialidad = p_especialidad;
   END IF;

    -- Insertar el usuario con la especialidad validada
    INSERT INTO usuarios (
        telefono, dni, nombre, apellido1, apellido2, contrasena, fechaNacimiento, especialidad, tipoUsuario
    )
    VALUES (
        p_telefono, p_dni, p_nombre, p_apellido1, p_apellido2, p_contrasena, p_fechaNacimiento, v_especialidad, p_tipoUsuario
    );
END //

DELIMITER ;

--- PROCEDIMIENTO PARA CREAR CITA ---
DELIMITER //

CREATE OR REPLACE PROCEDURE crearAgenda(
	IN p_medicoId INT,
	IN p_fechaInicio DATE,
	IN p_fechaFin DATE,
	IN p_diaSemana ENUM('Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'),
	IN p_horaInicio TIME,
	IN p_horaFin TIME,
	IN p_duracionCita TIME
)
BEGIN

	DECLARE v_medicoId INT;

    SELECT usuarioId INTO v_medicoId
    FROM usuarios
    WHERE usuarioId = p_medicoId
		AND tipoUsuario = 'Médico';

    IF v_medicoId IS NULL THEN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No se puede crear la agenda: El médico no existe.';
    END IF;
      
   INSERT INTO agenda(medicoId, fechaInicio, fechaFin, diaSemana, horaInicio, horaFin, duracionCita)
   VALUES (v_medicoId, p_fechaInicio, p_fechaFin, p_diaSemana, p_horaInicio, p_horaFin, p_duracionCita);

END//

DELIMITER ;

--- PROCEDIMIENTO PARA SOLICITAR CITA ---
DELIMITER //

CREATE OR REPLACE PROCEDURE solicitaCita  (
    IN p_medicoId INT,
    IN p_pacienteId INT,
    IN p_agendaId INT,
    IN p_lugarId INT,
    IN p_fechaHoraCita DATETIME,
    IN p_motivo TEXT
)
BEGIN
    
	 DECLARE v_medicoId INT;
	 DECLARE v_pacienteId INT;
	 DECLARE v_agendaId INT;
    DECLARE v_duracionCita TIME;
    DECLARE v_diaCita VARCHAR(20);
    DECLARE v_fechaFinCita DATETIME;
    DECLARE v_citaId INT;
    DECLARE v_citaFinId INT;
    DECLARE v_citaFin INT;
    DECLARE v_disponibilidadAgenda INT;

    -- Iniciar la transacción
    START TRANSACTION;
    SET lc_time_names = 'es_ES';


    SET v_diaCita = DAYNAME(DATE(p_fechaHoraCita)); -- Obtener día de la cita
	
	SELECT usuarios.usuarioId
	INTO v_medicoId
	FROM usuarios
	WHERE usuarios.usuarioId = p_medicoId;
	
	IF (v_medicoId IS NULL) then 
		ROLLBACK;
		SIGNAL SQLSTATE '45000'
       SET MESSAGE_TEXT = 'No se puede registrar la cita: el médico no existe';
    END IF;
    
   SELECT usuarios.usuarioId
	INTO v_pacienteId
	FROM usuarios
	WHERE usuarios.usuarioId = p_pacienteId;
	
   IF (v_pacienteId IS NULL) OR (p_pacienteId IS NULL) then 
   	ROLLBACK;
		SIGNAL SQLSTATE '45000'
       SET MESSAGE_TEXT = 'No se puede registrar la cita: el paciente no existe';
    END IF;
    
   SELECT COUNT(*) INTO v_disponibilidadAgenda
   FROM agenda
   WHERE agenda.agendaId = p_agendaId 
		AND agenda.diaSemana = v_diaCita AND 
		DATE(p_fechaHoraCita) BETWEEN fechaInicio AND fechaFin 
		AND TIME(p_fechaHoraCita) BETWEEN horaInicio AND horaFin;
   
   IF v_disponibilidadAgenda = 0 then 
   ROLLBACK;
   	SIGNAL SQLSTATE '45000'
   	SET MESSAGE_TEXT = 'No se puede registrar la cita: No está entre las horas de la agenda';
   END IF;
   
	SELECT agendaId, duracionCita
	INTO v_agendaId, v_duracionCita
	FROM agenda
	WHERE agendaId = p_agendaId;
  	
	IF v_agendaId IS NULL then 
   	ROLLBACK;
		SIGNAL SQLSTATE '45000'
       SET MESSAGE_TEXT = 'No se puede registrar la cita: La agenda no existe';
    END IF;
    
   IF v_duracionCita IS NULL THEN
        ROLLBACK;
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'No se puede registrar la cita: la duración de la cita no está definida en la agenda.';
    END IF;
    
   SELECT citas.citaId INTO v_citaId
	FROM citas
	WHERE (citas.medicoId = p_medicoId) AND (TIME(p_fechaHoraCita) BETWEEN TIME(fechaHoraCita) AND TIME(fechaHoraFinCita))
	LIMIT 1;
	
   IF v_citaId IS NOT NULL then 
   	ROLLBACK;
		SIGNAL SQLSTATE '45000'
       SET MESSAGE_TEXT = 'No se puede registrar la cita: el médico ya tiene una cita en esa fecha y hora.';
    END IF;

    -- Calcular la hora de fin de la cita
    SET v_fechaFinCita = ADDTIME(p_fechaHoraCita, v_duracionCita);
    
   SELECT citas.citaId INTO v_citaFin
	FROM citas
	WHERE (TIME(v_fechaFinCita) BETWEEN TIME(fechaHoraCita) AND TIME(fechaHoraFinCita))
	LIMIT 1;
	
    -- Comprobar que la fecha en la que termina la cita no esta entre una cita ya definida
   IF v_citaFinId IS NOT NULL then 
   	ROLLBACK;
		SIGNAL SQLSTATE '45000'
       SET MESSAGE_TEXT = 'No se puede registrar la cita: el médico ya tiene una cita en esa fecha y hora.';
    END IF;

    -- Insertar la cita
    INSERT INTO citas (medicoId, pacienteId, agendaId, lugarId, fechaHoraCita, fechaHoraFinCita, motivo)
    VALUES (p_medicoId, p_pacienteId, p_agendaId, p_lugarId, p_fechaHoraCita, v_fechaFinCita, p_motivo);

    -- Confirmar la transacción
    COMMIT;
END//
DELIMITER ;

--- Procedimiento para modificar una cita
DELIMITER //

CREATE OR REPLACE PROCEDURE modificarCita(
	IN p_citaId INT,
	IN p_fechaHoraCita DATETIME
)
BEGIN
	DECLARE v_diaSemana VARCHAR(20);
	DECLARE v_duracionCita TIME;
	DECLARE v_fechaFinCita DATETIME;
	DECLARE v_citaInicioId INT;
	DECLARE v_citaFinId INT;
	DECLARE v_agendaId INT;
	DECLARE v_disponibilidadAgenda INT;
	
	START TRANSACTION;

	SET lc_time_names = 'es_ES';

	SET v_diaSemana = DAYNAME(DATE(p_fechaHoraCita));
	
	SELECT citas.citaId INTO v_citaInicioId
	FROM citas
	WHERE (TIME(p_fechaHoraCita) BETWEEN TIME(fechaHoraCita) AND TIME(fechaHoraFinCita))
	LIMIT 1;
	
   IF v_citaInicioId IS NOT NULL then 
   	ROLLBACK;
		SIGNAL SQLSTATE '45000'
       SET MESSAGE_TEXT = 'No se puede registrar la cita: el médico ya tiene una cita en esa fecha y hora.';
    END IF;
	
	SELECT citas.agendaId INTO v_agendaId
	FROM citas
	WHERE citas.citaId = p_citaId;

	SELECT COUNT(*) INTO v_disponibilidadAgenda
    FROM agenda
    WHERE agenda.agendaId = v_agendaId 
		AND agenda.diaSemana = v_diaSemana AND 
		DATE(p_fechaHoraCita) BETWEEN fechaInicio AND fechaFin 
		AND TIME(p_fechaHoraCita) BETWEEN horaInicio AND horaFin;
   
    IF v_disponibilidadAgenda = 0 then 
    ROLLBACK;
   		SIGNAL SQLSTATE '45000'
   		SET MESSAGE_TEXT = 'No se puede registrar la cita: No está entre las horas de la agenda';
    END IF;
	
	SELECT agenda.duracionCita INTO v_duracionCita
    FROM agenda
    WHERE agenda.agendaId = v_agendaId;
   
    SET v_fechaFinCita = ADDTIME(p_fechaHoraCita, v_duracionCita);

    SELECT citas.citasId INTO v_citaFinId
	FROM citas
	WHERE (citas.medicoId = p_medicoId) AND (TIME(v_fechaFinCita) BETWEEN TIME(fechaHoraCita) AND TIME(fechaHoraFinCita))
	LIMIT 1;
	
	IF v_citaFinId IS NOT NULL then 
   	ROLLBACK;
		SIGNAL SQLSTATE '45000'
       SET MESSAGE_TEXT = 'No se puede registrar la cita: el médico ya tiene una cita en esa fecha y hora.';
    END IF;
   
   UPDATE citas
   SET citas.fechaHoraFinCita = v_fechaFinCita, citas.fechaHoraCita = p_fechaHoraCita
   WHERE citas.citaId = p_citaId;
   
   COMMIT;
   
END//

DELIMITER ;

--- Procedimientao para cancelar cita 


DELIMITER //

CREATE OR REPLACE PROCEDURE eliminarCita(
	IN p_citaId INT
)
BEGIN

	DECLARE v_citaId INT;
	
	SELECT citas.citaId
	INTO v_citaId
	FROM citas
	WHERE citas.citaId = p_citaId;
	
	if v_citaId IS NULL THEN 
	   ROLLBACK;
		SIGNAL SQLSTATE '45000'
      SET MESSAGE_TEXT = 'No se puede eliminar la cita: la cita no existe';
    END IF;
    
   DELETE FROM citas
   WHERE citas.citaId = p_citaId;

END //

DELIMITER ;

--- Procedimiento para crear lugar

DELIMITER //

CREATE OR REPLACE PROCEDURE crearLugar(
	IN p_edificio VARCHAR(50),
	IN p_planta VARCHAR(25),
	IN p_puerta VARCHAR(25)
	)
BEGIN 
	
	INSERT INTO lugar(edificio, planta, puerta)
	VALUES (p_edificio, p_planta, p_puerta);

END//

DELIMITER ;

--- Procedimiento para crear cita de urgencias

DELIMITER //

CREATE OR REPLACE PROCEDURE crearCitaUrgencias(
	IN p_pacienteId INT,
	IN p_enfermeroId INT,
	IN p_motivo TEXT,
	IN p_triage INT
)
BEGIN
	DECLARE v_pacienteId INT;
	DECLARE v_enfermeroId INT;
	DECLARE v_fechaAtencionCita DATETIME;
	DECLARE v_fechaLlegadaCita DATETIME;
	
	SELECT usuarios.usuarioId
	INTO v_pacienteId
	FROM usuarios
	WHERE usuarios.usuarioId = p_pacienteId AND usuarios.tipoUsuario = 'Paciente';
	
	IF v_pacienteId IS NULL THEN 
	   ROLLBACK;
		SIGNAL SQLSTATE '45000'
      SET MESSAGE_TEXT = 'No se puede añadir la cita de urgencias: el paciente no existe';
    END IF;
   
	SELECT usuarios.usuarioId
	INTO v_enfermeroId
	FROM usuarios
	WHERE usuarios.usuarioId = p_enfermeroId AND usuarios.tipoUsuario = 'Enfermero'; 
	
	IF v_enfermeroId IS NULL then 
		ROLLBACK;
		SIGNAL SQLSTATE '45000'
      SET MESSAGE_TEXT = 'No se puede añadir la cita de urgencias: el enfermero no existe';
    END IF;
    
   SET v_fechaLlegadaCita = NOW();
    
   IF p_triage = 1 THEN -- Nivel I: azul - atención inmediata
            SET v_fechaAtencionCita = v_fechaLlegadaCita;
      ELSEIF p_triage = 2 THEN
        		SET v_fechaAtencionCita = DATE_ADD(v_fechaLlegadaCita, INTERVAL 7 MINUTE);
      ELSEIF p_triage = 3 THEN
            SET v_fechaAtencionCita = DATE_ADD(v_fechaLlegadaCita, INTERVAL 30 MINUTE);
      ELSEIF p_triage = 4 THEN
            SET v_fechaAtencionCita =  DATE_ADD(v_fechaLlegadaCita, INTERVAL 45 MINUTE);
      ELSEIF p_triage = 5 THEN
            SET v_fechaAtencionCita =  DATE_ADD(v_fechaLlegadaCita, INTERVAL 60 MINUTE);
   END IF;  
    
   INSERT INTO citaurgencias(pacienteId, enfermeroId, motivo, triage, fechaHoraAtencion)
   VALUES(p_pacienteId, p_enfermeroId, p_motivo, p_triage, v_fechaAtencionCita);
   
END //

DELIMITER ;

--- Procedimiento por el que el medico acepta una cita de urgencias para ser atendida

DELIMITER //

CREATE OR REPLACE PROCEDURE aceptarCitaUrgencias(
    IN p_citaUrgenciasId INT,
    IN p_medicoId INT,
    IN p_fechaAtencionOpcional DATETIME
)
BEGIN
    DECLARE v_triage INT;
    DECLARE v_medicoId INT;
	     
   SELECT usuarios.usuarioId
	INTO v_medicoId
	FROM usuarios
	WHERE usuarios.usuarioId = p_medicoId;
	
	IF v_medicoId IS NULL THEN 
		SIGNAL SQLSTATE '45000'
      SET MESSAGE_TEXT = 'No se puede añadir la cita de urgencias: el medico no existe';
    END IF;
    
    IF p_fechaAtencionOpcional IS NULL then 
    	UPDATE citaurgencias
    	SET medicoId = p_medicoId
    	WHERE citaUrgenciasId = p_citaUrgenciasId;
    ELSE 
   	-- Actualizar la fecha de atención
   	UPDATE citaurgencias
    	SET medicoId = p_medicoId, fechaHoraAtencion = p_fechaAtencionOpcional
    	WHERE citaUrgenciasId = p_citaUrgenciasId;
   END IF;
   
END //

DELIMITER ;

--- Procedimiento para asignar diagnóstico a una cita
DELIMITER //

CREATE PROCEDURE insertarDiagnostico (
    IN p_citaId INT,
    IN p_diagnostico TEXT
)
BEGIN
    DECLARE v_citaId INT;
    -- Verificar que la cita existe
    SELECT citas.citaId INTO v_citaId
    FROM citas
    WHERE citas.citaId = p_citaId;

    IF v_citaId IS NULL THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'No se puede insertar el diagnóstico: la cita no existe';   
    END IF;
    
        -- Insertar el diagnóstico
        UPDATE citas 
        SET citas.diagnostico = p_diagnostico
		  WHERE citas.citaId = p_citaId;
END//

DELIMITER ;

--- Procedimiento para asignar diagnóstico a una cita de urgencias
DELIMITER //

CREATE OR REPLACE PROCEDURE insertarDiagnosticoCitaUrgencias(
	IN p_citaUrgenciaId INT,
	IN p_diagnostico TEXT
)
BEGIN
	DECLARE v_citaUrgenciaId INT;
	
	SELECT citaurgencias.citaUrgenciasId
	INTO v_citaUrgenciaId
	FROM citaurgencias
	WHERE citaurgencias.citaUrgenciasId = p_citaUrgenciaId;
	
	IF v_citaUrgenciaID IS NULL THEN
			SIGNAL SQLSTATE '45000'
      SET MESSAGE_TEXT = 'No se puede añadir un diagnóstico a la cita de urgencias: la cita de urgencias no existe';
   END IF;
   
   UPDATE citaurgencias
   SET diagnostico = p_diagnostico
   WHERE citaUrgenciasId = p_citaUrgenciaId;
END //

DELIMITER ;

--- Procedimiento para consultar las citas
DELIMITER //

CREATE OR REPLACE PROCEDURE registrarAccesoConsultaCita(
	IN p_medicoId INT,
	IN p_enfermeroId INT,
	IN p_administrativoId INT,
	IN p_citaId INT,
	IN p_citaUrgencias INT
) 
BEGIN

	IF p_medicoId IS NOT NULL THEN
		IF p_citaId IS NOT NULL THEN
			INSERT INTO registroacceso(medicoId, citaId)
			VALUES(p_medicoId, p_citaId);
		ELSE
			INSERT INTO registroacceso(medicoId, citaUrgenciasId)
			VALUES(p_medicoId, p_citaUrgencias);
		END IF;
	ELSEIF p_enfermeroId IS NOT NULL THEN 
		IF p_citaId IS NOT NULL THEN
			INSERT INTO registroacceso(enfermeroId, citaId)
			VALUES(p_enfermeroId, p_citaId);
		ELSE
			INSERT INTO registroacceso(enfermeroId, citaUrgenciasId)
			VALUES(p_enfermeroId, p_citaUrgencias);
		END IF;
	ELSEIF p_administrativoId IS NOT NULL THEN 
		IF p_citaId IS NOT NULL THEN
			INSERT INTO registroacceso(administrativoId, citaId)
			VALUES(p_administrativoId, p_citaId);
		ELSE
			INSERT INTO registroacceso(administrativoId, citaUrgenciasId)
			VALUES(p_administrativoId, p_citaUrgencias);
		END IF;
	END IF;
	
		IF p_citaId IS NOT NULL THEN
			SELECT *
			FROM citas
			WHERE citas.citaId = p_citaId;
		ELSE
			SELECT *
			FROM citaUrgencias
			WHERE citaurgencias.citaUrgenciasId = p_citaUrgencias;
		END IF;
	
END //

DELIMITER ;