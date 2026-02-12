CREATE DATABASE IF NOT EXISTS bestashop_db;
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


SELECT * FROM products;