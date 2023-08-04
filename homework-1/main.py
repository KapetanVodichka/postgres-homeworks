"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv
import os


current_dir = os.path.dirname(os.path.abspath(__file__))


conn = psycopg2.connect(
    host='localhost',
    database='north',
    user='postgres',
    password='****'
)

customer_file_path = os.path.join(current_dir, "north_data", "customers_data.csv")
employees_file_path = os.path.join(current_dir, "north_data", "employees_data.csv")
orders_file_path = os.path.join(current_dir, "north_data", "orders_data.csv")

customer_data = []
with open(customer_file_path, 'r', newline='') as f:
    csv_reader = csv.DictReader(f)
    for row in csv_reader:
        customer_data.append((row["customer_id"], row["company_name"], row["contact_name"]))

employees_data = []
with open(employees_file_path, 'r', newline='') as f:
    csv_reader = csv.DictReader(f)
    for row in csv_reader:
        employees_data.append((row["employee_id"], row["first_name"], row["last_name"], row["title"], row["birth_date"], row["notes"]))

orders_data = []
with open(orders_file_path, 'r', newline='') as f:
    csv_reader = csv.DictReader(f)
    for row in csv_reader:
        orders_data.append((row["order_id"], row["customer_id"], row["employee_id"], row["order_date"], row["ship_city"]))

try:
    with conn:
        with conn.cursor() as cur:
            cur.executemany('INSERT INTO customers (customer_id, company_name, contact_name) VALUES (%s, %s, %s)', customer_data)
            cur.executemany('INSERT INTO employees (employee_id, first_name, last_name, title, birth_date, notes) VALUES (%s, %s, %s, %s, %s, %s)', employees_data)
            cur.executemany('INSERT INTO orders (order_id, customer_id, employee_id, order_date, ship_city) VALUES (%s, %s, %s, %s, %s)', orders_data)
            cur.execute('SELECT * FROM customers')
            cur.execute('SELECT * FROM employees')
            cur.execute('SELECT * FROM orders')
            rows = cur.fetchall()
finally:
    conn.close()

# Проверил в pgAdmin 4 - всё заносится корректно