CREATE NONCLUSTERED INDEX IX_TestTable_number2 
    ON dbo.Test (Zawartosc2);   
GO  

SELECT Zawartosc, Zawartosc2
  FROM [master].[dbo].[test]
  ORDER BY Zawartosc2 DESC