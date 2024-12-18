DROP DATABASE IF EXISTS ARUS;
CREATE DATABASE ARUS;
USE ARUS;


-- Eliminamos las tablas
DROP TABLE IF EXISTS Turno;
DROP TABLE IF EXISTS Tarea;
DROP TABLE IF EXISTS Asignacion;
DROP TABLE IF EXISTS Pago;
DROP TABLE IF EXISTS Rol;
DROP TABLE IF EXISTS Persona;

-- Creamos la tabla Persona
CREATE TABLE Persona (
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    nombre VARCHAR(255) NOT NULL,
    correo VARCHAR(255) NOT NULL UNIQUE,
    departamento ENUM(
        'Aerodinámica',
        'Business',
        'Control',
        'Chasis',
        'Cost',
        'Dinámica',
        'Electrónica',
        'E-Powertrain',
        'Marketing',
        'Percepción',
        'Suspensión y transmisión'
    ) NOT NULL,
    CONSTRAINT correoCheck CHECK (correo LIKE '%@alum.us.es')
);

-- Creamos la tabla Rol
CREATE TABLE Rol (
    personaId INT PRIMARY KEY NOT NULL,
    rol ENUM('Miembro', 'Team Leader') NOT NULL,
    FOREIGN KEY (personaId) REFERENCES Persona(id) ON DELETE CASCADE
);

-- Creamos la tabla Pago
CREATE TABLE Pago (
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    personaId INT NOT NULL,
    cantidad DECIMAL(10, 2) NOT NULL,
    concepto VARCHAR(255),
    realizado BOOLEAN NOT NULL,
    FOREIGN KEY (personaId) REFERENCES Persona(id) ON DELETE CASCADE
);

-- Creamos la tabla Asignacion
CREATE TABLE Asignacion (
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    personaId INT,
    fechaAsignacion DATETIME NOT NULL DEFAULT NOW(),
    numeroHoras INT NOT NULL,
    FOREIGN KEY (personaId) REFERENCES Persona(id) ON DELETE SET NULL
);

-- Creamos la tabla Tarea
CREATE TABLE Tarea (
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    asignacionId INT NOT NULL,
    nombre VARCHAR(255) NOT NULL,
    descripcion VARCHAR(255),
    estado ENUM('Pendiente', 'Empezado', 'Completado', 'Con retraso') NOT NULL,
    comentario VARCHAR(255),
    fechaEntrega DATETIME,
    FOREIGN KEY (asignacionId) REFERENCES Asignacion(id) ON DELETE CASCADE
);

-- Creamos la tabla Turno
CREATE TABLE Turno (
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    tareaId INT NOT NULL,
    fecha DATETIME NOT NULL,
    ubicacion VARCHAR(255) NOT NULL,
    duracion INT,
    comentario VARCHAR(255),
    asiste BOOLEAN NOT NULL,
    FOREIGN KEY (tareaId) REFERENCES Tarea(id) ON DELETE CASCADE
);
