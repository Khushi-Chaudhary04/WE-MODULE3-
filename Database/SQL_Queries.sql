-- Table: Pokemon
CREATE TABLE Pokemon (
    pokemon_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    primary_type VARCHAR(20) NOT NULL,
    secondary_type VARCHAR(20),
    UNIQUE(name)
);

-- Table: Move
CREATE TABLE Move (
    move_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    power INT NOT NULL,
    type VARCHAR(20) NOT NULL,
    UNIQUE(name)
);

-- Table: Pokemon_Move
CREATE TABLE Pokemon_Move (
    pokemon_id INT REFERENCES Pokemon(pokemon_id),
    move_id INT REFERENCES Move(move_id),
    PRIMARY KEY (pokemon_id, move_id)
);

-- Inserting Pokemon
INSERT INTO Pokemon (name, primary_type, secondary_type) VALUES
('Bulbasaur', 'Grass', NULL),
('Charmander', 'Fire', NULL),
('Squirtle', 'Water', NULL),
('Eevee', 'Normal', NULL),
('Pidgey', 'Normal', 'Flying');

-- Inserting Moves
INSERT INTO Move (name, power, type) VALUES
('Tackle', 35, 'Normal'),
('Water Gun', 40, 'Water'),
('Ember', 40, 'Fire'),
('Vine Whip', 40, 'Grass'),
('Wing Attack', 65, 'Flying'),
('Headbutt', 70, 'Normal'),
('Return', 100, 'Normal');

-- Inserting Pokemon-Move relationships
INSERT INTO Pokemon_Move (pokemon_id, move_id) VALUES
(1, 1), (1, 4), (1, 7),
(2, 1), (2, 3), (2, 7),
(3, 1), (3, 2), (3, 7),
(4, 1), (4, 6), (4, 7),
(5, 1), (5, 5), (5, 7);

-- Query to return all the Pokémon who can learn 'Return':
SELECT p.name
FROM Pokemon p
INNER JOIN Pokemon_Move pm ON p.pokemon_id = pm.pokemon_id
INNER JOIN Move m ON pm.move_id = m.move_id
WHERE m.name = 'Return';

-- Query to return all the moves in the game that are powerful against Grass:
SELECT m.name
FROM Move m
WHERE m.type IN ('Fire', 'Flying') OR
      (m.type = 'Water' AND NOT EXISTS (SELECT 1 FROM Move WHERE type = 'Grass'));

--Now if we consider  that mostly only the pokemon type matters, because if a weaker type pokemon is against a stronger one, its power value is halved and doubled if vice versa.

-- Query to return all the moves in the game that are powerful against Grass:
SELECT m.name,
       CASE
           WHEN m.type = 'Fire' THEN m.power * 2
           WHEN m.type = 'Flying' THEN m.power * 2
           ELSE m.power
       END AS effective_power
FROM Move m
WHERE m.type IN ('Fire', 'Flying') OR
      (m.type = 'Water' AND NOT EXISTS (SELECT 1 FROM Move WHERE type = 'Grass'));

-- Query to return all the Pokémon who can learn 'Return':
SELECT p.name
FROM Pokemon p
JOIN Pokemon_Move pm ON p.pokemon_id = pm.pokemon_id
JOIN Move m ON pm.move_id = m.move_id
WHERE m.name = 'Return';
