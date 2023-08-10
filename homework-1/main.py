"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
from employees import sql_empl, val_empl
from customers import sql_cust, val_cust
from orders import sql_ord, val_ord


conn = psycopg2.connect(
    host="localhost",
    database="north",
    user="postgres",
    password="914905"
)

try:
    with conn:
        with conn.cursor() as cur:
            cur.executemany(sql_empl, val_empl)
            cur.executemany(sql_cust, val_cust)
            cur.executemany(sql_ord, val_ord)
finally:
    conn.close()
