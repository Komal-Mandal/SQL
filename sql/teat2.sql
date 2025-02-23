/* create database */
create database test_db;

/* create table */

create table employees(

    id INT PRIMARY KEY  ,
    NAME VARCHAR(50) NOT NULL,
    DESIGNATION VARCHAR(50) NOT NULL DEFAULT 'PROBATION',
    DEPT VARCHAR(50) NOT NULL
);
 /* insert values inside the table */

insert into employees(id,NAME,DESIGNATION,DEPT)

VALUES
(101,"RAM","MANAGER","LOAN"),
(102,"SHAM","EMPLOYEE","cash"),
(103,"RAJU","HR","LOAN"),
(104,"rohit","it","cash");

/* SHOW ONLY THOSE ROW WHICH CONTAING DEPT AS LOAN */
 select * from employees where DEPT = "LOAN";

 /* SHOW ONLY FIRST ROW */
 SELECT * FROM  employees where id="101";

 /* show only id,name from first row */
 SELECT id,NAME FROM  employees where id="101";

 /*UPDATE THE DESIGNATION VALUE TO LOAN WHO HAVE ID 104 */

 UPDATE employees
 set DEPT="LOAN"
 WHERE ID = 104;

 /*delete the record which have id = 103 */
 delete from employees where id = 103;

 