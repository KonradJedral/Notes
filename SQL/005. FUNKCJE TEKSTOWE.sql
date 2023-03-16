USE ksiegarnia;

-- Łączenie tekstów 
-- CONCAT(tekst, tekst2, tekst3)

SELECT CONCAT(author, title) FROM ksiazki LIMIT 5;

SELECT CONCAT(author, '-', title, '-', rok_wydania) FROM ksiazki LIMIT 5;

SELECT   
	CONCAT_WS(' - ', author, title, rok_wydania) AS 'autor - tytuł - rok wydania'  -- najpierw separator, pózniej co łączymy, dodajemy AS, żeby ładnie nazwać naszą kolumnę
    FROM ksiazki 
    LIMIT 5;
    
-- Wybieranie części tekstu
-- SUBSTRING(tekst, początek, ilość) 

SELECT SUBSTRING('MySQL jest super', 7, 4);   -- (tekst, index od którego zaczynamy(od 1 nie od 0), ile)
SELECT SUBSTRING('MySQL jest super', 3, 12);
SELECT SUBSTRING('MySQL jest super', 7);   -- od pozycji 7 do końca 
SELECT SUBSTRING('MySQL jest super', -4);  -- od 4 od końca do końca 
SELECT SUBSTRING('MySQL jest super', );

SELECT SUBSTRING(title, 1, 12) FROM ksiazki;
SELECT SUBSTR(title, 1, 12) FROM ksiazki; -- krótszy zapis

-- CONCAT + SUBSTRING

SELECT concat
(
	SUBSTRING(title,1,7),		-- UWAGA! dla krótszych tytułów niż 7 znaków i tak zostaną dodane "..."
    '...'
)
FROM ksiazki;

-- ZASTĘPOWANIE TEKSTU
-- REPLACE(tekst, co zamieniamy, na co zamieniamy)

SELECT REPLACE('MySQL jest super!', 'super', 'extra'); 

SELECT 
substring(
	REPLACE(title, 'e', '3'),
    1, 10
)
FROM ksiazki;


-- ODWRACANIE TEKSTU OD TYŁU 
-- REVERSE(tekst)

SELECT REVERSE(author) FROM ksiazki;


-- SPRAWDZANIE DLUGOSCI TEKSTU
-- CHAR_LENGTH(tekst)

SELECT CHAR_LENGTH('My SQL jest super!');

SELECT title, CHAR_LENGTH(title) AS 'Długosć tytułu' FROM ksiazki;

-- Podnoszenie do duzych liter
-- UPPER(tekst)

SELECT UPPER(title) FROM ksiazki;

-- Zmniejszanie do małych liter
-- LOWER(tekst)

SELECT LOWER('MYSQL JEST Super!');

-- ROZBIJANIE JEDNEJ KOLUMNY NA DWIE 
-- SUBSTRING_INDEX(nazwa kolumny, która rozbijamy, separator, index (calego słowa), które chcemy wyciągnąć)

SELECT 
	SUBSTRING_INDEX(author, ' ', 1) AS first_name,
	SUBSTRING_INDEX(author, ' ', -1) AS last_name
FROM ksiazki;

-- ZWRACANIE TYLKO WARTOSCI UNIKALNYCH, BEZ POWTÓRZEŃ
-- DISTINCT

SELECT DISTINCT rok_wydania FROM ksiazki;


-- SORTOWANE 
-- ORDER BY po czym sortujemy 
-- ORDER BY po czym DESC - odwraacmy

SELECT
	title AS tytuł, 
    rating 
FROM ksiazki
ORDER BY  rating;

SELECT
	title AS tytuł, 
    rating 
FROM ksiazki
ORDER BY rating DESC
LIMIT 10;

SELECT 
	author AS autor,
	title AS tytuł,
    rating AS ocena,
    rok_wydania AS rok_wydania,
    ISBN
FROM ksiazki
ORDER BY 4 DESC;  -- posortuje po roku wydania, dlatego że jest czwarta kolumna wypisana w SELECT 


-- WYSZUKIWANIE FRAZ 
-- LIKE 

SELECT * FROM ksiazki 
WHERE author LIKE 'John Tolkien'; -- To samo co: WHERE author = 'John Tolkien'; 

-- W funkcji LIKE możemy używać %, który zastępuje dowolny znak lub ciąg znaków:

SELECT * FROM ksiazki 
WHERE author LIKE 'John%'; -- wyświetli wszystkie rekordy, które zaczynają się od John i dalej dowolnie. 

SELECT * FROM ksiazki 
WHERE author LIKE 'Jo%';

SELECT * FROM ksiazki 
WHERE author LIKE '%en';  -- Jak nie pamiętamy co jest z przodu, a pamiętamy koniec 

SELECT * FROM ksiazki 
WHERE author LIKE '%To%';  -- Dowolne znaki (w tym nic) + To + dowolne znaki (w tym na koncu)

SELECT SUBSTRING_INDEX(author, ' ', 1) FROM ksiazki
WHERE SUBSTRING_INDEX(author, ' ', 1) LIKE '____'; -- szukamy imion, które mają 4 litery, dlatego dajemy cztery "_"



