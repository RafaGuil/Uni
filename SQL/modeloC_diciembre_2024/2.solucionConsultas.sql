-- 2.1
-- Ordenado por unidades y, a igualdad de unidades, por precio unitario
SELECT PR.nombre, PR.precio, LP.unidades FROM lineaspedido LP
JOIN productos PR ON LP.pedidoId = PR.id
ORDER BY LP.unidades DESC, PR.precio DESC
LIMIT 5;


-- 2.3
SELECT U.nombre, P.fechaRealizacion, 
SUM(LP.precio * LP.unidades), SUM(LP.unidades)
FROM lineaspedido LP
JOIN pedidos P ON LP.pedidoId = P.id 
LEFT JOIN empleados E ON P.empleadoId = E.id
LEFT JOIN usuarios U ON E.usuarioId = U.id
WHERE P.fechaRealizacion < CURDATE() - INTERVAL 7 DAY
GROUP BY P.id;
-- Agrupamos solo por P.Id ya que nos dice "para todos los pedidos"

-- LEFT JOIN TE RELLENA CON NULL LOS DATOS NO EXISTENTES DE LA TABLA DERECHA
-- RIGHT JOIN LO MISMO QUE LEFT JOIN PERO AL REVÉS
-- JOIN SOLO COGE DATOS QUE NO HAYA NULL NI A IZQ NI A DER

-- WHERE filtra filas individuales antes de agrupar
-- HAVING filtra grupos después de agrupar

-- SELECT ...
-- FROM ...
-- JOIN ...
-- WHERE ...
-- GROUP BY ...
-- HAVING ...
-- ORDER BY ...
-- LIMIT ...
