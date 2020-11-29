-- Database table info goes here
DROP TABLE IF EXISTS casts;
DROP TABLE IF EXISTS spells;
DROP TABLE IF EXISTS wizards;
DROP TABLE IF EXISTS locations;

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

CREATE TABLE spells (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description VARCHAR(255),
    wizard INT REFERENCES wizards(id)
);

CREATE TABLE casts (
    id SERIAL PRIMARY KEY,
    deaths INT,
    details VARCHAR(255),
    wizard_id INT REFERENCES wizards(id),
    location_id INT REFERENCES locations(id),
    spell_id INT REFERENCES spells(id)
);