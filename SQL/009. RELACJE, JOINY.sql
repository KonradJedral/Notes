-- RELACJE 
-- RELACJE, TABELE RELACYJNE, REFERENCJE, ZAPYTANIA DO WIELU TABEL, JOIN'y, TRIGGERY

SELECT DATABASE();
SHOW TABLES;

CREATE TABLE uzytkownicy
(	
	id INT AUTO_INCREMENT PRIMARY KEY,
    imie VARCHAR(20) NOT NULL, 
    nazwisko VARCHAR(50) NOT NULL, 
    email VARCHAR(255) NOT NULL, 
    adres_ulica VARCHAR(255) NOT NULL,
    adres_miasto VARCHAR(255) NOT NULL,
	adres_kod VARCHAR(6) NOT NULL,
    telefon INT(9) NOT NULL,
    data_rejestracji TIMESTAMP DEFAULT NOW() ON UPDATE CURRENT_TIMESTAMP
);

LOAD DATA INFILE 
'C:\\Programowanie\\SQL\\Databases\\uzytkownicy.csv'
INTO TABLE uzytkownicy
CHARACTER SET utf8
FIELDS TERMINATED BY ';'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES 
(imie, nazwisko, email, adres_ulica, adres_miasto, adres_kod, telefon);

SELECT * FROM uzytkownicy;

