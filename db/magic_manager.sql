-- Database table info goes here

DROP TABLE IF EXISTS wizards;
DROP TABLE IF EXISTS locations;
DROP TABLE IF EXISTS spells;

CREATE TABLE wizards (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    age INT
);

CREATE TABLE locations (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    type VARCHAR(255),
    realm VARCHAR(255)
);

