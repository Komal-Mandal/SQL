create table cus(
 cus_id int auto_increment primary key,
 name varchar(50),
 email varchar(50)
 );

 
 CREATE TABLE orders (
        ord_id INT AUTO_INCREMENT PRIMARY KEY,
         date DATE,
       amount DECIMAL(10,2) ,
         cus_id INT,
        FOREIGN KEY(cus_id) REFERENCES cus(cus_id)
     );

     insert into cus(name,email)
     values("ram" ,"ram@gamil.com"),("shyam","shyam456@gmail.com"),("radha","radha@gmail.com");

insert into orders(ord_id,date,amount,cus_id)
 values(1,curdate(),234.56,1),(2,curdate(),567.78,1),(3,curdate(),779.45,2);

 /* joins */
 /* cross joins */
 select * from cus,orders;

 /* inner join */
  select * from cus
     inner join orders
     orders
     on orders.cus_id = cus.cus_id;

   /* inner join with group by*/
     select name,sum(amount) from cus
     inner join orders
     orders
     on orders.cus_id = cus.cus_id
     GROUP BY name;

/* left join */
select * from cus
left JOIN
orders
on orders.cus_id = cus.cus_id;

/* left join with group by*/
select name , sum(amount) from cus
left JOIN
orders
on orders.cus_id = cus.cus_id
group by name;

/* right join */
select * from cus
right JOIN
orders
on orders.cus_id = cus.cus_id;