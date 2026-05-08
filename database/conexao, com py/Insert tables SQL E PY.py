import sqlite3

conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

cursor.execute("DROP TABLE IF EXISTS usuarios")

cursor.execute("""
CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    login TEXT,
    nome TEXT
)
""")

cursor.execute("INSERT INTO usuarios (login, nome) VALUES (?, ?)", ("admin", "Administrador"))
cursor.execute("INSERT INTO usuarios (login, nome) VALUES (?, ?)", ("william", "William Silva"))
cursor.execute("INSERT INTO usuarios (login, nome) VALUES (?, ?)", ("ana", "Ana Silva"))

conexao.commit()
conexao.close()

print("Banco criado com sucesso.")
