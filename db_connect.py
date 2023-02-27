from psycopg2 import OperationalError
import psycopg2

def connection_db(db_name, db_user,db_pass, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_pass,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
        cursor = connection.cursor()
        # cursor.execute('SELECT name,price FROM sneakers_db WHERE price >500') # find with price more 500BYN
        cursor.execute("SELECT name,price FROM sneakers_db WHERE name = 'Кроссовки AIR MAX 270 REACT'") # find needed model

        print(cursor.fetchall())
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")
    return connection


if __name__ == "__main__":
    connection_db('postgres', 'urname', 'urpass', '127.0.0.1', '5432')
