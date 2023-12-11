import sqlite3

# Ustanowienie połączenia z bazą danych SQLite
conn = sqlite3.connect('SQLite_Python.db')
cursor = conn.cursor()

# Tworzenie tabeli 'logs'
cursor.execute('''
CREATE TABLE logs (
    text_field VARCHAR(30)
)
''')

# Dodawanie trzech rekordów do tabeli 'logs'
records = [
    ('First record',),
    ('Second record',),
    ('Third record',)
]

cursor.executemany('INSERT INTO logs (text_field) VALUES (?)', records)

# Zatwierdzenie zmian i zamknięcie połączenia
conn.commit()
conn.close()

# Informacja o zakończeniu operacji
"Trzy rekordy zostały dodane do tabeli 'logs'."
