-- 문제 1
SELECT
    employeeNumber, 
    lastName,
    firstName,
    city
FROM
    employees
INNER JOIN offices
    ON employees.officeCode = offices.officeCode
ORDER BY
    employeeNumber;
-- 문제 2
SELECT
    customerNumber , officeCode , customers.city, offices.city
FROM
    customers
LEFT JOIN offices
    ON customers.city = offices.city
ORDER BY
    customerNumber DESC;
    
-- 문제 3
SELECT
    customerNumber , officeCode , customers.city, offices.city
FROM
    customers
RIGHT JOIN offices
    ON customers.city = offices.city
ORDER BY
    customerNumber DESC;
-- 문제 4
SELECT
    customerNumber , officeCode , customers.city, offices.city
FROM
    customers
INNER JOIN offices
    ON customers.city = offices.city
ORDER BY
    customerNumber DESC;
    
-- 문제 5
-- INNER는 겹치는것 조회
-- LEFT  customers.city 전부 조회
-- RIGHT offices.city 전부 조회

-- 문제 6 
SELECT
    customerNumber , officeCode , customers.city, offices.city
FROM
    customers
LEFT JOIN offices
    ON customers.city = offices.city
UNION    
SELECT
    customerNumber , officeCode , customers.city, offices.city
FROM
    customers
RIGHT JOIN offices
    ON customers.city = offices.city
ORDER BY
    customerNumber DESC;
    
-- 문제 7
SELECT
    orderdetails.orderNumber , orderDate 
FROM
    orderdetails
INNER JOIN orders
    ON orderdetails.orderNumber = orders.orderNumber
ORDER BY
    1;
-- 문제 8
SELECT
    orderdetails.orderNumber , orderdetails.productCode , productName 
FROM
    orderdetails
INNER JOIN products
    ON orderdetails.productCode = products.productCode
ORDER BY
    1;
-- 문제 9
SELECT
    orderdetails.orderNumber , 
    orderdetails.productCode , 
    orderDate, 
    productName
FROM
    orderdetails
INNER JOIN orders
    ON orderdetails.orderNumber = orders.orderNumber
INNER JOIN products
    ON orderdetails.productCode = products.productCode
ORDER BY
    1;
