DROP TABLE IF EXISTS Garantias;

CREATE TABLE Garantias (
	id INT PRIMARY KEY AUTO_INCREMENT,
	productoId INT UNIQUE,
	fechaIni DATE NOT NULL,
	fechaFin DATE NOT NULL CHECK (fechaFin > fechaIni),
	garantiaExtendida BOOLEAN NOT NULL,
	FOREIGN KEY (productoId) REFERENCES Productos(id)
);

INSERT INTO Garantias (productoId, fechaIni, fechaFin, garantiaExtendida) VALUES
							(1, '2024-01-15', '2025-01-15', TRUE),
							(2, '2024-01-15', '2025-01-15', TRUE)