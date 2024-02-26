CREATE TABLE IF NOT EXISTS sales (
    sales_order_number VARCHAR(255) PRIMARY KEY,
    sales_order_line_number INTEGER,
    order_date TIMESTAMP,
    customer_name VARCHAR(255),
    email_address VARCHAR(255),
    item VARCHAR(255),
    quantity INTEGER,
    unit_price DOUBLE PRECISION,
    tax_amount DOUBLE PRECISION
);