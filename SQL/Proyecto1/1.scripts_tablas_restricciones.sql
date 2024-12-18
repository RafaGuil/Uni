DROP TABLE IF EXISTS usuarios;
DROP TABLE IF EXISTS citaUrgencias;
DROP TABLE IF EXISTS agenda;
DROP TABLE IF EXISTS lugar;
DROP TABLE IF EXISTS citas;
DROP TABLE IF EXISTS registroAcceso;

CREATE TABLE usuarios(
	usuarioId INT NOT NULL AUTO_INCREMENT,
	telefono VARCHAR(25) NOT NULL, #poner el prefijo del + mirarlo
	dni VARCHAR(9) NOT NULL UNIQUE,
	nombre VARCHAR(50) NOT NULL, 
	apellido1 VARCHAR(50) NOT NULL,
	apellido2 VARCHAR(50) NOT NULL, 
	contrasena VARCHAR(255) NOT NULL,
	fechaNacimiento DATE NOT NULL,
	especialidad VARCHAR(50), 
	tipoUsuario ENUM('Médico', 'Enfermero', 'Administrativo', 'Paciente') NOT NULL,
	PRIMARY KEY (usuarioId),
	CONSTRAINT check_dni CHECK (dni REGEXP '^[0-9]{8}[A-Za-z]$'),
	CONSTRAINT check_contrasena_especial CHECK (contrasena REGEXP '[!@#$%^&*()_+\\[\\]{}|;:,.<>?]') ##REVISAR
	);
	
CREATE TABLE citaUrgencias(
	citaUrgenciasId INT NOT NULL AUTO_INCREMENT, 
	medicoId INT,
	pacienteId INT,
	enfermeroId INT,
	motivo TEXT NOT NULL, 
	fechahoraLlegada DATETIME DEFAULT NOW(), 
	fechaHoraAtencion DATETIME, 
	triage INT,
	diagnostico TEXT,
	CONSTRAINT check_triage CHECK (triage >= 1 AND triage <= 5),
	PRIMARY KEY(citaUrgenciasId),
	FOREIGN KEY (medicoId) REFERENCES usuarios(usuarioId)
		ON DELETE RESTRICT
		ON UPDATE CASCADE,
	FOREIGN KEY (pacienteId) REFERENCES usuarios(usuarioId)
		ON DELETE RESTRICT
		ON UPDATE CASCADE,
	FOREIGN KEY (enfermeroId) REFERENCES usuarios(usuarioId)
		ON DELETE RESTRICT
		ON UPDATE CASCADE
);

CREATE TABLE agenda (
    agendaId INT NOT NULL AUTO_INCREMENT,
    medicoId INT NOT NULL,
    fechaInicio DATE NOT NULL,
    fechaFin DATE NOT NULL,
    diaSemana ENUM('Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo') NOT NULL,
    horaInicio TIME NOT NULL,
    horaFin TIME NOT NULL,
    duracionCita TIME NOT NULL,
    PRIMARY KEY (agendaId),
    CONSTRAINT check_fechaFin CHECK (fechaFin > fechaInicio),
    CONSTRAINT check_horaFin CHECK (horaFin > horaInicio),
    FOREIGN KEY (medicoId) REFERENCES usuarios (usuarioId)
    ON DELETE RESTRICT
    ON UPDATE CASCADE
);

CREATE TABLE lugar(
	lugarId INT NOT NULL AUTO_INCREMENT,
	edificio VARCHAR(50) NOT NULL,
	planta VARCHAR(25) NOT NULL,
	puerta VARCHAR(25) NOT NULL,
	PRIMARY KEY (lugarId)
);

CREATE TABLE citas(
	citaId INT NOT NULL AUTO_INCREMENT,
	medicoId INT NOT NULL,
	pacienteId INT NOT NULL,
	agendaId INT NOT NULL , 
	lugarId INT NOT NULL,
	fechaHoraCita DATETIME NOT NULL,
	fechaHoraFinCita DATETIME,
	motivo TEXT NOT NULL,
	diagnostico TEXT,
	PRIMARY KEY(citaId),
	FOREIGN KEY(medicoId) REFERENCES usuarios(usuarioId)
	ON DELETE RESTRICT 
	ON UPDATE CASCADE,
	FOREIGN KEY(pacienteId) REFERENCES usuarios(usuarioId)
	ON DELETE RESTRICT 
	ON UPDATE CASCADE,
	FOREIGN KEY(agendaId) REFERENCES agenda(agendaId)
	ON DELETE RESTRICT
	ON UPDATE CASCADE,
	FOREIGN KEY (lugarId) REFERENCES lugar(lugarId)
	ON DELETE RESTRICT
	ON UPDATE CASCADE
);

CREATE TABLE registroAcceso(
	registroId INT NOT NULL AUTO_INCREMENT,
	medicoId INT,
	administrativoId INT,
	enfermeroId INT,
	citaId INT,
	citaUrgenciasId INT,
	fechaConsulta DATETIME DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (registroId),
	FOREIGN KEY (medicoId) REFERENCES usuarios(usuarioId)
		ON DELETE RESTRICT
		ON UPDATE CASCADE,
	FOREIGN KEY (administrativoId) REFERENCES usuarios(usuarioId)
		ON DELETE RESTRICT
		ON UPDATE CASCADE,
	FOREIGN KEY (enfermeroId) REFERENCES usuarios(usuarioId)
		ON DELETE RESTRICT
		ON UPDATE CASCADE,
	FOREIGN KEY (citaId) REFERENCES citas(citaId)
		ON DELETE RESTRICT
		ON UPDATE CASCADE,
	FOREIGN KEY (citaUrgenciasId) REFERENCES citaUrgencias(citaUrgenciasId)
		ON DELETE RESTRICT
		ON UPDATE CASCADE
);