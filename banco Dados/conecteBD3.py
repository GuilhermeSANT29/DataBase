import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="iot_monitoramento"
)

print("Conectado ao banco!")

cursor = conexao.cursor()

cursor.execute("SELECT * FROM leituras")

for linha in cursor.fetchall():
    print(linha)