create table person(
dt date,
dd time,
pdt datetimt
);

insert into person
values('2025-07-19' '23:00:00' '2023-07-12 23:00:00');

select * from person;

insert into person
values(curdate(), curtime(),now());

select dayname(curdate());
select dayofmonth(curdate());
select dayofweek(curdate());
select monthname(curdate());