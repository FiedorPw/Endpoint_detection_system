import sqlite3

# Ustanowienie połączenia z bazą danych SQLite
conn = sqlite3.connect('SQLite_Python.db')
cursor = conn.cursor()

# Tworzenie tabeli 'logs'
# cursor.execute('''
# CREATE TABLE logs (
#     rules VARCHAR(30),
#     descriptions VARCHAR(30),
#     times TEXT
# )
# ''')

# Dodawanie trzech rekordów do tabeli 'logs'
records = [
    ('First record',),
    ('Second record',),
    ('Third record',)
]

# cursor.executemany('INSERT INTO logs (rules) VALUES (?)', records)

"""Insert a Log instance into the logs table."""
sql = '''INSERT INTO logs (rules, descriptions, times) 
            VALUES (?, ?, ?)'''
cursor.execute(sql, ("first rule", "test description", "test time"))

# Zatwierdzenie zmian i zamknięcie połączenia
conn.commit()
conn.close()

# Informacja o zakończeniu operacji
"Trzy rekordy zostały dodane do tabeli 'logs'."
