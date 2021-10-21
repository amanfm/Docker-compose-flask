CREATE DATABASE aman;
use aman;

CREATE TABLE full_name (
  first_name VARCHAR(20),
  last_name VARCHAR(10)
);

INSERT INTO full_name
  (first_name, last_name)
VALUES
  ('aman', 'shah'),
  ('kaustav', 'bora');