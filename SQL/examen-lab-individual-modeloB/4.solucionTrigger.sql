DELIMITER //
-- incluya su solución a continuación
CREATE OR REPLACE TRIGGER t_limitar_importe_pedidos_de_menores
BEFORE INSERT ON lineaspedido FOR EACH ROW
BEGIN

	DECLARE fechaNacimiento DATE;
	
	SET fechaNacimiento = (SELECT C.fechaNacimiento FROM clientes C JOIN pedidos P ON C.id = P.clienteId JOIN lineaspedido LP ON P.id = LP.pedidoId WHERE LP.id = NEW.id);

	IF (NEW.precio > 500 AND fechaNacimiento >= CURDATE() - INTERVAL 18 YEAR) THEN
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Los pedidos realizados por menores no pueden superar los 500€.';
	END IF;

END //
-- fin de su solución
DELIMITER ;

