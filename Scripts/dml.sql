/* ======================================================
     PROYECTO FINAL - MANUELA GIRALDO Y SOPHIA MATEUS
     SISTEMA DE GESTIÓN - CLUB DE PILATES Y YOGA 
     DML - Datos de Prueba
   ====================================================== */

SET DEFINE OFF;

-- ══════════════════════════════════════════════
-- 1. MIEMBROS (9 registros)
-- ══════════════════════════════════════════════
INSERT INTO py_miembros (tipo_doc, num_doc, nombre, email, fecha_registro, estado)
VALUES ('CC', '100123456', 'Mariana Alzate', 'alzatemariana@gmail.com', DATE '2026-03-26', 'ACTIVO');

INSERT INTO py_miembros (tipo_doc, num_doc, nombre, email, fecha_registro, estado)
VALUES ('CC', '100234567', 'Juliana Marin', 'juls123@gmail.com', DATE '2026-04-10', 'ACTIVO');

INSERT INTO py_miembros (tipo_doc, num_doc, nombre, email, fecha_registro, estado)
VALUES ('CC', '100789012', 'Sophia Mateus', 'sophiamateus@gmail.com', DATE '2026-05-13', 'ACTIVO');

INSERT INTO py_miembros (tipo_doc, num_doc, nombre, email, fecha_registro, estado)
VALUES ('TI', '105432109', 'Manuela Giraldo', 'manugiraldo@gmail.com', DATE '2026-05-23', 'ACTIVO');

INSERT INTO py_miembros (tipo_doc, num_doc, nombre, email, fecha_registro, estado)
VALUES ('CE', '9876543', 'Salome Espinal', 'salo.esp@gmail.com', DATE '2026-04-15', 'INACTIVO');

INSERT INTO py_miembros (tipo_doc, num_doc, nombre, email, fecha_registro, estado)
VALUES ('CC', '100345678', 'Susana Duque', 'duquelop@gmail.com', DATE '2026-05-20', 'POTENCIAL');

INSERT INTO py_miembros (tipo_doc, num_doc, nombre, email, fecha_registro, estado)
VALUES ('CC', '100456789', 'Luisa Fernanda Sanchez', 'nanda.s@gmail.com', DATE '2026-05-05', 'ACTIVO');

INSERT INTO py_miembros (tipo_doc, num_doc, nombre, email, fecha_registro, estado)
VALUES ('CC', '100567890', 'Maria Alejandra Velasquez', 'malejav@gmail.com', DATE '2026-04-20', 'ACTIVO');

INSERT INTO py_miembros (tipo_doc, num_doc, nombre, email, fecha_registro, estado)
VALUES ('CC', '100678901', 'Mariana Londoño', 'marlon@gmail.com', DATE '2026-05-07', 'ACTIVO');


-- ══════════════════════════════════════════════
-- 2. MEMBRESIAS (7 registros)
-- ══════════════════════════════════════════════
INSERT INTO py_membresias (miembro_id, tipo_pase, valor_pase, fecha_inicio, fecha_corte, estado_pago, saldo_pendiente)
VALUES (1, 'PILATES MENSUAL', 180000, DATE '2026-05-10', DATE '2026-06-09', 'PAGADA', 0);

INSERT INTO py_membresias (miembro_id, tipo_pase, valor_pase, fecha_inicio, fecha_corte, estado_pago, saldo_pendiente)
VALUES (2, 'YOGA MENSUAL', 150000, DATE '2026-05-15', DATE '2026-06-14', 'PAGO PARCIAL', 50000);

INSERT INTO py_membresias (miembro_id, tipo_pase, valor_pase, fecha_inicio, fecha_corte, estado_pago, saldo_pendiente)
VALUES (3, 'PILATES MENSUAL', 180000, DATE '2026-04-15', DATE '2026-05-15', 'NO PAGADA', 180000);

INSERT INTO py_membresias (miembro_id, tipo_pase, valor_pase, fecha_inicio, fecha_corte, estado_pago, saldo_pendiente)
VALUES (8, 'VIP ANUAL', 1600000, DATE '2026-05-20', DATE '2027-05-20', 'PAGADA', 0);

