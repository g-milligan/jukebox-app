\c mydb_example

INSERT INTO species(
    species_display_name, 
    species_key, 
    species_vore_type, 
    species_created_at, 
    species_modified_at
)
VALUES 
(
    'Squirrel',
    'squirrel',
    'Omnivore',
    current_timestamp,
    current_timestamp
),
(
    'Fox',
    'fox',
    'Omnivore',
    current_timestamp,
    current_timestamp
),
(
    'Lion',
    'lion',
    'Carnivore',
    current_timestamp,
    current_timestamp
),
(
    'Kitty',
    'cat',
    'Carnivore',
    current_timestamp,
    current_timestamp
),
(
    'Elephant',
    'nuffy',
    'Herbivore',
    current_timestamp,
    current_timestamp
);

SELECT * FROM species;

INSERT INTO animal(
    animal_display_name,
    animal_key,
    animal_age,
    animal_is_friendly,
    animal_created_at,
    animal_modified_at
)
VALUES 
(
    'Jerry',
    'jerry',
    16,
    false,
    current_timestamp,
    current_timestamp
),
(
    'Wilkinson Jimbo',
    'whyjimmy',
    44,
    true,
    current_timestamp,
    current_timestamp
),
(
    'Smifton Wuppledump',
    'smiffit',
    4,
    false,
    current_timestamp,
    current_timestamp
),
(
    'Tippy',
    'formerlylumpy',
    null,
    true,
    current_timestamp,
    current_timestamp
),
(
    'Clever Fred',
    'cled',
    90,
    false,
    current_timestamp,
    current_timestamp
),
(
    'Leon Regalion',
    'leonr',
    33,
    true,
    current_timestamp,
    current_timestamp
),
(
    'Noof Noof',
    'noofie',
    1030,
    false,
    current_timestamp,
    current_timestamp
);

SELECT * FROM animal;

INSERT INTO animal_species(
    fk_species_id,
    fk_animal_id,
    animal_species_created_at,
    animal_species_modified_at
)
VALUES
( 1, 1, current_timestamp, current_timestamp ),
( 1, 2, current_timestamp, current_timestamp ),
( 4, 3, current_timestamp, current_timestamp ),
( 1, 4, current_timestamp, current_timestamp ),
( 2, 5, current_timestamp, current_timestamp ),
( 3, 6, current_timestamp, current_timestamp ),
( 5, 7, current_timestamp, current_timestamp );

SELECT fk_species_id, fk_animal_id FROM animal_species;