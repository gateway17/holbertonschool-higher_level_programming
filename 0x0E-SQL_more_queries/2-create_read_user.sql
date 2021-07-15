-- Creates database called "hbtn_0d_2"
-- Creates an user and gives "SELECT" previleges
-- on the alluded database.

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2 TO 'user_0d_2'@'localhost';
