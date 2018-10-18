1.
SELECT * FROM CUSTOMERS
WHERE Country='UK';

2.
SELECT Orders.CustomerID, CustomerName, COUNT(*) AS Cnt from Orders
Join Customers ON Orders.CustomerID = Customers.CustomerID
Group by Customers.CustomerID
Order by Cnt DESC;

3.
Select Products.SupplierID, SupplierName, AVG(Price) from Products
JOIN Suppliers ON Suppliers.SupplierID = Products.SupplierID
Group By Suppliers.SupplierID
Order By AVG(Price) DESC;

4.
SELECT COUNT(DISTINCT(Country)) FROM CUSTOMERS

5.
SELECT CategoryName, COUNT(Categories.CategoryID) as CNT
FROM Products
 	JOIN Orderdetails ON Products.ProductID = Orderdetails.ProductID
    JOIN Categories ON Products.CategoryID = Categories.CategoryID
Group By Categories.CategoryID
Order By CNT Desc;

6.
SELECT OrderID, Orderdetails.Quantity AS Cost
FROM Products
	Join Orderdetails ON Orderdetails.ProductID = Products.ProductID
GROUP BY OrderID
Order By Cost DESC;

7.
SELECT e.FirstName, e.LastName, SUM(p.Price * op.Quantity) as Total
FROM Employees as e
	Join Orders as o
    Join OrderDetails as op
    Join Products as p
    On
    	e.EmployeeID = o.EmployeeID
        AND
        o.OrderID = op.OrderID
        AND
        op.ProductID = p.ProductID
Group By e.EmployeeID
Order By
	Total DESC;

8.
SELECT e.FirstName, e.LastName, e.Notes
FROM 
	Employees as e
WHERE
	e.Notes LIKE '%BS%'

9.
SELECT AVG(p.Price) as AvgPrice, SupplierName, Count(*) as NumProducts
FROM Products as p
	JOIN Suppliers AS s
		ON 
        p.SupplierID = s.SupplierID
GROUP BY s.SupplierID
HAVING NumProducts >= 3
ORDER BY AvgPrice DESC;


	
