-- SQL-команды для создания таблиц
create table customers(
customer_id varchar(30) primary key NOT null Unique,
company_name varchar(50),
contact_name varchar(50)
);
select * from customers;

create table employees(
employee_id serial primary key,
first_name varchar(20),
last_name varchar(20),
title varchar(50),
birth_date date,
notes text
);

select * from employees;

create table orders(
order_id int,
customer_id varchar(20) references customers(customer_id),
employee_id int references employees(employee_id),
order_date date,
ship_city varchar(20)
);

select * from orders;