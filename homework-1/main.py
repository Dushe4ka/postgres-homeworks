"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv

def opening_customers():
    with open('north_data/customers_data.csv', newline='') as f:
        list_cvs = []
        filereader = csv.reader(f, quotechar='|')
        next(filereader)
        for elem in filereader:
            list_cvs.append(elem)
        return list_cvs


def opening_employees():
    with open('north_data/employees_data.csv', newline='') as f:
        list_csv = []
        filereader = csv.reader(f, quotechar='|')
        next(filereader)
        for elem in filereader:
            list_csv.append(elem)
        return list_csv


def opening_orders():
    with open('north_data/orders_data.csv', newline='') as f:
        list_csv_order = []
        filereader = csv.reader(f, quotechar='|')
        for elem in filereader:
            next(filereader)
            list_csv_order.append(elem)
        return list_csv_order


conn = psycopg2.connect(
    host="localhost",
    database="north",
    user="postgres",
    password="12357985"
)

cur = conn.cursor()
# rows = opening_customers()
#
#
# cur.executemany("INSERT INTO customers VALUES (%s, %s, %s)", rows)
# cur.execute('SELECT * FROM customers')
row_emp = opening_employees()
for i in row_emp:
    print(i)
cur.executemany("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", row_emp)
# row_order = opening_orders()
# cur.executemany("INSERT INTO customers VALUES (%s, %s, %s)", row_order)
conn.commit()



