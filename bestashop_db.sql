-- Uncomment this line if you wish for the script to create the database
-- WARNING: Requires the script to be run with admin privileges
-- CREATE DATABASE IF NOT EXISTS bestashop_db;

-- Replace bestashop_db with the name of your database
USE bestashop_db;

CREATE TABLE categories (
    category_id INT AUTO_INCREMENT,
    name VARCHAR(45),
    PRIMARY KEY (category_id)
);

CREATE TABLE sellers (
    seller_id INT  AUTO_INCREMENT,
    name VARCHAR(45),
    PRIMARY KEY (seller_id)
);

CREATE TABLE products (
    product_id INT AUTO_INCREMENT,
    seller_id INT,
    category_id INT,
    description VARCHAR(512),
    price DECIMAL(10, 2),
    location VARCHAR(100),
    PRIMARY KEY (product_id),
    FOREIGN KEY (seller_id) REFERENCES sellers(seller_id),
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);


CREATE TABLE clients (
    client_id INT AUTO_INCREMENT,
    name VARCHAR(512),
    email VARCHAR(320),
    password VARCHAR(128),
    salt VARCHAR(128),
    PRIMARY KEY (client_id)
);


CREATE VIEW products_full AS
SELECT p.product_id, s.name AS 'seller', c.name AS 'category', p.description, p.price, p.location
  FROM products AS p
  JOIN sellers AS s
    ON p.seller_id = s.seller_id
  JOIN categories AS c
    ON p.category_id = c.category_id;