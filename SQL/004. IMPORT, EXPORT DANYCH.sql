-- POBIERANIE DANYCH Z PLIKU 

-- Tworzymy tabele, do której zaimportujemy dane 

CREATE TABLE fastest_file2
(
	zwierze CHAR(30),
    predkosc DECIMAL(4,1),   -- (długość przed przecinkiem, długość po przecinku)
    klasa CHAR(20)
);

-- Zmiana możliwości importowania danych z każdej lokalizacji: 
-- 1. Zamknij Workbench, 2. Zainstaluj MySQL Notifier (https://downloads.mysql.com/archives/notifier/), 3. w C:\ProgramData\MySQL\MySQL Server 8.0 znajdz plik my.ini
-- 4. secure-file-priv="C:\ProgramData\MySQL\MySQL Server 8.0\Uploads" zmień na secure-file-priv="", 5. Restart serwera przez Notifiera

LOAD DATA INFILE 'C:\\Programowanie\\SQL\\Databases\\fastest_utf8.csv'
INTO TABLE fastest_file2
CHARACTER SET utf8MB4  -- pozwala zachować polskie znaki 
FIELDS TERMINATED BY ';'  -- separator naszych pól - co oddziela  kolejne wartości
OPTIONALLY ENCLOSED BY '"' -- oznacza, że " jest częścią oznaczenia pola, a nie wartością pola
LINES TERMINATED BY '\r\n' -- -- przejście do nowej linii za pomocą entera 
IGNORE 1 LINES -- zignoruj pierwszą linię przy wczytywaniu (ponieważ są to nagłówki)
(zwierze, @predkosc, @klasa) -- tworzenie tymczasowych kolumn, tworzymy je bo mają przecinki lub puste wiersze
SET predkosc = REPLACE(@predkosc, ',', '.'), -- REPLACE(gdzie, co, na co) -- zmieniamy , na . w tymczasowej kolumnie @ predkosc i przypisujemy ja do kolumny predkosc
	klasa = IF(@klasa = '', NULL, @klasa); -- do kolumny klasa przypisujemy kolumne @klasa, jeżeli IF(warunek, jeśl Prawda, jeśli Fałsz) - wpisujemy NULL w puste wiersze
    
SELECT * FROM fastest_file2;


-- ZADANIE 

CREATE TABLE ksiazki
(
	id INT AUTO_INCREMENT PRIMARY KEY,
    author CHAR(40),
    title VARCHAR(150),
    rok_wydania INT,
    ISBN char(13),
    rating DECIMAL(3,2),
    ratings_no INT,
    reviews_no INT,
    1_star INT,
    2_star INT, 
    3_star INT, 
    4_star INT,
    5_star INT
);

LOAD DATA INFILE 'C:\\Programowanie\\SQL\\Databases\\ksiazki.csv'
INTO TABLE ksiazki
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES 
(author, title, rok_wydania, ISBN, @rating, ratings_no, reviews_no, 1_star, 2_star, 3_star, 4_star, 5_star)
SET rating = REPLACE(@rating, ',', '.');

SELECT * FROM ksiazki;



-- EXPORT DANYCH


SELECT author, title FROM ksiazki;

SELECT author, title FROM ksiazki 
INTO OUTFILE 'C:\\Programowanie\\SQL\\Databases\\pliktest.csv'
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n';