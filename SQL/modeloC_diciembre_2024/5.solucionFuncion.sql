DELIMITER //
-- incluya su solución a continuación
CREATE OR REPLACE FUNCTION calcular_fidelidad_cliente(clienteId INT) RETURNS DECIMAL(10, 2)
BEGIN
	DECLARE n_pedidos INT;
	DECLARE gasto_total DECIMAL(10, 2);
	DECLARE res DECIMAL(10, 2);
	
	SET n_pedidos = (SELECT COUNT(*) FROM pedidos P WHERE clienteId = clienteId); -- Mirar por qué /clienteId = clienteId/ y no /P.clienteId = clienteId/
	
	SET gasto_total = (SELECT COALESCE(SUM(LP.unidades * LP.precio), 0) FROM lineaspedido LP JOIN pedidos P ON LP.pedidoId = P.id WHERE P.clienteId = clienteId);
	
	SET res = (n_pedidos * 0.5) + (gasto_total * 0.05);
	
	RETURN(res);
	
END //

-- fin de su solución
DELIMITER ;

SELECT calcular_fidelidad_cliente(1);

 DELIMITER //

CREATE OR REPLACE PROCEDURE registrar_cliente_premium(
  IN p_email VARCHAR(255),
  IN p_contrasena VARCHAR(255),
  IN p_nombre VARCHAR(255),
  IN p_direccionEnvio VARCHAR(255),
  IN p_codigoPostal VARCHAR(10),
  IN p_fechaNacimiento DATE
)
BEGIN
  DECLARE v_usuarioId INT;
  DECLARE v_clienteId INT;
  DECLARE v_pedidoId INT;
  DECLARE v_smartphoneId INT;
  DECLARE v_facturacionTotal DECIMAL(10, 2);
  DECLARE v_clientesPremiumPermitidos INT;
  DECLARE v_clientesPremiumRegistrados INT;

  -- Manejo de errores
  DECLARE EXIT HANDLER FOR SQLEXCEPTION
  BEGIN
      ROLLBACK;
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error al registrar cliente premium';
  END;

  -- Iniciar transacción
  START TRANSACTION;

  -- Calcular la facturación total del mes anterior
  SET v_facturacionTotal = (SELECT SUM(lp.precio * lp.unidades)
  FROM LineasPedido lp
  JOIN Pedidos p ON lp.pedidoId = p.id
  WHERE MONTH(p.fechaRealizacion) = MONTH(CURDATE()) - 1
  AND YEAR(p.fechaRealizacion) = YEAR(CURDATE()));

  IF v_facturacionTotal IS NULL THEN
      SET v_facturacionTotal = 0; -- Si no hay facturación, se considera 0.
  END IF;

  -- Calcular cuántos clientes premium están permitidos
  SET v_clientesPremiumPermitidos = FLOOR(v_facturacionTotal / 5000);

  -- Contar cuántos clientes premium se han registrado este mes
  SET v_clientesPremiumRegistrados = (SELECT COUNT(DISTINCT p.clienteId)
  FROM Pedidos p
  JOIN LineasPedido lp ON p.id = lp.pedidoId
  JOIN Productos prod ON lp.productoId = prod.id
  WHERE prod.nombre = 'Smartphone' AND lp.precio = 0
  AND MONTH(p.fechaRealizacion) = MONTH(CURDATE())
  AND YEAR(p.fechaRealizacion) = YEAR(CURDATE()));

  -- Verificar si se ha alcanzado el límite de clientes premium
  IF v_clientesPremiumRegistrados >= v_clientesPremiumPermitidos THEN
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Límite de clientes premium alcanzado';
  END IF;

  -- Crear el usuario
  INSERT INTO Usuarios (email, contraseña, nombre)
  VALUES (p_email, p_contrasena, p_nombre);

  SET v_usuarioId = LAST_INSERT_ID();

  -- Crear el cliente
  INSERT INTO Clientes (usuarioId, direccionEnvio, codigoPostal, fechaNacimiento)
  VALUES (v_usuarioId, p_direccionEnvio, p_codigoPostal, p_fechaNacimiento);

  SET v_clienteId = LAST_INSERT_ID();

  -- Obtener el ID del producto "Smartphone"
  SELECT id INTO v_smartphoneId
  FROM Productos
  WHERE nombre = 'Smartphone';

  IF v_smartphoneId IS NULL THEN
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El producto "Smartphone" no existe';
  END IF;

  -- Crear el pedido por defecto
  INSERT INTO Pedidos (clienteId, direccionEntrega, fechaRealizacion)
  VALUES (v_clienteId, p_direccionEnvio, CURDATE());

  SET v_pedidoId = LAST_INSERT_ID();

  -- Insertar la línea de pedido con precio 0
  INSERT INTO LineasPedido (pedidoId, productoId, unidades, precio)
  VALUES (v_pedidoId, v_smartphoneId, 1, 0);

  -- Confirmar transacción
  COMMIT;
