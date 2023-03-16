-- FUNKCJE AGREGUJACE 
-- COUNT()
-- Zlicza liczbę wierszy 

SELECT COUNT(*) FROM ksiazki;  -- zlicza wszystkie ksiazki 

SELECT COUNT(author) FROM ksiazki; -- zliczy ilu jest autorów wraz z powtórzeniami, czyli ten sam wynik co przy (*)

SELECT COUNT(DISTINCT author) FROM ksiazki;  -- zliczy ilu jest autorów bez powtórzeń

SELECT COUNT(*) FROM ksiazki  -- zlicza ile jest ksiazek, w których tytule znajduje się 'the'
WHERE title LIKE '%the%';

SELECT COUNT(*) FROM ksiazki    -- zlicza ile jest wystąpień autorow z nazwiskiem, które składa się z 6 liter
WHERE CHAR_LENGTH(SUBSTRING_INDEX(author, ' ', -1)) = 6; 

SELECT 
	COUNT(DISTINCT SUBSTRING_INDEX(author, ' ', -1)) AS 'liczba unikatów na 6' 
FROM ksiazki 
WHERE CHAR_LENGTH(SUBSTRING_INDEX(author, ' ', -1)) = 6; 		-- Zlicza liczbę unikalnych nazwisk na 6 liter 

-- GRUPOWANIE 

SELECT   -- zlicza ile ksiazek napisal każdy z autorów
	author, 
    COUNT(*) AS 'ile ksiazek' 
FROM ksiazki
GROUP BY author;

-- STATYSTYKI OPISOWE
-- MIN(), MAX(), SUM(), AVG(), ROUND(), % - MODULO - reszta z dzielenia 
SELECT MIN(rating) FROM ksiazki;  -- najniższy rating
SELECT MAX(rating) FROM ksiazki; -- najwyższy rating


-- Dwa zapisy na znalzienie MIN lub MAX przy SELECT kilku kolumn:
SELECT author, title, rating FROM ksiazki ORDER BY rating LIMIT 1;   

SELECT author, title, rating FROM ksiazki
WHERE rating = (SELECT MIN(rating) FROM ksiazki);

-- SUM()

SELECT SUM(ratings_no) FROM ksiazki;

SELECT author, SUM(ratings_no), COUNT(*) FROM ksiazki
GROUP BY author;

-- AVG()
-- standardowo minimum 4 miejsca po przecinku 

SELECT AVG(ratings_no) FROM ksiazki;  -- srednia ilść głosów oddana na ksiazke

SELECT 
	rok_wydania, 
    ROUND(AVG(rating), 2),
    COUNT(*)
FROM ksiazki
GROUP BY rok_wydania
ORDER BY rok_wydania DESC;

-- ROUND()
-- zaokrąglanie wyników

SELECT ROUND(4.21213144, 2); -- zakrogla (liczba, ilosc miejsc po przecinku) tak jak w matematyce

-- MODULO() - reszta z dzielenia 

SELECT 13 % 2;
SELECT 13 % 5;
SELECT 
	rok_wydania, 
    ROUND(AVG(rating), 2),
    COUNT(*)
FROM ksiazki
WHERE rok_wydania % 2 = 0     -- tylko dla lat parzystych
GROUP BY rok_wydania
ORDER BY rok_wydania DESC;




