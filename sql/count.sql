 
 /* it is used to count no of employees  in the table*/
 select count(*) from employees;


/* how many managers in the table */
select count(id) from employees
where DESIGNATION = "MANAGER";