import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="toddyDB",
    port=3306
)

print("Conectado ao banco!")

cursor = conexao.cursor()

cursor.execute("SELECT * FROM sensores")

dados = cursor.fetchall()

print("Total de registros:", len(dados))
print("------------------------")

for linha in dados:
    print(linha)

cursor.close()
conexao.close()