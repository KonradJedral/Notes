-- LOGIKA 
-- Operatory logiczne, transpormacja, zawieranie, warunki 

-- OPERATORY LOGICZNE
-- =, !=, <, >, >=, <=,    AND, OR, BETWEEN, NOT BETWEEN, LIKE, NOT LIKE

SELECT 5=5; -- Wynik 1, czyli PRAWDA
SELECT 5=6; -- WYNIK 0, czyli FAŁSZ

SELECT 5!=5; -- WYNIK 0, czyli FAŁSZ
SELECT 5!=6; -- Wynik 1, czyli PRAWDA

SELECT 8>5;  -- 1=PRAWDA 
SELECT 5<6;  -- 1=PRWADA
SELECT 8>=5; -- 1=PRAWDA
SELECT 5<=5; -- 1=PRAWDA

SELECT title, rok_wydania FROM ksiazki WHERE rok_wydania >= 2000; -- wyświetli wszystkie książki wydane po 2000 roku 

SELECT title, rok_wydania FROM ksiazki WHERE rok_wydania != 2015; -- Wszystkie książki, które wydane były w innym roku niż 2015

-- AND = &&, OR = ||

SELECT        -- książki wydane po 2010 z ratingiem wiekszym niz 4
	title, 
	rok_wydania, 
	rating 
FROM ksiazki
WHERE 
	rok_wydania > 2010 AND 
    rating > 4;
    
SELECT        -- książki wydane po 2010 lub z ratingiem wiekszym niz 4
	title, 
	rok_wydania, 
	rating 
FROM ksiazki
WHERE 
	rok_wydania > 2010 OR 
    rating > 4;
    
SELECT        -- książki wydane po 2010, ale przed 2015 - BETWEEN
	title, 
	rok_wydania
FROM ksiazki
WHERE 
	rok_wydania > 2010 AND 
	rok_wydania < 2015;

-- BETWEEN

SELECT        -- książki wydane pomiędzy 2010, a 2015. (X >= 2010 AND X <= 2015)
	title, 
	rok_wydania
FROM ksiazki
WHERE 
	rok_wydania BETWEEN 2010 AND 2015;

-- NOT BETWEEN

SELECT        -- książki wydane przed 2010 i po 2005. (X < 2010 AND X > 2005)
	title, 
	rok_wydania
FROM ksiazki
WHERE 
	rok_wydania NOT BETWEEN 2000 AND 2005;
    
-- zaprzeczenie LIKE 
    
SELECT author, title FROM ksiazki WHERE author LIKE '%John%';
SELECT author, title FROM ksiazki WHERE author NOT LIKE '%John%';  -- Ci autorzy, którzy nie posiadają w imieniu lub nazwisku John


-- TRANSFORMACJE 
-- CAST(x AS Y) - X to co chcemy zamienić Y - na co zamieniamy (CHAR, DATE, INT)

SELECT CAST('200-05-01' AS DATE);


SELECT CAST(10 AS CHAR);  -- 10 jako napis, a nie liczba 

-- ZAWIERANIE  -  IN ()

-- po staremu:
SELECT 
	SUBSTRING_INDEX(author, ' ', 1) AS first_name,
    SUBSTRING_INDEX(author, ' ', -1) AS last_name,
    title,
    rok_wydania
FROM ksiazki
WHERE 
	SUBSTRING_INDEX(author, ' ', -1) = 'Tolkien' OR
    SUBSTRING_INDEX(author, ' ', -1) = 'Rowling' OR
    SUBSTRING_INDEX(author, ' ', -1) = 'King' OR 
    SUBSTRING_INDEX(author, ' ', -1) = 'Orwell';
    
-- Z wykorzystaniem IN 

SELECT 
	SUBSTRING_INDEX(author, ' ', 1) AS first_name,
    SUBSTRING_INDEX(author, ' ', -1) AS last_name,
    title,
    rok_wydania
FROM ksiazki
WHERE 
	SUBSTRING_INDEX(author, ' ', -1) IN ('Tolkien', 'Rowling', 'King', 'Orwell');
    
-- WARUNKI LOGICZNE 

SELECT 
	title,
    rating,
    CASE
		WHEN rating > 4 THEN 'dobra ksiazka' 
        ELSE 'przecietna ksiazka'
	END AS 'OCENA',
    author
FROM ksiazki;


SELECT 
	title,
    rating,
    CASE
		WHEN rating > 4.2 THEN 'bardzo dobra ksiazka' 
        WHEN rating BETWEEN 3.8 AND 4.2 THEN 'dobra ksiazka'
        ELSE 'przecietna ksiazka'
	END AS Rodzaj,
    author
FROM ksiazki;

-- IF 

SELECT 
	title,
    rating,
    IF(rating > 4, 'dobra ksiazka', 'przecietna ksiazka'),
    author
FROM ksiazki;




