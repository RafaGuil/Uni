DELIMITER //

CREATE PROCEDURE insertar_producto_y_regalos(
    IN p_nombre VARCHAR(255),
    IN p_descripcion VARCHAR(255),
    IN p_precio DECIMAL(10,2),
    IN p_tipoProductoId INT,
    IN p_esParaRegalo BOOLEAN
)
-- incluya su solución a continuación
BEGIN

	DECLARE idProducto INT;
	DECLARE idPedido INT;
	
	DECLARE EXIT HANDLER FOR SQLEXCEPTION BEGIN
		ROLLBACK;
		RESIGNAL;
	END;	
	
	START TRANSACTION;
		
		IF p_precio > 50 THEN
			SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No se permite crear un producto para regalo de más de 50€.';
		END IF;
		
		INSERT INTO Productos (nombre, descripción, precio, tipoProductoId, puedeVenderseAMenores) 
		VALUES (p_nombre, p_descripcion, p_precio, p_tipoProductoId, TRUE);
		
		SET idProducto = (SELECT MAX(P.id) FROM productos P);
		
		IF p_esParaRegalo IS TRUE THEN
			INSERT INTO Pedidos (fechaRealizacion, fechaEnvio, direccionEntrega, comentarios, clienteId, empleadoId) 
			VALUES (CURDATE(), CURDATE()+1, 'A', NULL, 1, NULL);
			
			SET idPedido = (SELECT MAX(PE.id) FROM pedidos PE);
			
			INSERT INTO LineasPedido (pedidoId, productoId, unidades, precio) 
			VALUES (idPedido, idProducto, 1, 0);
		END IF;
		
	COMMIT;
END //
-- fin de su solución
DELIMITER ;