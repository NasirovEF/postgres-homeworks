"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import psycopg2


conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='12345')
with conn:
    with conn.cursor() as cur:
        with open('north_data/customers_data.csv', encoding='utf-8') as file:
            header = next(file)
            file_r = csv.reader(file, delimiter=',')
            for v in file_r:
                cur.execute("INSERT INTO customers VALUES (%s, %s, %s)", tuple(v))

        with open('north_data/employees_data.csv', encoding='utf-8') as file:
            header = next(file)
            file_r = csv.reader(file, delimiter=',')
            for v in file_r:
                cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", tuple(v))

        with open('north_data/orders_data.csv', encoding='utf-8') as file:
            header = next(file)
            file_r = csv.reader(file, delimiter=',')
            for v in file_r:
                cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", tuple(v))

conn.close()
