-- SQL-команды для создания таблиц
CREATE TABLE customers
(
	customer_id text PRIMARY KEY,
	company_name text,
	contact_name text
);

SELECT * FROM orders;


CREATE TABLE employees
(
	employee_id int PRIMARY KEY,
	first_name text,
	last_name text,
	title text,
	birth_date date,
	notes varchar(100)
);


CREATE TABLE orders
(
	order_id int PRIMARY KEY,
	customer_id text REFERENCES customers(customer_id),
	employee_id int REFERENCES employees(employee_id),
	order_date date,
	ship_city text
)