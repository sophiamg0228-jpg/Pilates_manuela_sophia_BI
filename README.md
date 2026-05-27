# 🧘 Club de Pilates & Yoga — Sistema de Gestión

## 📋 Descripción del Sistema

Sistema de gestión integral para un club de Pilates y Yoga que permite administrar miembros, membresías, clases, inscripciones y pagos. La aplicación está desarrollada en **Streamlit** con conexión a **Oracle Cloud (Autonomous Database)**, ofreciendo una interfaz moderna para la consulta y registro de datos en tiempo real.

---

## 👥 Integrantes

| Nombre | Rol |
|--------|-----|
| Manuela Giraldo | Diseño de base de datos, DDL/DML, restricciones |
| Sophia Mateus | Aplicación Streamlit, conexión Oracle, documentación |

---

## 🏢 Dominio Elegido y Justificación

Se eligió el dominio de un **club de Pilates y Yoga** porque representa un negocio real con reglas de operación claras y variadas:

- Los miembros pueden tener diferentes estados (activo, inactivo, potencial).
- Existen múltiples tipos de membresía con precios y vigencias distintas (Pilates Mensual, Yoga Mensual, VIP Anual, Daily Pass, Cortesía).
- Las clases tienen cupos limitados y diferentes disciplinas (Reformer Pilates, Mat Pilates, Mat Yoga, Hot Yoga, Puppy Yoga).
- Las inscripciones controlan asistencia y evitan duplicados.
- Los pagos se asocian a membresías con control de saldo pendiente y múltiples canales.

Este dominio permite implementar restricciones NOT NULL, UNIQUE, CHECK y de integridad referencial de forma natural y justificada por la lógica del negocio.

---

## 📊 Diagrama Entidad-Relación (ERD)

```
┌──────────────────────┐
│     PY_MIEMBROS      │
├──────────────────────┤
│ PK miembro_id        │
│    tipo_doc       NOT NULL
│    num_doc        NOT NULL   ── UNIQUE(tipo_doc, num_doc)
│    nombre         NOT NULL
│    email
│    fecha_registro NOT NULL
│    estado         NOT NULL   ── CHECK (ACTIVO, INACTIVO, POTENCIAL)
└──────────┬───────────┘
           │ 1
           │
           │ N
┌──────────┴───────────┐         ┌──────────────────────┐
│    PY_MEMBRESIAS     │         │    PY_INSCRIPCIONES   │
├──────────────────────┤         ├───────────────────────┤
│ PK membresia_id      │         │ PK inscripcion_id     │
│ FK miembro_id        │         │ FK miembro_id         │◄── PY_MIEMBROS
│    tipo_pase  NOT NULL│        │ FK clase_id           │◄── PY_CLASES
│    valor_pase NOT NULL│        │    fecha_registro     │
│    fecha_inicio      │         │    estado_asist       │── CHECK
│    fecha_corte       │         │    UNIQUE(miembro_id, clase_id)
│    estado_pago       │         └───────────────────────┘
│    saldo_pendiente   │
└──────────┬───────────┘
           │ 1
           │
           │ N
┌──────────┴───────────┐         ┌──────────────────────┐
│      PY_PAGOS        │         │      PY_CLASES       │
├──────────────────────┤         ├──────────────────────┤
│ PK pago_id           │         │ PK clase_id          │
│ FK membresia_id      │         │    disciplina  NOT NULL ── CHECK
│    fecha_pago        │         │    fecha_clase NOT NULL
│    monto_pago NOT NULL│        │    horario    NOT NULL
│    canal_pago NOT NULL│        │    cupo_maximo NOT NULL ── CHECK > 0
│    referencia        │         │    cargo_inasist      ── CHECK >= 0
└──────────────────────┘         └──────────────────────┘
```

### Relaciones

- **PY_MIEMBROS → PY_MEMBRESIAS**: Un miembro puede tener muchas membresías (1:N)
- **PY_MIEMBROS → PY_INSCRIPCIONES**: Un miembro puede inscribirse a muchas clases (1:N)
- **PY_CLASES → PY_INSCRIPCIONES**: Una clase puede tener muchas inscripciones (1:N)
- **PY_MEMBRESIAS → PY_PAGOS**: Una membresía puede tener muchos pagos (1:N)

---

## 📑 Descripción de Tablas y Restricciones

### 1. PY_MIEMBROS
Almacena la información personal de cada miembro del club.

