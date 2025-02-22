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
(102,"SHAM","EMPLOYEE","LOAN"),
(103,"RAJU","HR","LOAN");

/* display the table */
 SELECT * FROM employees;

/* display only id and name from the table */
  select id,name from employees;