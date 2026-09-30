-- SQLite: example for an empty, isolated test database; not a production migration.
-- Demonstrates referential integrity across tenants, NOT authorization or RLS.
-- Money uses integer minor units; the domain must define currency scale.
PRAGMA foreign_keys = ON;

CREATE TABLE tenants (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL CHECK (length(trim(name)) > 0)
);
CREATE TABLE customers (
    tenant_id INTEGER NOT NULL,
    id INTEGER NOT NULL,
    display_name TEXT NOT NULL CHECK (length(trim(display_name)) > 0),
    PRIMARY KEY (tenant_id, id),
    FOREIGN KEY (tenant_id) REFERENCES tenants(id) ON DELETE RESTRICT
);
CREATE TABLE products (
    tenant_id INTEGER NOT NULL,
    id INTEGER NOT NULL,
    sku TEXT NOT NULL CHECK (length(trim(sku)) > 0),
    PRIMARY KEY (tenant_id, id),
    UNIQUE (tenant_id, sku),
    FOREIGN KEY (tenant_id) REFERENCES tenants(id) ON DELETE RESTRICT
);
CREATE TABLE orders (
    tenant_id INTEGER NOT NULL,
    id INTEGER NOT NULL,
    customer_id INTEGER NOT NULL,
    currency TEXT NOT NULL CHECK (length(currency) = 3 AND currency NOT GLOB '*[^A-Z]*'),
    status TEXT NOT NULL DEFAULT 'draft' CHECK (status IN ('draft', 'confirmed', 'cancelled')),
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (tenant_id, id),
    FOREIGN KEY (tenant_id, customer_id) REFERENCES customers(tenant_id, id) ON DELETE RESTRICT
);
CREATE TABLE order_items (
    tenant_id INTEGER NOT NULL,
    order_id INTEGER NOT NULL,
    line_no INTEGER NOT NULL CHECK (typeof(line_no) = 'integer' AND line_no > 0),
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL CHECK (typeof(quantity) = 'integer' AND quantity > 0),
    unit_price_minor INTEGER NOT NULL CHECK (typeof(unit_price_minor) = 'integer' AND unit_price_minor >= 0),
    PRIMARY KEY (tenant_id, order_id, line_no),
    FOREIGN KEY (tenant_id, order_id) REFERENCES orders(tenant_id, id) ON DELETE RESTRICT,
    FOREIGN KEY (tenant_id, product_id) REFERENCES products(tenant_id, id) ON DELETE RESTRICT
);
-- Query: latest orders for one customer within its tenant.
CREATE INDEX orders_by_customer_time ON orders(tenant_id, customer_id, created_at, id);
-- Supports product FK checks and reverse lookup; order lookup is supported by the PK.
CREATE INDEX order_items_by_product ON order_items(tenant_id, product_id);
