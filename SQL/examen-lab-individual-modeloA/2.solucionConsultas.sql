-- 2.1
SELECT P.nombre AS nombreProducto, TP.nombre AS tipoProducto, P.precio 
FROM productos P
JOIN tiposproducto TP ON P.tipoProductoId = TP.id
WHERE TP.nombre = 'Digitales';

-- 2.2
SELECT 
  U.nombre AS empleado,
  COUNT(DISTINCT P.id) AS num_pedidos_mayores_500,
  COALESCE(SUM(P.total), 0) AS importe_total_gestionado
FROM Empleados E
LEFT JOIN Usuarios U ON U.id = E.usuarioId
LEFT JOIN (
  SELECT 
    Pe.id,
    Pe.empleadoId,
    SUM(LP.precio * LP.unidades) AS total
  FROM Pedidos Pe
  JOIN LineasPedido LP ON LP.pedidoId = Pe.id
  WHERE YEAR(Pe.fechaRealizacion) = YEAR(CURDATE())
  GROUP BY Pe.id
  HAVING total > 500
) P ON P.empleadoId = E.id
GROUP BY U.nombre
ORDER BY importe_total_gestionado DESC;