INSERT INTO py_membresias (miembro_id, tipo_pase, valor_pase, fecha_inicio, fecha_corte, estado_pago, saldo_pendiente)
VALUES (9, 'PILATES MENSUAL', 180000, DATE '2026-05-23', DATE '2026-06-22', 'PAGADA', 0);

INSERT INTO py_membresias (miembro_id, tipo_pase, valor_pase, fecha_inicio, fecha_corte, estado_pago, saldo_pendiente)
VALUES (6, 'DAILY PASS', 35000, DATE '2026-05-25', DATE '2026-05-25', 'PAGADA', 0);

INSERT INTO py_membresias (miembro_id, tipo_pase, valor_pase, fecha_inicio, fecha_corte, estado_pago, saldo_pendiente)
VALUES (7, 'CORTESIA', 0, DATE '2026-05-25', DATE '2026-05-25', 'PAGADA', 0);


-- ══════════════════════════════════════════════
-- 3. CLASES (5 registros)
-- ══════════════════════════════════════════════
INSERT INTO py_clases (disciplina, fecha_clase, horario, cupo_maximo, cargo_inasist)
VALUES ('REFORMER PILATES', DATE '2026-05-20', '07:00-08:00', 10, 15000);

INSERT INTO py_clases (disciplina, fecha_clase, horario, cupo_maximo, cargo_inasist)
VALUES ('HOT YOGA', DATE '2026-05-23', '18:30-19:30', 15, 12000);

INSERT INTO py_clases (disciplina, fecha_clase, horario, cupo_maximo, cargo_inasist)
VALUES ('MAT PILATES', DATE '2026-05-25', '08:00-09:00', 12, 15000);

INSERT INTO py_clases (disciplina, fecha_clase, horario, cupo_maximo, cargo_inasist)
VALUES ('PUPPY YOGA', DATE '2026-05-26', '10:00-11:00', 8, 20000);

INSERT INTO py_clases (disciplina, fecha_clase, horario, cupo_maximo, cargo_inasist)
VALUES ('MAT YOGA', DATE '2026-05-28', '06:00-07:00', 20, 10000);


-- ══════════════════════════════════════════════
-- 4. INSCRIPCIONES (6 registros)
-- ══════════════════════════════════════════════
INSERT INTO py_inscripciones (miembro_id, clase_id, fecha_registro, estado_asist)
VALUES (1, 1, DATE '2026-05-19', 'ASISTIÓ');

INSERT INTO py_inscripciones (miembro_id, clase_id, fecha_registro, estado_asist)
VALUES (2, 2, DATE '2026-05-22', 'NO ASISTIÓ');

INSERT INTO py_inscripciones (miembro_id, clase_id, fecha_registro, estado_asist)
VALUES (3, 3, DATE '2026-05-19', 'NO ASISTIÓ');

INSERT INTO py_inscripciones (miembro_id, clase_id, fecha_registro, estado_asist)
VALUES (4, 8, DATE '2026-05-24', 'ASISTIÓ');

INSERT INTO py_inscripciones (miembro_id, clase_id, fecha_registro, estado_asist)
VALUES (5, 4, DATE '2026-05-25', 'RESERVADO');

INSERT INTO py_inscripciones (miembro_id, clase_id, fecha_registro, estado_asist)
VALUES (6, 5, DATE '2026-05-24', 'RESERVADO');


-- ══════════════════════════════════════════════
-- 5. PAGOS (4 registros)
-- ══════════════════════════════════════════════
INSERT INTO py_pagos (membresia_id, fecha_pago, monto_pago, canal_pago, referencia)
VALUES (1, DATE '2026-05-10', 180000, 'TRANSFERENCIA', 'TRF-MARI001');

INSERT INTO py_pagos (membresia_id, fecha_pago, monto_pago, canal_pago, referencia)
VALUES (2, DATE '2026-05-15', 100000, 'TARJETA', 'TC-JULI002');

INSERT INTO py_pagos (membresia_id, fecha_pago, monto_pago, canal_pago, referencia)
VALUES (4, DATE '2026-05-20', 1600000, 'TRANSFERENCIA', 'PSE-SOPHIA03');

INSERT INTO py_pagos (membresia_id, fecha_pago, monto_pago, canal_pago, referencia)
VALUES (5, DATE '2026-05-23', 180000, 'TRANSFERENCIA', 'PSE-MANU004');

COMMIT;
