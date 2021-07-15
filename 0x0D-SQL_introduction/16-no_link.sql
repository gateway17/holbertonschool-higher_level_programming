-- lists all records of the table second_table
-- Resturn the score and name in desending order

SELECT score, name FROM second_table WHERE name IS NOT NULL
ORDER BY score DESC;