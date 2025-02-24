/* GROUP BY is used to group similar data together and apply functions like count, sum, or average on each group.*/

select DEPT from employees group by DEPT;

select count(id) from employees group by DEPT;