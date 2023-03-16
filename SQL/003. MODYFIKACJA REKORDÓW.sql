-- MODYFIKACJA DANYCH W TABELI
-- UPDATE, DELETE

USE sakila;

DESC customer;

SELECT * FROM customer LIMIT 10;

-- UPDATE nazwa tabeli SET co i na co zmieniamy WHERE komu zmieniamy
UPDATE customer SET email = 'mary.smith@gmail.com' WHERE customer_id = 1;

UPDATE customer SET last_name = 'Woodland' WHERE customer_id = 7;

USE zawierzeta; 

CREATE TABLE fastest
(
    animal CHAR(30),
    max_speed INT,
    class CHAR(20)
);


INSERT INTO fastest(animal, max_speed, class)
VALUES
    ("Peregrine falcon", 390, "Flight-diving"),
    ("Golden eagle", 320, "Flight-diving"),
    ("Whitethroated needletail swift", 170, "Flight"),
    ("Eurasian hobby", 160, "Flight"),
    ("Mexican free-tailed bat", 160, "Flight"),
    ("Frigatebird", 153, "Flight"),
    ("Rock dove", 149, "Flight"),
    ("Spur-winged goose", 142, "Flight"),
    ("Black marlin", 129, "Swimming"),
    ("Gyrfalcon", 128, "Flight");
    

SELECT * FROM fastest;

UPDATE fastest SET max_speed = 500 WHERE class = 'Flight';

DELETE FROM fastest WHERE animal = 'Rock dove';

DELETE FROM fastest WHERE class = 'Flight-diving'; 

-- ZADANIE 

USE sakila;
SELECT * FROM customer;

SELECT customer_id, first_name, last_name FROM customer
WHERE first_name = 'Amy' AND last_name = 'Lopez';
-- Wynik customer_id = 32

UPDATE customer SET email = 'Lopez.A@yahoo.com' WHERE customer_id = 32;

SELECT * FROM customer LIMIT 30, 5;

DELETE FROM customer WHERE customer_id = 33;