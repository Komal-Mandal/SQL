/* String Function */

 /*1.concat*/
 
select concat("hey" "buddy");

select id,concat(NAME, " ", DESIGNATION) as fullname
from employees;


/* concat_ws means concat with separator */
select concat_ws("-","hii","hello");

select concat_ws(":","NAME","DESIGNATION","DEPT")
FROM employees;

/*  substring   */
select substring("hello buddy",1,4);

SELECT SUBSTRING(id,2) as emp_id,NAME from employees;


