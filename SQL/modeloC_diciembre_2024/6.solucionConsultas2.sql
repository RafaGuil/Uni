-- 1. Consultas básicas de selección
-- Lista todos los usuarios en la tabla `Usuarios`, mostrando solo sus nombres y correos electrónicos.
SELECT U.nombre, U.email FROM usuarios U;

-- Muestra los empleados con su salario y el nombre correspondiente en la tabla `Usuarios`.
SELECT U.nombre, E.salario FROM usuarios U JOIN empleados E ON U.id = E.usuarioId;

-- Obtén los productos de la tabla `Productos` que tienen un precio mayor o igual a 20.00.
SELECT P.* FROM productos P WHERE P.precio >= 20.00;

-- Lista los clientes con su dirección de envío, código postal y fecha de nacimiento.
SELECT C.direccionEnvio, C.codigoPostal, C.fechaNacimiento FROM clientes C;

-- 2. Consultas con condiciones específicas y funciones agregadas
-- Encuentra el salario promedio de los empleados.
SELECT AVG(E.salario) FROM empleados E;

-- Obtén el número total de productos agrupados por tipo de producto.
SELECT T.nombre, COUNT(P.id) FROM productos P JOIN tiposproducto T ON P.tipoProductoId = T.id GROUP BY T.nombre;

-- Lista los pedidos realizados por cada cliente con su nombre y la fecha de realización.
SELECT U.nombre, P.fechaRealizacion FROM usuarios U 
JOIN clientes C ON U.id = C.id
JOIN pedidos P ON C.id = P.clienteId
ORDER BY C.id ASC;

-- Cliente que ha pedido la menor variedad de productos.
SELECT U.nombre, COUNT(DISTINCT P.id) AS distintosProductos FROM usuarios U 
JOIN clientes C ON U.id = C.usuarioId
JOIN pedidos PE ON C.id = PE.clienteId
JOIN lineaspedido LP ON PE.id = LP.pedidoId
JOIN productos P ON LP.productoId = P.id
GROUP BY C.id
ORDER BY COUNT(DISTINCT P.id) ASC
LIMIT 1;

-- Top 3 clientes adultos que más han gastado (mínimo 100), comprando productos aptos para menores y
-- atendidos por empleados bien pagados o sin asignación de empleado.
SELECT C.id AS clienteId, U.nombre AS clienteNombre, COUNT(DISTINCT LP.productoId) AS distintosProductos,
SUM(LP.unidades*LP.precio) AS totalGastado, AVG(LP.precio) AS precioMedio
FROM Usuarios U
JOIN Clientes C ON U.id=C.usuarioId
JOIN Pedidos PE ON C.id=PE.clienteId
JOIN LineasPedido LP ON PE.id=LP.pedidoId
JOIN Productos P ON LP.productoId=P.id
JOIN TiposProducto TP ON P.tipoProductoId=TP.id
LEFT JOIN Empleados E ON PE.empleadoId=E.id
WHERE C.fechaNacimiento<=DATE_SUB(CURDATE(),INTERVAL 18 YEAR)
  AND (E.salario>3000 OR E.salario IS NULL)
  AND P.puedeVenderseAMenores=TRUE
GROUP BY C.id, U.nombre
HAVING SUM(LP.unidades*LP.precio)>100
ORDER BY totalGastado DESC, distintosProductos DESC
LIMIT 3;

-- 3. Consultas con JOIN y filtrado avanzado
-- Encuentra los pedidos realizados por clientes mayores de edad (18 años o más).
