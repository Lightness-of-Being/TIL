-- 문제 1
SELECT
    productCode, productName, MSRP
FROM
    products
WHERE
    MSRP > 
    (SELECT AVG(MSRP) FROM products)
ORDER BY
    3;
-- 문제 2
SELECT
    customers.customerNumber, customerName
FROM
    customers
INNER JOIN orders
    ON customers.customerNumber = orders.customerNumber
WHERE orderDate BETWEEN '2003-01-06' and '2003-03-26'
ORDER BY
    1;
-- 문제 3
SELECT
    productCode , productName , productLine , MSRP
FROM
    products
WHERE (
    productLine = 'Classic Cars' and
    (MSRP = (SELECT MAX(MSRP) FROM products))
);
-- 문제 4
SELECT customerNumber, customerName, country
FROM customers
WHERE  country = (SELECT MAX(country) FROM customers)
ORDER BY customerNumber ASC;
-- 문제 5
SELECT C.customerNumber, C.customerName, COUNT(*) AS order_count
FROM customers AS C INNER JOIN orders AS O 
ON C.customerNumber = O.customerNumber
GROUP BY C.customerNumber
HAVING customerNumber = 
(SELECT MAX(
(SELECT COUNT(*) FROM customers)
) FROM customers);
-- 문제 6
SELECT DISTINCT productCode, productName
FROM orders AS t1
JOIN orderdetails AS t2 USING (orderNumber) 
JOIN products AS t3 USING (productCode)
WHERE YEAR(t1.orderDate) = '2004'
ORDER BY productCode DESC;

