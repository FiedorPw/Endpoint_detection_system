import sqlite3
import Logs

def insert_log_db(logs: Logs):
    # Ustanowienie połączenia z bazą danych SQLite
    conn = sqlite3.connect('SQLite_Python.db')
    log_cursor = conn.cursor()

    # Dodawanie trzech rekordów do tabeli 'logs'
    records = [
        (logs.rule,),
        (logs.description,),
        (logs.time,)
    ]

    """Insert a Log instance into the logs table."""
    sql = '''INSERT INTO logs (rules, descriptions, times) 
               VALUES (?, ?, ?)'''
    log_cursor.execute(sql, (logs.rule, logs.description, logs.time))
    conn.commit()
    conn.close()
    return log_cursor.lastrowid




try:
    sqliteConnection = sqlite3.connect('SQLite_Python.db')
    cursor = sqliteConnection.cursor()
    print("Database created and Successfully Connected to SQLite")

    sqlite_select_Query = "select sqlite_version();"
    cursor.execute(sqlite_select_Query)
    record = cursor.fetchall()
    print("SQLite Database Version is: ", record)

    sqlite_select_Query = "select * from logs;"
    cursor.execute(sqlite_select_Query)
    record = cursor.fetchall()
    print("SQLite Database Version is: ", record)




    cursor.execute("")
    cursor.close()

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("The SQLite connection is closed")
