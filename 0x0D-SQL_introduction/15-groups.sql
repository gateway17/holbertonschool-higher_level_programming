-- lists the number of records with the same score in the table second_table
-- the number of records for this score with the label number

SELECT score AS "score", COUNT(score) AS "number" FROM second_tableb GROUP BY score ORDER BY score DESC;