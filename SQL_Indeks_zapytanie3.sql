CREATE CLUSTERED INDEX IX_TestTable_number2 
    ON dbo.Test (Zawartosc2);   
GO  

SELECT Zawartosc
  FROM [master].[dbo].[test]
  ORDER BY Zawartosc2 DESC