CREATE TABLE zamowienia
(
	id INT AUTO_INCREMENT PRIMARY KEY,
    uzytkownicy_id INT NOT NULL,
    data_zamowienia TIMESTAMP DEFAULT NOW() ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE koszyk
( 
	zamowienia_id INT,
    ksiazki_id INt 
);

-- powyższe tabele nie maja referencji, wiec je usuwamy

DROP TABLE koszyk;
DROP TABLE zamowienia;

CREATE TABLE zamowienia
(
	id INT AUTO_INCREMENT PRIMARY KEY,
    uzytkownicy_id INT NOT NULL,
    data_zamowienia TIMESTAMP DEFAULT NOW() ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (uzytkownicy_id) REFERENCES uzytkownicy(id)   -- tworzenie referencji FOREIGN KEY (nazwa kolumny z tej tabeli) REFERENCES nazwa tabeli, z którą łączymy (nazwa kolumny)
);

CREATE TABLE koszyk
( 
	zamowienia_id INT,
    ksiazki_id INT,
    FOREIGN KEY (zamowienia_id) REFERENCES zamowienia(id),
    FOREIGN KEY (ksiazki_id) REFERENCES ksiazki(id)
);

LOAD DATA INFILE 
'C:\\Programowanie\\SQL\\Databases\\zamowienia.csv'
INTO TABLE zamowienia
CHARACTER SET utf8
FIELDS TERMINATED BY ';'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES 
(id, uzytkownicy_id);



LOAD DATA INFILE 
'C:\\Programowanie\\SQL\\Databases\\koszyk.csv'
INTO TABLE koszyk
CHARACTER SET utf8
FIELDS TERMINATED BY ';'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES 
(zamowienia_id, ksiazki_id);


SELECT * FROM ksiazki;
SELECT * FROM uzytkownicy;
SELECT * FROM koszyk;
SELECT * FROM zamowienia;


-- WYPISANIE DANYCH Z DWÓCH LUB WIECEJ TABEL BEZ JOINÓW 

SELECT * FROM zamowienia, uzytkownicy;


SELECT * FROM zamowienia, uzytkownicy WHERE uzytkownicy_id = uzytkownicy.id;
-- przypisujemy wartości z kolumny zamowienia (uzytkownicy_id) z kolumną z drugiej tabeli(id), 
-- żeby móc porównać z kolumną z drugiej tabeli to napierw musimy zapisać nazwe tabeli i po kropce nazwe tabeli (uzytkownicy.id)

-- Wszytkie zamówienia dla Pani Jadzi (użytkownik z id = 1)

SELECT * FROM zamowienia, koszyk, ksiazki WHERE zamowienia_id = zamowienia.id AND uzytkownicy_id = 1 AND ksiazki_id = ksiazki.id;




CREATE TABLE autor
(
    id INT AUTO_INCREMENT PRIMARY KEY,
    imie CHAR(20),
    nazwisko CHAR(20)
);
 
 
CREATE TABLE ksiazka
(
    id INT AUTO_INCREMENT PRIMARY KEY,
    tytul CHAR(20),
    rok_wydania INT(4),
    autor_id INT,
    FOREIGN KEY(autor_id) REFERENCES autor(id)
);
 
 
INSERT INTO autor(imie, nazwisko)
VALUES
    ("George", "Orwell"),
    ("Bram", "Stoker"),
    ("Frank", "Herbert"),
    ("Stephen", "King") ,
    ("Charles", "Dickens");
 
 
INSERT INTO ksiazka(tytul, rok_wydania, autor_id)
VALUES
    ("Animal Farm", 1945, 1),
    ("Dune", 1965, 3),
    ("Dracula", 1897, 2),
    ("The Stand", 1990, 4),
    ("1984", 1949, 1),
    ("The Shining", 1977, 4);
 
 
SELECT * FROM autor;
SELECT * FROM ksiazka;


-- JOINy

-- LEFT JOIN - Cała tabela pierwsza i część wspólna z drugiej 
SELECT * FROM autor LEFT JOIN ksiazka ON autor.id = ksiazka.autor_id; -- mamy wszystkich autorów i przypisane do nich ksiazki 

-- LEFT JOIN bez części wspólnej -wszystkie elementy z pierwszej tabeli, które nie mają części wspólnych w drugiej tabeli
SELECT * FROM autor LEFT JOIN ksiazka ON autor.id = ksiazka.autor_id 
WHERE ksiazka.autor_id IS NULL; -- wszyscy autorzy, do których nie ma przypisanych autorów 

-- RIGHT JOIN - cała druga tabela i część wspólna z pierwszej tabeli 
SELECT * FROM autor RIGHT JOIN ksiazka ON autor.id = ksiazka.autor_id; -- wszystkie ksiązki i przypisani do nich autorzy 

-- RIGHT JOIN bez części wspólnej  - wszystkie elemetny z drugiej tabeli, które nie mają części wspólnej w pierwszej tabeli 
SELECT * FROM autor RIGHT JOIN ksiazka ON autor.id = ksiazka.autor_id
WHERE ksiazka.autor_id IS NULL; -- wszystkie książki, które nie mają przypisanego autora (wszystkie ksiazki maja przypisanego autora)

-- INNER JOIN (JOIN) - część wspólna obydwu tabel 
SELECT autor.id, autor.imie, autor.nazwisko, ksiazka.tytul, ksiazka.rok_wydania FROM autor JOIN ksiazka ON autor.id = ksiazka.autor_id; -- wszyscy autorzyi książki, którzy są ze sobą powiązani 

-- CROSS JOIN -- przemnoży wszystkie przypadki z jednej tabeli przez wszystkie przypadki z drugiej tabeli
SELECT * FROM autor, ksiazka; 
-- wypisuje wszystkie wartości z pierwszej tabeli przypisujac jej pierwszą wartość z drugiej tabeli. 
-- Następnie znowu wypisuje wszystkie wartości z pierwszej tabeli przypisując im drugą wartość z drugiej tabeli itd..
-- Jest to równoważne z takim zapisem:
SELECT * FROM autor CROSS JOIN ksiazka;

-- FULL JOIN - wszystkie wartości z obydwu tabel
SELECT * FROM autor LEFT JOIN ksiazka ON autor.id = ksiazka.autor_id 
UNION 
SELECT * FROM autor RIGHT JOIN ksiazka ON autor.id = ksiazka.autor_id; -- wypisuje wszystkich autorów i wszystkie książki niezależnie czy mają jakieś powiązania



-- USUWANIE Z TABEL Z RELACJAMI

DELETE FROM autor WHERE imie='George'; 

DROP TABLE ksiazka;
DROP TABLE autor;


CREATE TABLE autor
(
    id INT AUTO_INCREMENT PRIMARY KEY,
    imie CHAR(20),
    nazwisko CHAR(20)
);
 
 
CREATE TABLE ksiazka
(
    id INT AUTO_INCREMENT PRIMARY KEY,
    tytul CHAR(20),
    rok_wydania INT(4),
    autor_id INT,
    FOREIGN KEY(autor_id) 
		REFERENCES autor(id)
        ON DELETE CASCADE -- jeśli jest taki zapis, to usuwając jakiegoś autora(już będziemy mogli) usuniemy wszystkie powiązane z nim książki
);
 
 
INSERT INTO autor(imie, nazwisko)
VALUES
    ("George", "Orwell"),
    ("Bram", "Stoker"),
    ("Frank", "Herbert"),
    ("Stephen", "King") ,
    ("Charles", "Dickens");
 
 
INSERT INTO ksiazka(tytul, rok_wydania, autor_id)
VALUES
    ("Animal Farm", 1945, 1),
    ("Dune", 1965, 3),
    ("Dracula", 1897, 2),
    ("The Stand", 1990, 4),
    ("1984", 1949, 1),
    ("The Shining", 1977, 4);
 
SELECT * FROM autor;
SELECT * FROM ksiazka;

DELETE FROM autor WHERE nazwisko='Orwell'; 



-- JOINy CD. 

SELECT * FROM zamowienia, uzytkownicy WHERE uzytkownicy_id = uzytkownicy.id;
SELECT * FROM zamowienia, koszyk WHERE zamowienia_id = zamowienia.id AND uzytkownicy_id = 1;

-- To samo za pomocą JOINów 

SELECT * FROM zamowienia LEFT JOIN uzytkownicy ON zamowienia.uzytkownicy_id = uzytkownicy.id;

SELECT 
	zamowienia.id,
    uzytkownicy.adres_ulica,
    uzytkownicy.adres_miasto,
    uzytkownicy.adres_kod
 FROM zamowienia 
 LEFT JOIN uzytkownicy 
 ON zamowienia.uzytkownicy_id = uzytkownicy.id;

-- Drugi przykład

SELECT * FROM zamowienia RIGHT JOIN uzytkownicy ON zamowienia.uzytkownicy_id = uzytkownicy.id
WHERE uzytkownicy_id = 1;


-- ŁĄCZENIE WIELU TABEL

SELECT 
	* 
FROM zamowienia JOIN koszyk 
ON zamowienia.id = koszyk.zamowienia_id
JOIN ksiazki 
ON koszyk.ksiazki_id = ksiazki.id;

-- inny przykład:

SELECT 
	uzytkownicy.imie,
    uzytkownicy.nazwisko,
    ksiazki.title
FROM uzytkownicy JOIN zamowienia ON uzytkownicy.id = zamowienia.uzytkownicy_id
JOIN koszyk ON zamowienia.id = koszyk.zamowienia_id
JOIN ksiazki ON koszyk.ksiazki_id = ksiazki.id;


-- TRIGGERY
-- wyzwalacze/spusty

-- DELIMITER $$ 
-- CIAŁO TRIGGERA				-- wszystko co sie znajdzie w srodku będzie traktowane jako jeden kod pomimo zawartych w środku wielu zapytań i ";"
-- $$
-- DELIMITER;

DELIMITER $$

CREATE TRIGGER insert_order BEFORE INSERT ON koszyk 
FOR EACH ROW BEGIN    -- konstrukcja stała, która sie nie zmienia 
	UPDATE magazyn SET stan_magazynowy = stan_magazynowy - 1
		WHERE magazyn.ksiazki_id = NEW.ksiazki_id;
END; $$
DELIMITER ;

SELECT ksiazki_id, stan_magazynowy FROM magazyn LIMIT 5;

-- Dodajemy nowe zamowienia (uzytkownikow, którzy cos zamówili do tabeli zamowienia)
INSERT INTO zamowienia(uzytkownicy_id)
VALUES
	(4),
    (8);

-- Sprawdzamy czy zostali dodani i nr ich zamowień
SELECT * FROM zamowienia WHERE uzytkownicy_id = 4 OR uzytkownicy_id = 8;

-- Dodajemy ksiazki jakie zamowili 
INSERT INTO koszyk(zamowienia_id, ksiazki_id)
VALUES 
	(12, 1),
    (12, 3),
    (13, 4);
    
-- Sprawdzamy, czy TRIGGER ustawiony na koszyk zmienił stan magazynowy o 1 w każdej zamówionej pozycji
SELECT ksiazki_id, stan_magazynowy FROM magazyn LIMIT 5;

-- Sprawdzanie jakie mamy triggery 
SHOW TRIGGERS;

-- Usuwanie Triggerow 
DROP TRIGGER insert_order -- DROP TRIGGER nazwa triggera


