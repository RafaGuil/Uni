-- 2.1
SELECT UE.nombre, PE.fechaRealizacion, UC.nombre FROM pedidos PE
LEFT JOIN empleados E ON PE.empleadoId = E.id
LEFT JOIN usuarios UE ON E.usuarioId = UE.id
LEFT JOIN clientes C ON PE.clienteId = C.id
LEFT JOIN usuarios UC ON C.usuarioId = UC.id
WHERE MONTH(PE.fechaRealizacion) = MONTH(CURDATE())
	AND YEAR(PE.fechaRealizacion) = YEAR(CURDATE());




-- 2.2
SELECT U.nombre, SUM(LP.unidades), SUM(LP.unidades*LP.precio) FROM lineaspedido LP
LEFT JOIN pedidos P ON LP.pedidoId = P.id
LEFT JOIN clientes C ON P.clienteId = C.id
LEFT JOIN usuarios U ON C.usuarioId = U.id
GROUP BY U.id
HAVING COUNT(P.id) > 5;