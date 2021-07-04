"""
1. Створити 10 користувачів в БД за допомогою  insert
2. Вивести всіх у кого поштова скринька на gmail
3. Змінити пароль користувачу ID 4
4. Видалити користувача під іменем Bill (або якесь інше) 
5. Показати всіх користувачів у який ім'я починається на A

"""

import psycopg2
from psycopg2 import Error
from settings import *


def f_print(data):
    print("Result:")
    for i in range(len(data)):
        print(data[i])
    print('----------------------------------------------------------------')


try:
    connection = psycopg2.connect(user=USER,
                                  password=PASSWORD,
                                  host=HOST,
                                  port=PORT,
                                  database="user_db")
    # -----------------Підключення--------------------------------
    cursor = connection.cursor()
    print("PostgreSQL Server Information")
    print(connection.get_dsn_parameters(), "\n")
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("Are you connected to - ", record, "\n")

    # SQL-таблица------------------------------------
    create_table_query = '''CREATE TABLE if not exists user_table
                          (ID INT PRIMARY KEY     NOT NULL,
                          LOGIN           TEXT    NOT NULL,
                          EMAIL           TEXT    NOT NULL,
                          PASSWORD        TEXT    NOT NULL,
                          NAME            TEXT,     
                          AGE         INTEGER); '''

    cursor.execute(create_table_query)
    connection.commit()
    print("The table was successfully created in PostgreSQL")
    print('----------------------------------------------------------------')
    # --------------Добовлення даних в таблицю--------------------------
    # insert_query = """ INSERT INTO  user_table (ID, LOGIN, EMAIL, PASSWORD, NAME, AGE)
    #                                 VALUES
    #                                 (1, 'petrov', 'petrov@gmail.com','2556','Petya', 21),
    #                                 (2, 'roman', 'roman@gmail.com','dv356fdg','Roman', 30),
    #                                 (3, 'logo', 'oleg@ukr.net','vsdvcv','Oleg', 22),
    #                                 (4, 'kolis', 'kolis@gmail.com','25gdfg56','Kolis', 45),
    #                                 (5, 'lims', 'lims@ukr.net','26fsdf','Lism', 26),
    #                                 (6, 'arm', 'arm@gmail.com','arm_256','Armen', 29),
    #                                 (7, 'lito', 'lito@gmail.com','8956as','Lito', 23),
    #                                 (8, 'baswer', 'baswer@ukr.net','casdnkljns','Baswert', 61),
    #                                 (9, 'carden', 'carden@gmail.com','255sdfsd86','Carden', 52),
    #                                 (10, 'dragon', 'dragon@gmail.com','3565fasbv','Dragon', 19)

    #                 """
    # cursor.execute(insert_query)
    # connection.commit()
    # print("Record inserted successfully")
    # print('---------------------------------------------')
    # -----------Виводимо gmail ------------------------
    show_query = """Select * from user_table where EMAIL like '%gmail%'"""
    cursor.execute(show_query)
    f_print(cursor.fetchall())
    # -----------Зміна паролю ------------------------
    update_query = """Update user_table set PASSWORD = 'alfjkashdfkjsbhk' where id = 4"""
    cursor.execute(update_query)
    connection.commit()
    cursor.execute("SELECT * from user_table")
    f_print(cursor.fetchall())
    # -----------Видалення користувача ------------------------
    delete_query = """Delete from user_table where NAME = 'Oleg'"""
    cursor.execute(delete_query)
    connection.commit()
    count = cursor.rowcount
    print(count, "Entry successfully deleted")
    cursor.execute("SELECT * from user_table")
    f_print(cursor.fetchall())
    # -----------Виводимо користувачів з буквою 'А' -----------
    show_query_name = """Select * from user_table where NAME like 'A%'"""
    cursor.execute(show_query_name)
    f_print(cursor.fetchall())
    # -----------Сортування по ID ------------------------
    sort_query = """Select * from user_table ORDER BY LOGIN"""
    cursor.execute(sort_query)
    f_print(cursor.fetchall())
    # print("Result:", cursor.fetchall())
# -----------Видаляємо всю таблицю ------------------------
# update_query = """Delete from user_table"""
# cursor.execute(update_query)
# connection.commit()
# cursor.execute("SELECT * from user_table")
# print("Result:", cursor.fetchall())
# print('---------------------------------------------')
# -------------------------------------------------
except (Exception, Error) as error:
    print("Error while working with PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection closed")
