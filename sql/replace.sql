select replace("hello buddy","hello","hey");

select replace(id,10,"EMP") as EMP_ID,NAME from employees; 

/* reverse */

select reverse(NAME) as rname from employees;

/* upper case */
select ucase(NAME) from employees;

/* lower case */
select lcase(NAME) FROM employees;

/* char_length */
select NAME,char_length(NAME) AS LENGTH from employees;

/* left */
select left("hey buddy raju",3);

/* right */
select right("hey buddy raju",4);

/* repeat */
select repeat("hahaha",10);

/* TRIM */
select trim(   "komal"   );
