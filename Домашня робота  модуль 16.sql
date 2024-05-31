-- Створення бази даних Sales
--CREATE DATABASE Sales;

-- Створення таблиці Sales (інформація про продажі)
-- CREATE TABLE Salesman (
--     ID SERIAL PRIMARY KEY,
--     Name VARCHAR(100)
--     )
-- CREATE TABLE Customer (
--     ID SERIAL PRIMARY KEY,
--     Name VARCHAR(50),
--     Email VARCHAR(100)
-- );

-- CREATE TABLE Sales1 (
--     ID SERIAL PRIMARY KEY,
--     INFO VARCHAR(25),
--     SaleAmount DECIMAL(10, 2),
--     Salesman_ID INT REFERENCES Salesman(ID),
--     Customer_ID INT REFERENCES Customer(ID)
-- );


--Відображення усіх угод
-- SELECT * 
-- FROM Sales;

--Відображення угод конкретного продавця
-- SELECT * 
-- FROM Sales 
-- WHERE Salesman_ID = Salesman_ID;

--Відображення максимальної за сумою угоди
--SELECT * 
--FROM Sales ORDER BY SaleAmount ASC LIMIT 1

--Відображення мінімальної за сумою угоди
--SELECT * FROM Sales1 ORDER BY SaleAmount ASC LIMIT 1;

--Відображення максимальної суми угоди для конкретного продавця
-- SELECT * 
-- FROM Sales1 WHERE Salesman_ID = Salesman_ID ORDER BY SaleAmount DESC LIMIT 1;

--Відображення мінімальної за сумою угоди для конкретного продавця
--SELECT * FROM Sales1 WHERE Salesman_ID = Salesman_ID ORDER BY SaleAmount ASC LIMIT 1;

--Відображення максимальної за сумою угоди для конкретного покупця
--SELECT * 
--FROM Sales1 WHERE Customer_ID = Customer_ID ORDER BY SaleAmount DESC LIMIT 1;

--Відображення мінімальної за сумою угоди для конкретного покупця
--SELECT * 
--FROM Sales1 WHERE Customer_ID = Customer_ID ORDER BY SaleAmount ASC LIMIT 1;

--Відображення продавця з максимальною сумою продажів за всіма угодами
-- SELECT Salesman_ID, SUM(SaleAmount) AS TotalSalesAmount 
-- FROM Sales1 
-- GROUP BY Salesman_ID 
-- ORDER BY TotalSalesAmount DESC 
-- LIMIT 1;

--Відображення продавця з мінімальною сумою продажів за всіма угодами
-- SELECT Salesman_ID, SUM(SaleAmount) AS TotalSalesAmount 
-- FROM Sales1 
-- GROUP BY Salesman_ID 
-- ORDER BY TotalSalesAmount ASC 
-- LIMIT 1;

-- Відображення покупця з максимальною сумою покупок за всіма угодами
-- SELECT Customer_ID, SUM(SaleAmount) AS TotalPurchasesAmount 
-- FROM Sales1 
-- GROUP BY Customer_ID 
-- ORDER BY TotalPurchasesAmount DESC 
-- LIMIT 1;

-- Відображення середньої суми покупки для конкретного покупця
-- SELECT Customer_ID, AVG(SaleAmount) AS AvgPurchaseAmount 
-- FROM Sales1 
-- GROUP BY Customer_ID 
-- HAVING Customer_ID = Customer_ID;

--Відображення середньої суми покупки для конкретного продавця
-- SELECT Salesman_ID, AVG(SaleAmount) AS AvgSaleAmount 
-- FROM Sales1 
-- GROUP BY Salesman_ID 
-- HAVING Salesman_ID = Salesman_ID;