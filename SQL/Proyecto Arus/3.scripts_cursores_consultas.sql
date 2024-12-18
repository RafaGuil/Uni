-- Variables globales
SET @pNombrePersona = NULL;
SET @pDepartamento = NULL;
SET @pPalabraTarea = NULL;
SET @pEstado = NULL;

-- R.I.01. Información Tarea
SELECT * FROM Tarea WHERE id = 1;

-- R.I.02. Información persona
SELECT * FROM Persona WHERE id = 2;

-- R.I.03. Información pago
SELECT * FROM Pago WHERE id = 3;

-- R.I.04. Información turno
SELECT * FROM Turno WHERE id = 4;

-- R.I.05. Información asignación
SELECT * FROM Asignacion WHERE id = 5;

-- R.I.06. Filtrado y búsqueda de tareas
SELECT T.* FROM Tarea T
JOIN Asignacion A ON T.asignacionId = A.id
JOIN Persona P ON A.personaId = P.id
WHERE (@pNombrePersona IS NULL OR P.nombre LIKE CONCAT('%', @pNombrePersona, '%'))
  AND (@pPalabraTarea IS NULL OR T.nombre LIKE CONCAT('%', @pPalabraTarea, '%'))
  AND (@pEstado IS NULL OR T.estado = @pEstado);

-- R.I.07. Filtrado y búsqueda de usuarios
SELECT * FROM Persona 
WHERE (@pNombrePersona IS NULL OR nombre LIKE CONCAT('%', @pNombrePersona, '%'))
  AND (@pDepartamento IS NULL OR departamento LIKE CONCAT('%', @pDepartamento, '%'));

-- R.I.08. Filtrado y búsqueda de deudores
SELECT PE.nombre, P.cantidad, P.concepto, P.realizado FROM Pago P
JOIN Persona PE ON P.personaId = PE.id
WHERE (realizado IS FALSE);

-- R.I.09. Facturacion
SELECT SUM(cantidad) FROM pago
