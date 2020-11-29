-- Database table info goes here

DROP TABLE IF EXISTS wizards;

CREATE TABLE wizards (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    age INT
);
