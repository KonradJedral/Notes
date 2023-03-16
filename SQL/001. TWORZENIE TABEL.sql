-- TWORZENIE TABEL I DODAWANIE REKORDÓW 
-- NOT NULL, DEFAULT, AUTO_INCREMENT, PRIMARY KEY

CREATE TABLE unikaty_najszybsze
(
	zwierze_id INT AUTO_INCREMENT,		-- jeśli Primary Key jest tylko jedna kolomna to możemy ją wpisać tu, jeśli więcej to na dole
    zwierze CHAR(20) DEFAULT 'nienazwane',
    max_predkosc INT NOT NULL,
    stan CHAR(10) DEFAULT 'nie podano',
	PRIMARY KEY (zwierze_id)
);

-- Opis tabeli
DESC unikaty_najszybsze;

-- Dodawanie pojedynczego rekordu
INSERT INTO unikaty_najszybsze (zwierze, max_predkosc, stan) 
VALUES ('Sokol Wedrowny', 390, 'nurkowanie');

-- Dodawanie kilku rekordów 
INSERT INTO unikaty_najszybsze (zwierze, max_predkosc, stan) 
VALUES 
('Orzel Zloty', 320, 'nurkowanie'),
('Kobuz', 160, 'nurkowanie'),
('Gepard', 120, 'sprint');

-- Usuwanie tabeli
DROP TABLE unikaty_najszybsze;


SELECT * FROM unikaty_najszybsze;

