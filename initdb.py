import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS dividas')
cursor.execute('DROP TABLE IF EXISTS ganhos')

cursor.execute('''
CREATE TABLE dividas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    despesa TEXT,
    pagValor REAL,
    pagParcial REAL,
    faltaQuanto REAL,
    pagData TEXT
)
''')

cursor.execute('''
CREATE TABLE ganhos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ganhoValor REAL,
    descricao TEXT,
    ganhoData TEXT,
    descricaoServ TEXT
)
''')

conn.commit()
conn.close()

print('Banco recriado com sucesso')
