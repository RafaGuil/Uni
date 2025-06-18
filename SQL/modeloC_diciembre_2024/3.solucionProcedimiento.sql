DELIMITER //

DROP PROCEDURE bonificar_pedido_retrasado;
CREATE PROCEDURE bonificar_pedido_retrasado(IN p_pedidoId INT)
-- incluya su solución a continuación
BEGIN 
	DECLARE empleado INT;
	DECLARE pedido ROW TYPE OF pedidos;
	DECLARE newEmpleado INT;
	
	DECLARE EXIT HANDLER FOR SQLEXCEPTION
		BEGIN
			ROLLBACK;
			SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error al bonificar pedido retrasado';
		END;
	
	START TRANSACTION;
	
		SET pedido = (SELECT * FROM pedidos P WHERE P.id = p_pedidoId);
		SET empleado = (SELECT e.id FROM empleados E WHERE e.id = pedido.empleadoId);
	
		IF empleado IS NULL THEN 
			SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El pedido no tiene gestor';
		END IF;
		
			SELECT e.id INTO newEmpleado
			FROM empleados E
			WHERE e.id != empleado
			LIMIT 1;
			
			UPDATE pedidos
			SET empleadoId = newEmpleado
			WHERE id = p_pedidoId;
			
			UPDATE lineaspedido
			SET precio = precio*0.8
			WHERE pedidoId = p_pedidoId;
				
	COMMIT;
END //
-- fin de su solución
DELIMITER ;

CALL bonificar_pedido_retrasado(1);