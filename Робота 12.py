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
import sqlite3


with open('config.json', 'r') as f:
    data = json.load(f)
    db_user = data['user']
    db_password = data['password']

db_url = f'postgresql+psycopg2://{db_user}:{db_password}@localhost:5432/Hospital'
engine = create_engine(db_url)


def create_database():
    conn = sqlite3.connect('Hospital.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Salesmen (
            salesman_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Customers (
            customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Sales (
            sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
            sale_amount DECIMAL(10, 2) NOT NULL,
            salesman_id INTEGER NOT NULL,
            customer_id INTEGER NOT NULL,
            FOREIGN KEY (salesman_id) REFERENCES Salesmen(salesman_id),
            FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
        )
    ''')

    conn.commit()
    conn.close()


def execute_query(query, params=None):
    conn = sqlite3.connect('Hospital.db')
    cursor = conn.cursor()
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results


def execute_insert_update_delete(query, params):
    conn = sqlite3.connect('Hospital.db')
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()
    conn.close()


def display_menu():
    print("1. Display all Hospital")
    print("2. Display Hospital of a specific salesman")
    print("3. Display the maximum Hospital amount")
    print("4. Display the minimum sale amount")
    print("5. Display the maximum sale amount for a specific salesman")
    print("6. Display the minimum sale amount for a specific salesman")
    print("7. Display the maximum sale amount for a specific customer")
    print("8. Display the minimum sale amount for a specific customer")
    print("9. Display the salesman with the maximum total sales amount")
    print("10. Display the salesman with the minimum total sales amount")
    print("11. Display the customer with the maximum total purchase amount")
    print("12. Display the average purchase amount for a specific customer")
    print("13. Display the average sale amount for a specific salesman")
    print("14. Insert new data")
    print("15. Update existing data")
    print("16. Delete data")
    print("17. Save results to a file")
    print("18. Exit")


def save_results_to_file(results, file_path):
    with open(file_path, 'w') as file:
        json.dump(results, file, indent=4)
    print(f"Results saved to {file_path}")


def main():
    create_database()

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            query = "SELECT * FROM Hospital"
            results = execute_query(query)
            for row in results:
                print(row)
        elif choice == '2':
            salesman_id = input("Enter salesman ID: ")
            query = "SELECT * FROM Hospital WHERE salesman_id = ?"
            results = execute_query(query, (salesman_id,))
            for row in results:
                print(row)
        elif choice == '3':
            query = "SELECT * FROM Hospital ORDER BY sale_amount DESC LIMIT 1"
            results = execute_query(query)
            for row in results:
                print(row)
        elif choice == '4':
            query = "SELECT * FROM Hospital ORDER BY sale_amount ASC LIMIT 1"
            results = execute_query(query)
            for row in results:
                print(row)
        elif choice == '5':
            salesman_id = input("Enter salesman ID: ")
            query = "SELECT * FROM Hospital WHERE salesman_id = ? ORDER BY sale_amount DESC LIMIT 1"
            results = execute_query(query, (salesman_id,))
            for row in results:
                print(row)
        elif choice == '6':
            salesman_id = input("Enter salesman ID: ")
            query = "SELECT * FROM Hospital WHERE salesman_id = ? ORDER BY sale_amount ASC LIMIT 1"
            results = execute_query(query, (salesman_id,))
            for row in results:
                print(row)
        elif choice == '7':
            customer_id = input("Enter customer ID: ")
            query = "SELECT * FROM Hospital WHERE customer_id = ? ORDER BY sale_amount DESC LIMIT 1"
            results = execute_query(query, (customer_id,))
            for row in results:
                print(row)
        elif choice == '8':
            customer_id = input("Enter customer ID: ")
            query = "SELECT * FROM Hospital WHERE customer_id = ? ORDER BY sale_amount ASC LIMIT 1"
            results = execute_query(query, (customer_id,))
            for row in results:
                print(row)
        elif choice == '9':
            query = "SELECT salesman_id, SUM(sale_amount) AS total_sales FROM Hospital GROUP BY salesman_id ORDER BY total_sales DESC LIMIT 1"
            results = execute_query(query)
            for row in results:
                print(row)
        elif choice == '10':
            query = "SELECT salesman_id, SUM(sale_amount) AS total_sales FROM Hospital GROUP BY salesman_id ORDER BY total_sales ASC LIMIT 1"
            results = execute_query(query)
            for row in results:
                print(row)
        elif choice == '11':
            query = "SELECT customer_id, SUM(sale_amount) AS total_purchases FROM Hospital GROUP BY customer_id ORDER BY total_purchases DESC LIMIT 1"
            results = execute_query(query)
            for row in results:
                print(row)
        elif choice == '12':
            customer_id = input("Enter customer ID: ")
            query = "SELECT AVG(sale_amount) FROM Hospital WHERE customer_id = ?"
            results = execute_query(query, (customer_id,))
            for row in results:
                print(row)
        elif choice == '13':
            salesman_id = input("Enter salesman ID: ")
            query = "SELECT AVG(sale_amount) FROM Hospital WHERE salesman_id = ?"
            results = execute_query(query, (salesman_id,))
            for row in results:
                print(row)
        elif choice == '14':
            table = input("Enter table (Hospital, Salesmen, Customers): ")
            if table == "Sales":
                sale_amount = input("Enter sale amount: ")
                salesman_id = input("Enter salesman ID: ")
                customer_id = input("Enter customer ID: ")
                query = "INSERT INTO Hospital (sale_amount, salesman_id, customer_id) VALUES (?, ?, ?)"
                execute_insert_update_delete(query, (sale_amount, salesman_id, customer_id))
            elif table == "Salesmen":
                name = input("Enter name: ")
                query = "INSERT INTO Salesmen (name) VALUES (?)"
                execute_insert_update_delete(query, (name,))
            elif table == "Customers":
                name = input("Enter name: ")
                email = input("Enter email: ")
                query = "INSERT INTO Customers (name, email) VALUES (?, ?)"
                execute_insert_update_delete(query, (name, email))
            else:
                print("Invalid table name.")
        elif choice == '15':
            table = input("Enter table (Hospital, Salesmen, Customers): ")
            if table == "Sales":
                sale_id = input("Enter sale ID: ")
                sale_amount = input("Enter new sale amount: ")
                query = "UPDATE Hospital SET sale_amount = ? WHERE sale_id = ?"
                execute_insert_update_delete(query, (sale_amount, sale_id))
            elif table == "Salesmen":
                salesman_id = input("Enter salesman ID: ")
                name = input("Enter new name: ")
                query = "UPDATE Salesmen SET name = ? WHERE salesman_id = ?"
                execute_insert_update_delete(query, (name, salesman_id))
            elif table == "Customers":
                customer_id = input("Enter customer ID: ")
                name = input("Enter new name: ")
                email = input("Enter new email: ")
                query = "UPDATE Customers SET name = ?, email = ? WHERE customer_id = ?"
                execute_insert_update_delete(query, (name, email, customer_id))
            else:
                print("Invalid table name.")
        elif choice == '16':
            table = input("Enter table (Sales, Salesmen, Customers): ")
            if table == "Sales":
                sale_id = input("Enter sale ID to delete: ")
                query = "DELETE FROM Hospital WHERE sale_id = ?"
                execute_insert_update_delete(query, (sale_id,))
            elif table == "Salesmen":
                salesman_id = input("Enter salesman ID to delete: ")
                query = "DELETE FROM Salesmen WHERE salesman_id = ?"
                execute_insert_update_delete(query, (salesman_id,))
            elif table == "Customers":
                customer_id = input("Enter customer ID to delete: ")
                query = "DELETE FROM Customers WHERE customer_id = ?"
                execute_insert_update_delete(query, (customer_id,))
            else:
                print("Invalid table name.")
        elif choice == '17':
            query = input("Enter the query to save results: ")
            results = execute_query(query)
            file_path = input("Enter the file path to save results: ")
            save_results_to_file(results, file_path)
        elif choice == '18':
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
