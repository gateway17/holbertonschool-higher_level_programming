-- Creates a database called "hbtn_0d_usa",
-- Craetes a table called "cities" in the alluded database with:
-- 

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
state_id INT NOT NULL FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id),
'name' VARCHAR(256)NOT NULL);
