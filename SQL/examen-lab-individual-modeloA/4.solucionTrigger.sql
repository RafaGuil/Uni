DELIMITER //
-- incluya su solución a continuación
-- Cree un trigger llamado t_asegurar_mismo_tipo_producto_en_pedidos que impida que, a partir de ahora, un mismo pedido incluya productos físicos y digitales.
CREATE OR REPLACE TRIGGER t_asegurar_mismo_tipo_producto_en_pedidos
BEFORE INSERT ON lineaspedido
FOR EACH ROW
BEGIN
    DECLARE tipo_nuevo_producto INT;
    DECLARE tipo_existente INT;

    -- Obtener tipo del producto que se está insertando
    SELECT tipoProductoId INTO tipo_nuevo_producto
    FROM productos
    WHERE id = NEW.productoId;

    -- Verificar si ya existen otros productos en ese pedido
    SELECT tipoProductoId INTO tipo_existente
    FROM productos P
    JOIN lineaspedido LP ON LP.productoId = P.id
    WHERE LP.pedidoId = NEW.pedidoId
    LIMIT 1;

    -- Si ya hay productos en el pedido, y su tipo es distinto al nuevo, lanzar error
   IF tipo_existente IS NOT NULL AND tipo_existente != tipo_nuevo_producto THEN
      SIGNAL SQLSTATE '45000'
      SET MESSAGE_TEXT = 'Un mismo pedido no puede incluir productos físicos y digitales.';
   END IF;

END //

DELIMITER ;

INSERT INTO Pedidos (fechaRealizacion, fechaEnvio, direccionEntrega, comentarios, clienteId, empleadoId) VALUES
('2024-10-01', '2024-10-03', '123 Calle Principal', 'Entregar en la puerta', 1,  1);

INSERT INTO LineasPedido (pedidoId, productoId, unidades, precio) VALUES
(16, 1, 1, 699.99),   -- Smartphone (permitido)
(16, 5, 2, 15.99),    -- Camiseta (permitido)
(16, 3, 1, 9.99);     -- Libro Electrónico (permitido)