END//

DELIMITER ;

SET FOREIGN_KEY_CHECKS=0;
TRUNCATE TABLE pedidos;
TRUNCATE TABLE clientes;
TRUNCATE TABLE empleados;
TRUNCATE TABLE lineaspedido;
TRUNCATE TABLE productos;
TRUNCATE TABLE tiposproducto;
TRUNCATE TABLE usuarios;
SET FOREIGN_KEY_CHECKS=0;

INSERT INTO Usuarios (email, contraseña, nombre)
VALUES 
('cliente1@example.com', 'password123', 'Cliente Uno'),
('cliente2@example.com', 'password123', 'Cliente Dos'),
('cliente3@example.com', 'password123', 'Cliente Tres');

INSERT INTO Clientes (usuarioId, direccionEnvio, codigoPostal, fechaNacimiento)
VALUES 
(1, 'Calle A, 123', '41001', '1990-05-10'),
(2, 'Calle B, 456', '41002', '1985-08-20'),
(3, 'Calle C, 789', '41003', '2000-12-15');

INSERT INTO Productos (nombre, descripción, precio, tipoProductoId, puedeVenderseAMenores)
VALUES 
('Smartphone', 'Un teléfono inteligente', 800.00, 1, FALSE),
('Auriculares', 'Auriculares Bluetooth', 150.00, 2, TRUE),
('Cargador', 'Cargador rápido USB-C', 50.00, 2, TRUE);

-- Pedidos de Cliente 1 en el mes anterior
INSERT INTO Pedidos (fechaRealizacion, fechaEnvio, direccionEntrega, clienteId)
VALUES 
(DATE_SUB(CURDATE(), INTERVAL 1 MONTH), DATE_SUB(CURDATE(), INTERVAL 25 DAY), 'Calle A, 123', 1),
(DATE_SUB(CURDATE(), INTERVAL 1 MONTH), DATE_SUB(CURDATE(), INTERVAL 20 DAY), 'Calle A, 123', 1);

-- Pedidos de Cliente 2 en el mes anterior
INSERT INTO Pedidos (fechaRealizacion, fechaEnvio, direccionEntrega, clienteId)
VALUES 
(DATE_SUB(CURDATE(), INTERVAL 1 MONTH), DATE_SUB(CURDATE(), INTERVAL 28 DAY), 'Calle B, 456', 2);

-- Líneas de Pedido para Cliente 1
INSERT INTO LineasPedido (pedidoId, productoId, unidades, precio)
VALUES 
(1, 1, 2, 800.00), -- Smartphone x2
(1, 3, 1, 50.00),  -- Cargador x1
(2, 2, 3, 150.00); -- Auriculares x3

-- Líneas de Pedido para Cliente 2
INSERT INTO LineasPedido (pedidoId, productoId, unidades, precio)
VALUES 
(3, 1, 1, 800.00), -- Smartphone x1
(3, 2, 2, 150.00); -- Auriculares x2


-- Incrementar facturación para Cliente 1
INSERT INTO Pedidos (fechaRealizacion, fechaEnvio, direccionEntrega, clienteId)
VALUES (DATE_SUB(CURDATE(), INTERVAL 1 MONTH), DATE_SUB(CURDATE(), INTERVAL 15 DAY), 'Calle A, 123', 1);

INSERT INTO LineasPedido (pedidoId, productoId, unidades, precio)
VALUES (4, 1, 4, 800.00); -- Smartphone x4 (3200 € adicionales)

CALL registrar_cliente_premium(
    'premium1@example.com',
    'password123',
    'Cliente Premium Uno',
    'Calle Premium, 1',
    '41004',
    '1988-07-25'
);