| Columna | Tipo | Restricción | Justificación |
|---------|------|-------------|---------------|
| miembro_id | NUMBER (IDENTITY) | PK | Identificador único auto-generado |
| tipo_doc | VARCHAR2(5) | NOT NULL | Todo miembro debe tener tipo de documento |
| num_doc | VARCHAR2(20) | NOT NULL, UNIQUE(tipo_doc, num_doc) | Evita duplicar miembros con el mismo documento |
| nombre | VARCHAR2(50) | NOT NULL | El nombre es obligatorio para identificación |
| email | VARCHAR2(50) | — | Opcional, no todos los miembros lo proporcionan |
| fecha_registro | DATE | NOT NULL, DEFAULT SYSDATE | Registro automático de la fecha de ingreso |
| estado | VARCHAR2(15) | NOT NULL, CHECK | Solo permite ACTIVO, INACTIVO o POTENCIAL |

### 2. PY_MEMBRESIAS
Registra las membresías adquiridas por los miembros con su tipo, valor y estado de pago.

| Columna | Tipo | Restricción | Justificación |
|---------|------|-------------|---------------|
| membresia_id | NUMBER (IDENTITY) | PK | Identificador único auto-generado |
| miembro_id | NUMBER | FK → PY_MIEMBROS, NOT NULL | Toda membresía pertenece a un miembro |
| tipo_pase | VARCHAR2(30) | NOT NULL, CHECK | Solo permite los 5 tipos definidos por el negocio |
| valor_pase | NUMBER(10,2) | NOT NULL, CHECK >= 0 | El valor no puede ser negativo |
| fecha_inicio | DATE | NOT NULL | Se necesita saber cuándo inicia la membresía |
| fecha_corte | DATE | NOT NULL | Fecha de vencimiento para control de vigencia |
| estado_pago | VARCHAR2(20) | NOT NULL, CHECK | Solo PAGADA, PAGO PARCIAL o NO PAGADA |
| saldo_pendiente | NUMBER(10,2) | NOT NULL, CHECK >= 0 | Controla cuánto debe el miembro |

### 3. PY_CLASES
Contiene la programación de clases con disciplina, horario y capacidad.

| Columna | Tipo | Restricción | Justificación |
|---------|------|-------------|---------------|
| clase_id | NUMBER (IDENTITY) | PK | Identificador único auto-generado |
| disciplina | VARCHAR2(20) | NOT NULL, CHECK | Solo las 5 disciplinas que ofrece el club |
| fecha_clase | DATE | NOT NULL | Toda clase debe tener fecha programada |
| horario | VARCHAR2(15) | NOT NULL | Horario obligatorio para la agenda |
| cupo_maximo | NUMBER(2) | NOT NULL, CHECK > 0 | Debe haber al menos 1 cupo disponible |
| cargo_inasist | NUMBER(10,2) | NOT NULL, CHECK >= 0 | Penalización por no asistir, no puede ser negativa |

### 4. PY_INSCRIPCIONES
Registra la inscripción de un miembro a una clase específica.

| Columna | Tipo | Restricción | Justificación |
|---------|------|-------------|---------------|
| inscripcion_id | NUMBER (IDENTITY) | PK | Identificador único auto-generado |
| miembro_id | NUMBER | FK → PY_MIEMBROS, NOT NULL | Toda inscripción pertenece a un miembro |
| clase_id | NUMBER | FK → PY_CLASES, NOT NULL | Toda inscripción es para una clase |
| fecha_registro | DATE | NOT NULL, DEFAULT SYSDATE | Registro automático de la fecha |
| estado_asist | VARCHAR2(20) | NOT NULL, CHECK | Solo RESERVADO, ASISTIÓ o NO ASISTIÓ |
| — | — | UNIQUE(miembro_id, clase_id) | Evita que un miembro se inscriba dos veces a la misma clase |

### 5. PY_PAGOS
Registra los pagos realizados contra una membresía.

| Columna | Tipo | Restricción | Justificación |
|---------|------|-------------|---------------|
| pago_id | NUMBER (IDENTITY) | PK | Identificador único auto-generado |
| membresia_id | NUMBER | FK → PY_MEMBRESIAS, NOT NULL | Todo pago corresponde a una membresía |
| fecha_pago | DATE | NOT NULL | Se necesita la fecha para auditoría |
| monto_pago | NUMBER(12,2) | NOT NULL, CHECK >= 0 | El monto no puede ser negativo |
| canal_pago | VARCHAR2(30) | NOT NULL, DEFAULT 'TRANSFERENCIA' | Canal por defecto si no se especifica |
| referencia | VARCHAR2(50) | — | Opcional, referencia bancaria del pago |

