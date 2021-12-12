USE [NORTHWND]
GO

INSERT [dbo].[Categories] ([CategoryName], [Description], [Picture]) VALUES (N'Beverages', N'Soft drinks, coffees, teas, beers, and ales', NULL)
INSERT [dbo].[Categories] ([CategoryName], [Description], [Picture]) VALUES (N'Condiments', N'Sweet and savory sauces, relishes, seasonings', NULL)
GO

SELECT * FROM [dbo].[Categories]

SELECT CategoryName, COUNT(CategoryName) CategoryNameCount
FROM [dbo].[Categories]
GROUP BY CategoryName
HAVING COUNT(CategoryName) > 1


SELECT * FROM [dbo].[Categories]
WHERE 
	CategoryName LIKE 'A%' OR
	CategoryName LIKE 'B%' OR
	CategoryName LIKE 'C%' OR
	CategoryName LIKE 'D%' OR
	CategoryName LIKE 'E%' OR
	CategoryName LIKE 'F%'


SELECT * FROM [dbo].[Categories]
WHERE 
	CategoryName LIKE '[A-F]%'
