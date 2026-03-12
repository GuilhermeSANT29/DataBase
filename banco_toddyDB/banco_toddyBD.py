import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="toddyDB"
)

print("Conectado ao banco!")

cursor = conexao.cursor()

cursor.execute("SELECT * FROM sensores")

for linha in cursor.fetchall():
    print(linha)