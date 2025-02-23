
/* Task 1*/
select concat_ws(":",id,NAME,DESIGNATION,DEPT) FROM employees;

/* Task 2*/
SELECT CONCAT_WS(":", id, NAME, UPPER(DESIGNATION), DEPT) FROM employees;

/* tASK 3*/
select CONCAT(LEFT(DEPT,1),id),NAME FROM employees;