---

## 🔐 Reglas de Negocio Implementadas

| # | Regla de Negocio | Implementación | Tabla |
|---|------------------|----------------|-------|
| 1 | No puede haber dos miembros con el mismo tipo y número de documento | UNIQUE (tipo_doc, num_doc) | PY_MIEMBROS |
| 2 | Un miembro solo puede estar en estado ACTIVO, INACTIVO o POTENCIAL | CHECK (estado IN (...)) | PY_MIEMBROS |
| 3 | Solo se permiten los tipos de membresía definidos por el club | CHECK (tipo_pase IN (...)) | PY_MEMBRESIAS |
| 4 | El valor de una membresía no puede ser negativo | CHECK (valor_pase >= 0) | PY_MEMBRESIAS |
| 5 | El saldo pendiente nunca puede ser negativo | CHECK (saldo_pendiente >= 0) | PY_MEMBRESIAS |
| 6 | Solo se ofrecen las 5 disciplinas del club | CHECK (disciplina IN (...)) | PY_CLASES |
| 7 | Toda clase debe tener al menos 1 cupo | CHECK (cupo_maximo > 0) | PY_CLASES |
| 8 | El cargo por inasistencia no puede ser negativo | CHECK (cargo_inasist >= 0) | PY_CLASES |
| 9 | Un miembro no puede inscribirse dos veces a la misma clase | UNIQUE (miembro_id, clase_id) | PY_INSCRIPCIONES |
| 10 | La asistencia solo puede ser RESERVADO, ASISTIÓ o NO ASISTIÓ | CHECK (estado_asist IN (...)) | PY_INSCRIPCIONES |
| 11 | El monto de un pago no puede ser negativo | CHECK (monto_pago >= 0) | PY_PAGOS |
| 12 | Todo pago debe estar asociado a una membresía válida | FK membresia_id → PY_MEMBRESIAS | PY_PAGOS |

---

## 🚀 Instrucciones para Ejecutar la Aplicación

### Prerrequisitos

- Python 3.9 o superior
- Oracle Instant Client instalado
- Wallet de Oracle Cloud (`wallet_ADBG06`)

### Pasos

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/TU_USUARIO/proyecto-pilates-yoga.git
   cd proyecto-pilates-yoga
   ```

2. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configurar credenciales:**
   
   Crear un archivo `.env` en la raíz del proyecto con el siguiente contenido:
   ```
   ORACLE_USER=TU_USUARIO
   ORACLE_PASSWORD=TU_CONTRASEÑA
   ORACLE_DSN=adbg06_low
   WALLET_DIR=C:/ruta/a/tu/wallet_ADBG06
   WALLET_PASSWORD=TU_WALLET_PASSWORD
   ```

4. **Ejecutar los scripts SQL** (si es la primera vez):
   - Ejecutar `scripts/ddl.sql` para crear las tablas
   - Ejecutar `scripts/dml.sql` para insertar los datos de prueba

5. **Iniciar la aplicación:**
   ```bash
   streamlit run app/app.py
   ```

6. La app se abrirá automáticamente en `http://localhost:8501`

---

## 📸 Capturas de Pantalla

> *Agregar capturas de pantalla de la aplicación en funcionamiento una vez esté corriendo.*

| Sección | Descripción |
|---------|-------------|
| Dashboard | Vista general con métricas y membresías pendientes |
| Miembros | Lista filtrable por estado |
| Clases | Clases disponibles con cupos en tiempo real |
| Inscripciones | Registro de inscripciones a clases |
| Formulario | Registro de nuevos miembros |

---

## 💭 Reflexión del Equipo

### Dificultades Encontradas
- Configuración inicial de la wallet y conexión a Oracle Cloud desde Python.
- Manejo de permisos entre usuarios de la base de datos para que ambas integrantes pudieran trabajar simultáneamente.
- Coordinación del trabajo en paralelo: una persona en SQL y otra en Streamlit, asegurando que los nombres de tablas y columnas coincidieran.

### Aprendizajes
- La importancia de diseñar el modelo de datos antes de escribir código — el diagrama ERD nos ahorró muchos errores.
- El uso de variables de entorno para proteger credenciales es una práctica esencial en cualquier proyecto real.
- Streamlit facilita enormemente la creación de interfaces web conectadas a bases de datos sin necesidad de conocimientos avanzados de frontend.
- El trabajo colaborativo con GitHub permite que cada integrante aporte desde su máquina sin pisar el trabajo de la otra.

---

*Proyecto Final — BI para Decisiones Estratégicas · 2026-I*
