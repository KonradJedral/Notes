-- WYBIERANIE REKORDÓW 
-- SELECT, LIMIT, WHERE, =, <, >, !=, <=, >=, ALIASY

USE sakila;

SELECT * FROM film;
DESC film;

-- Wyświetlamy całe dwie kolumny 
SELECT title, release_year FROM film;

-- Wyświetlamy całe trzy kolumny
SELECT title, length, rating FROM film; 

-- Wyświetlamy ograniczoną ilość rekordów  
SELECT title, length FROM film LIMIT 10;

-- Wyświetlamy od podanej pozycji (+1 - podana pozycja nie zostanie wyświetlona) i po przecinku ile rekordów ma być wyświetlonych
SELECT length, title FROM film LIMIT 150, 20;    

-- Te które mają Rating General  'G'
SELECT title, rating FROM film
WHERE rating = 'G';

-- Te które mają długość większą niż 120 
SELECT title, length FROM film 
WHERE length > 120;

-- Te które mają długość = 130 
SELECT title, length FROM film 
WHERE length = 130;

-- Te które mają długość inną niż 130 
SELECT title, length FROM film 
WHERE length != 130;

-- Możemy wykorzystywać kolumny do filtrowania pomimo, że nie chcemy ich wyświetlać
SELECT title FROM film 
WHERE length = 150; 

-- Możemy łączyć warunki 
SELECT title FROM film 
WHERE length = 165
LIMIT 3; 

-- ZADANIA

SELECT title, rating FROM film;

SELECT title FROM film
LIMIT 980, 20;

SELECT title, rating FROM film
WHERE rating = 'g';

SELECT title, length, rental_rate FROM film
WHERE rating = 'PG-13' 
LIMIT 20;

-- ALIASY - przypisanie innych nazw kolumn niż oryginalne

SELECT 
	title AS 'Tytuł filmu', 
    release_year AS 'Rok wydania',
    length AS 'Długość filmu',
    rental_duration AS 'Czas Wypożyczenia',
    rental_rate AS 'Koszt Wypożyczenia',
    replacement_cost AS 'Koszt odkupu'
FROM film 
LIMIT 20;

-- ZADANIA

SELECT * FROM customer;

SELECT 
	first_name AS 'Imię',
    last_name AS 'Nazwisko',
    email AS 'Email',
    create_date AS 'Data rejestracji'
FROM customer
LIMIT 99,15