DELIMITER //
-- incluya su solución a continuación
CREATE OR REPLACE TRIGGER p_limitar_unidades_mensuales_de_productos_fisicos
BEFORE INSERT ON lineaspedido FOR EACH ROW
BEGIN

	DECLARE unidades_mes INT;
	DECLARE tipo_producto INT;
	DECLARE fecha DATE;
	
	SELECT PR.tipoProductoId INTO tipo_producto FROM productos PR
	WHERE PR.id = NEW.productoId;

	IF (tipo_producto = 1) THEN
	
		SET fecha = (SELECT p.fechaRealizacion FROM pedidos P WHERE P.id = NEW.pedidoId);
		
		SET unidades_mes = (SELECT SUM(LP.unidades) FROM lineaspedido LP 
								WHERE LP.producto = NEW.productoId AND
								MONTH(CURDATE()) = MONTH(FECHA) AND
								YEAR(CURDATE()) = YEAR(FECHA));
								
		IF (NEW.unidades + unidades_mes > 1000) THEN
			SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No se pueden vender tantas unidades de este producto';
		END IF;
		
	END IF;
	
END //
-- fin de su solución
DELIMITER ;