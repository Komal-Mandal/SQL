/*task 1:list the all depatments*/
select distinct dept from employees;

/* task2:recods of high to low salary */
select * from employees
order by salary DESC;

/*task3:select only 3 starting rows  */
select * from employees
limit 3;

/*task4:name start with R*/
select * from employees
where NAME like "R%";

