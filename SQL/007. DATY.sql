-- DATY

SELECT CURDATE();  -- obecna data 

SELECT CURTIME();  -- obecna godzina 

SELECT NOW();  -- obecna data i godzina 

SELECT DAY(NOW());  -- obecny dzień wyciagnięty z NOW()

SELECT DAY('2017-10-19');  -- dzień z podanej daty 

SELECT DAYNAME(NOW());  -- nazwa dnia jaki jest od NOW 

SELECT DAYOFWEEK(NOW());  -- liczbowo, który dzień tygodnia od NOW (niedziela = 1)

SELECT DAYOFYEAR(NOW());  -- liczbowo, który jest dzień roku od NOW 

SELECT MONTH(NOW());  -- liczbowo, który jest miesiac od NOW 

SELECT MONTHNAME(NOW());  -- nazwa miesiaca od NOW

SELECT HOUR(NOW()) ; -- liczbowo, godzina od NOW

SELECT MINUTE(NOW());  -- liczbowo, minuta od NOW

SELECT SECOND(NOW()); -- liczbowo, sekunda od NOW

-- DATE_FORMAT

SELECT DATE_FORMAT('2010-05-01 14:32:11', '%d/%m/%y');  -- konwersja daty na inny format (01/05/10)

SELECT DATE_FORMAT('2010-05-01 14:32:11', '%M-%D-%Y, %H:%i');   -- May-1st-2010, 14:32

-- Tabela z formatami dat:   https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_date-format

-- OPERACJE NA DATACH

SELECT DATEDIFF(NOW(), '2010-05-01');  -- DATEDIFF - różnica pomiedzy datami 

SELECT DATE_ADD(NOW(), INTERVAL 100 DAY);  -- dodajemy 100 dni do NOW

SELECT DATE_ADD(NOW(), INTERVAL 23 YEAR);  -- dodajemy do NOW 23 lata

SELECT DATE_SUB(NOW(), INTERVAL 100 DAY);  -- odejmujemy 100 dni

SELECT DATE_SUB(NOW(), INTERVAL 23 YEAR); -- odejmujemy  23 lata

-- TIMESTAMP
-- zwraca datę lub date i czas w postaci wartości DATETIME

SELECT TIMESTAMP('2010-05-01');

-- Budujemy tabelę do przetestowania TIMESTAMP 

CREATE TABLE komentarze 
(
	tresc VARCHAR(250),
    data_wpisu TIMESTAMP DEFAULT NOW()
);

INSERT INTO komentarze(tresc) VALUES ('Ta ksiazka jest super!');
INSERT INTO komentarze(tresc) VALUES ('Podobało mi się ;) ');

SELECT * FROM komentarze; 

UPDATE komentarze SET tresc = 'no moze nie za bardzo fajna' 
WHERE tresc ='Ta ksiazka jest super!';

-- dodawane komentatrze automatycznie mają przypisany TIMESTAMP według czasu, w którym komentarz został utworzony
-- UPDATE nie zmienia TIMESTAMP, dlatego trzeba podczas tabeli dodać "UPDATE CURRENT_TIMESTAMP"

CREATE TABLE komentarze2
(
	tresc VARCHAR(250),
    data_wpisu TIMESTAMP DEFAULT NOW() ON UPDATE CURRENT_TIMESTAMP
);

INSERT INTO komentarze2(tresc) VALUES ('Ta ksiazka jest super!');
INSERT INTO komentarze2(tresc) VALUES ('Podobało mi się ;) ');

SELECT * FROM komentarze2; 

UPDATE komentarze2 
SET tresc = 'no moze nie za bardzo fajna' 
WHERE tresc ='Ta ksiazka jest super!';