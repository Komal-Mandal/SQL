SELECT 
    CASE 
        WHEN salary >= 20000 THEN 'higher salary'
        ELSE 'lower salary'
    END AS category
FROM employees;


CREATE TABLE orders (
    ord_id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE,
    amount DECIMAL(10,2) ,
    cus_id INT,
    FOREIGN KEY(cus_id) REFERENCES cus(cus_id)
);