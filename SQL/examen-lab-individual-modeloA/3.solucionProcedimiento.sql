DELIMITER //

CREATE OR REPLACE PROCEDURE actualizar_precio_producto(
    IN p_productoId INT,
    IN p_nuevoPrecio DECIMAL(10, 2)
)
-- incluya su solución a continuación
BEGIN

	DECLARE precio DECIMAL(10, 2);

	DECLARE EXIT HANDLER FOR SQLEXCEPTION
		BEGIN
			ROLLBACK;
			RESIGNAL;
		END;
	
	START TRANSACTION;
		
		SET precio = (SELECT P.precio FROM productos P WHERE P.id = p_productoId);
		
		IF precio IS NULL THEN
			SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Producto no encontrado.';
		END IF;
		
		IF p_nuevoPrecio < precio * 0.5 THEN
			SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No se permite rebajar el precio más del 50%.';
		END IF;

		UPDATE productos P
		SET P.precio = p_nuevoPrecio
		WHERE P.id = p_productoId;
		
		UPDATE lineaspedido LP
		JOIN pedidos PE ON PE.id = LP.pedidoId
		SET precio = p_nuevoPrecio
		WHERE LP.productoId = p_productoId AND PE.fechaEnvio > CURDATE();


	COMMIT;
END //
-- fin de su solución
DELIMITER ;

CALL actualizar_precio_producto(
    1,
    500.00
)