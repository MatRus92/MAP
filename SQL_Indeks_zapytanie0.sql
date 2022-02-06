DROP TABLE test
CREATE TABLE test (Id INT IDENTITY, Zawartosc INT, Zawartosc2 MONEY)
GO

DECLARE @a INT
SET @a = 1
WHILE @a < 1000000 BEGIN
            INSERT INTO test (Zawartosc, Zawartosc2) VALUES (CONVERT(INT,RAND() * 100000), CONVERT(INT,RAND() * 100000))
            SET @a = @a + 1
END
GO