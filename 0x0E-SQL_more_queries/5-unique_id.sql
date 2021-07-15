-- Creates table "unique_id" with a default id=1, and unique!

CREATE TABLE IF NOT EXISTS unique_id(id INT SET DEFAULT 1 UNIQUE,
'name' VARCHAR(256));
