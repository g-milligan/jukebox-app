create database mydb_example;

\c mydb_example;

CREATE TABLE IF NOT EXISTS animal (
    animal_id               serial primary key,
    animal_display_name     varchar(255),
    animal_key              varchar(255) unique not null, 
    animal_age              integer,
    animal_is_friendly      boolean,
    animal_created_at       timestamp not null,
    animal_modified_at      timestamp not null
);

CREATE TYPE vore_type AS ENUM ('Unknown', 'Carnivore', 'Herbivore', 'Omnivore');

CREATE TABLE IF NOT EXISTS species (
    species_id              serial primary key,
    species_display_name    varchar(255),
    species_key             varchar(255) unique not null, 
    species_vore_type       vore_type,
    species_created_at      timestamp not null,
    species_modified_at     timestamp not null
);

CREATE TABLE IF NOT EXISTS animal_species (
    animal_species_id               serial primary key,
    fk_species_id                   integer references species(species_id),
    fk_animal_id                    integer references animal(animal_id),
    animal_species_created_at       timestamp not null,
    animal_species_modified_at      timestamp not null
);