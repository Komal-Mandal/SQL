/* This query adds a new column salary to the employees table, which must always have a value (NOT NULL). If no salary is provided, it will default to 25000 */

alter table employees
add column 
salary int NOT NULL
default 25000;