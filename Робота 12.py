# Завдання 1
# Створіть тритабличну базу даних Sales (Продажі). У цій
# базі даних мають бути таблиці: Sales (інформація про конкретні
# продажі), Salesmen (інформація про продавців), Customers (інформація про покупців). Створіть додаток для відображення
# даних з таблиць. Меню додатку має містити такий мінімальний набір звітів:
# ■ Відображення усіх угод;
# ■ Відображення угод конкретного продавця;
# ■ Відображення максимальної за сумою угоди;
# ■ Відображення мінімальної за сумою угоди;
# ■ Відображення максимальної суми угоди для конкретного
# продавця;
# ■ Відображення мінімальної за сумою угоди для конкретного продавця;
# ■ Відображення максимальної за сумою угоди для конкретного покупця;
# ■ Відображення мінімальної за сумою угоди для конкретного покупця;
# ■ Відображення продавця з максимальною сумою продажів
# за всіма угодами;
# Домашнє завдання
# 1
# ■ Відображення продавця з мінімальною сумою продажів
# за всіма угодами;
# ■ Відображення покупця з максимальною сумою покупок
# за всіма угодами;
# ■ Відображення середньої суми покупки для конкретного
# покупця;
# ■ Відображення середньої суми покупки для конкретного
# продавця.
# Завдання 2
# Додайте механізми для оновлення, видалення та вставки
# даних до бази даних за допомогою інтерфейсу меню. Користувач не може ввести запити INSERT, UPDATE, DELETE безпосередньо. Забороніть можливість оновлення та видалення
# усіх даних для кожної таблиці (UPDATE та DELETE без умов).
# Завдання 3
# Додайте до першого завдання можливість збереження
# результатів фільтрів у файл. Шлях і назву файлу вкажіть у
# налаштуваннях програми.

from sqlalchemy import create_engine, Column, Integer, String, Sequence, Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import text
import json
import psycopg2



with open('config.json', 'r') as f:
    data = json.load(f)
    db_user = data['user']
    db_password = data['password']

db_url = f'postgresql+psycopg2://{db_user}:{db_password}@localhost:5432/Hospital'
engine = create_engine(db_url)




def connect():
    return psycopg2.connect(
        dbname="Sales",
        user="your_username",
        password="your_password",
        host="localhost"
    )


def display_all_sales(cursor):
    cursor.execute("SELECT * FROM Sales")
    for row in cursor.fetchall():
        print(row)


def display_sales_by_salesman(cursor, salesman_id):
    cursor.execute("SELECT * FROM Sales WHERE Salesman_ID = %s", (salesman_id,))
    for row in cursor.fetchall():
        print(row)


def display_max_sale(cursor):
    cursor.execute("SELECT * FROM Sales ORDER BY SaleAmount DESC LIMIT 1")
    print(cursor.fetchone())


def display_min_sale(cursor):
    cursor.execute("SELECT * FROM Sales ORDER BY SaleAmount ASC LIMIT 1")
    print(cursor.fetchone())


def insert_sale(cursor, info, sale_amount, salesman_id, customer_id, sale_date):
    cursor.execute(
        "INSERT INTO Sales (INFO, SaleAmount, Salesman_ID, Customer_ID, SaleDate) VALUES (%s, %s, %s, %s, %s)",
        (info, sale_amount, salesman_id, customer_id, sale_date)
    )


def update_sale(cursor, sale_id, info, sale_amount, salesman_id, customer_id, sale_date):
    cursor.execute(
        "UPDATE Sales SET INFO = %s, SaleAmount = %s, Salesman_ID = %s, Customer_ID = %s, SaleDate = %s WHERE ID = %s",
        (info, sale_amount, salesman_id, customer_id, sale_date, sale_id)
    )


def delete_sale(cursor, sale_id):
    cursor.execute("DELETE FROM Sales WHERE ID = %s", (sale_id,))


def main():
    conn = connect()
    cursor = conn.cursor()

    while True:
        print("1. Display all sales")
        print("2. Display sales by salesman")
        print("3. Display maximum sale")
        print("4. Display minimum sale")
        print("5. Insert new sale")
        print("6. Update existing sale")
        print("7. Delete sale")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            display_all_sales(cursor)
        elif choice == '2':
            salesman_id = int(input("Enter Salesman ID: "))
            display_sales_by_salesman(cursor, salesman_id)
        elif choice == '3':
            display_max_sale(cursor)
        elif choice == '4':
            display_min_sale(cursor)
        elif choice == '5':
            info = input("Enter sale info: ")
            sale_amount = float(input("Enter sale amount: "))
            salesman_id = int(input("Enter Salesman ID: "))
            customer_id = int(input("Enter Customer ID: "))
            sale_date = input("Enter sale date (YYYY-MM-DD): ")
            insert_sale(cursor, info, sale_amount, salesman_id, customer_id, sale_date)
            conn.commit()
        elif choice == '6':
            sale_id = int(input("Enter Sale ID to update: "))
            info = input("Enter new sale info: ")
            sale_amount = float(input("Enter new sale amount: "))
            salesman_id = int(input("Enter new Salesman ID: "))
            customer_id = int(input("Enter new Customer ID: "))
            sale_date = input("Enter new sale date (YYYY-MM-DD): ")
            update_sale(cursor, sale_id, info, sale_amount, salesman_id, customer_id, sale_date)
            conn.commit()
        elif choice == '7':
            sale_id = int(input("Enter Sale ID to delete: "))
            delete_sale(cursor, sale_id)
            conn.commit()
        elif choice == '8':
            break
        else:
            print("Invalid choice. Please try again.")

    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()
