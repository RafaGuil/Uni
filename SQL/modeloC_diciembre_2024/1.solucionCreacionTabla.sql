DROP TABLE IF EXISTS Valoraciones;

CREATE TABLE Valoraciones (
    id INT PRIMARY KEY AUTO_INCREMENT,
    productoId INT NOT NULL,
    clienteId INT NOT NULL,
    puntuacion INT NOT NULL CHECK (puntuacion >= 1 AND puntuacion <= 5),
    fecha DATE NOT NULL,
    UNIQUE(clienteId, productoId),
    FOREIGN KEY (clienteId) REFERENCES clientes(id),
    FOREIGN KEY (productoId) REFERENCES productos(id)
    	ON DELETE CASCADE
    	ON UPDATE CASCADE
)