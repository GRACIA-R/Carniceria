CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT UNIQUE,
    costo_kg REAL,
    precio_kg REAL,
    stock_kg REAL
);

CREATE TABLE IF NOT EXISTS ventas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha TEXT,
    producto_id INTEGER,
    kg REAL,
    total REAL
);

CREATE TABLE IF NOT EXISTS compras (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha TEXT,
    proveedor TEXT,
    kg REAL,
    costo_total REAL
);

CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    telefono TEXT,
    email TEXT,
    tipo TEXT DEFAULT 'general', -- general | mayoreo | especial
    activo INTEGER DEFAULT 1
);

CREATE TABLE IF NOT EXISTS proveedores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    contacto TEXT,
    telefono TEXT,
    email TEXT,
    activo INTEGER DEFAULT 1
);

CREATE TABLE IF NOT EXISTS listas_precios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    descripcion TEXT
);

CREATE TABLE IF NOT EXISTS precios_producto (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    producto_id INTEGER NOT NULL,
    lista_id INTEGER NOT NULL,
    precio REAL NOT NULL,
    FOREIGN KEY (producto_id) REFERENCES productos(id),
    FOREIGN KEY (lista_id) REFERENCES listas_precios(id),
    UNIQUE(producto_id, lista_id)
);

ALTER TABLE clientes ADD COLUMN lista_precio_id INTEGER;

CREATE TABLE IF NOT EXISTS caja (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha TEXT,
    tipo TEXT,
    monto REAL,
    descripcion TEXT
);
