DROP DATABASE IF EXISTS Videojuegos;
CREATE DATABASE Videojuegos ;
USE Videojuegos;

DROP TABLE if EXISTS  Progresos;
DROP TABLE if EXISTS  Jugadores;
DROP TABLE if EXISTS  Videojuegos;


CREATE TABLE Videojuegos(
	videojuegoId INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
	nombre VARCHAR(80) NOT NULL,
	fechaLanzamiento DATE,
	logros INT,
	estado ENUM('Lanzado', 'Beta', 'Acceso anticipado'),
	precioLanzamiento DOUBLE
);

CREATE TABLE Jugadores(
	jugadorId INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	nickname VARCHAR(60) NOT NULL
);

CREATE TABLE Progresos(
	progresoId INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	videojuegoId INT NOT NULL,
	jugadorId INT NOT NULL,
	fechaValoracion DATE NOT NULL,
	puntuacion DECIMAL(10,1) NOT NULL,
	opinion VARCHAR(60) NOT NULL,
	likes INT DEFAULT 0,
	veredicto ENUM('Imprescindible', 'Recomendado', 'Comprar en rebajas', 'No merece la pena') NOT NULL, -- RN-1-02
	FOREIGN KEY (videojuegoId) REFERENCES Videojuegos(videojuegoId),
	FOREIGN KEY (jugadorId) REFERENCES Jugadores(jugadorId),
	CONSTRAINT puntuacionMax CHECK(puntuacion >= 0 AND puntuacion <= 5), -- RN-1-01
	CONSTRAINT nValoracionesMismoJuego UNIQUE(videojuegoId, jugadorId) -- RN-1-03
);

DELIMITER //
CREATE OR REPLACE PROCEDURE 
	pInsertValoracion(
		pJugadorId INT,
		pVideojuegoId INT,
		pFechaValoracion DATE,
		pPuntuacion DECIMAL(10,1),
		pOpinion VARCHAR(60),
		pVeredicto VARCHAR(60)
	)
BEGIN
	INSERT INTO Progresos (jugadorId, videojuegoId, fechaValoracion, puntuacion, opinion, veredicto)
	VALUES (pJugadorId, pVideojuegoId, pFechaValoracion, pPuntuacion, pOpinion, pVeredicto);
END //

CREATE OR REPLACE TRIGGER fechaValoracionPrevFechaLanzamiento
BEFORE INSERT ON Progresos FOR EACH ROW
BEGIN
	DECLARE pFechaLanzamiento DATE;
	SET pFechaLanzamiento = (SELECT fechaLanzamiento FROM Videojuegos V WHERE videojuegoId = NEW.videojuegoId);

	IF pFechaLanzamiento > new.fechaValoracion THEN
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'ERROR: La fecha de valoración no puede ser anterior a la fecha de lanzamiento.';
	END IF;
END //

CREATE OR REPLACE FUNCTION fNValUsuario(pUsuarioId INT) RETURNS INT
BEGIN
	RETURN(
		SELECT COUNT(*)
		FROM Progresos P JOIN Jugadores J JOIN
		ON (P.jugadorId = J.jugadorId)
		WHERE J.jugadorId = pUsuarioId
	);
END //
DELIMITER ;


INSERT INTO Videojuegos(nombre, fechaLanzamiento,logros, estado,precioLanzamiento) VALUES ('The Legend of Zelda: Breath of the Wild', '2017-03-03', 76, 'Lanzado', 69.99);
INSERT INTO Videojuegos(nombre, fechaLanzamiento,logros, estado,precioLanzamiento) VALUES ('The Legend of Zelda: Tears of the Kingdom', '2023-05-12', 139, 'Lanzado', 79.99);
INSERT INTO Videojuegos(nombre, fechaLanzamiento,logros, estado,precioLanzamiento) VALUES ('Maniac Mansion', '1987-01-01', 1, 'Lanzado', 49.98);
INSERT INTO Videojuegos(nombre, fechaLanzamiento,logros, estado,precioLanzamiento) VALUES ('Horizon: Zero Dawn', '2017-02-28', 31, 'Lanzado', 79.99);
INSERT INTO Videojuegos(nombre, fechaLanzamiento,logros, estado,precioLanzamiento) VALUES ('Super Metroid', '1994-04-28', 1, 'Lanzado', 69.99);
INSERT INTO Videojuegos(nombre, fechaLanzamiento,logros, estado,precioLanzamiento) VALUES ('Final Fantasy IX', '2001-02-16', 9, 'Lanzado', 69.99);
INSERT INTO Videojuegos(nombre, fechaLanzamiento,logros, estado,precioLanzamiento) VALUES ('Pokemon Rojo', '1999-11-01', 151, 'Lanzado', 49.98);
INSERT INTO Videojuegos(nombre, fechaLanzamiento,logros, estado,precioLanzamiento) VALUES ('Pokemon Amarillo', '2000-06-16', 155, 'Lanzado', 49.98);
INSERT INTO Videojuegos(nombre, fechaLanzamiento,logros, estado,precioLanzamiento) VALUES ('Pokemon Beige Clarito', '2023-12-15', 3, 'Beta', 2000000);


INSERT INTO Jugadores(nickname) VALUES ('Currito92');
INSERT INTO Jugadores(nickname) VALUES ('MariTrini67');
INSERT INTO Jugadores(nickname) VALUES ('IISSI_USER');
INSERT INTO Jugadores(nickname) VALUES ('Samus');
INSERT INTO Jugadores(nickname) VALUES ('Aran');

-- Pruebas de aceptactión (positivas)
CALL pInsertValoracion(1, 2, CURDATE(), 5, 'Un comentario de texto cualquiera', 'Imprescindible');
CALL pInsertValoracion(2, 4, CURDATE(), 3, 'Un comentario de texto cualquiera', 'Comprar en rebajas');
CALL pInsertValoracion(3, 3, CURDATE(), 4, 'Un comentario de texto cualquiera', 'Recomendado');
CALL pInsertValoracion(4, 5, CURDATE(), 1, 'Un comentario de texto cualquiera', 'No merece la pena');
CALL pInsertValoracion(2, 3, CURDATE(), 4.5, 'Un comentario de texto cualquiera', 'Imprescindible');

-- Pruebas de aceptactión (negativas)
-- CALL pInsertValoracion(1, 6, CURDATE(), 10, 'Un comentario de texto cualquiera', 'Imprescindible'); -- RN-1-01
-- CALL pInsertValoracion(3, 1, CURDATE(), 3, 'Un comentario de texto cualquiera', 'Ni fu ni fa'); -- RN-1-02
-- CALL pInsertValoracion(3, 3, CURDATE(), 2, 'No era para tanto', 'No merece la pena'); -- RN-1-03
-- CALL pInsertValoracion(6, 8, CURDATE(), 3, 'Un comentario de texto cualquiera', 'Comprar en rebajas'); -- No existe esa referencia
-- CALL pInsertValoracion(2, 3, '1977-01-01', 4.5, 'Un comentario de texto cualquiera', 'Imprescindible'); -- Ejercicio 4

-- Ejercicio 3 
SELECT J.nickname, V.nombre, P.* FROM Progresos P 
	JOIN Jugadores J ON P.jugadorId = J.jugadorId
	JOIN Videojuegos V ON P.videojuegoId = V.videojuegoId
	ORDER BY videojuegoId;

-- Ejercicio 5
fNValUsuario(2);