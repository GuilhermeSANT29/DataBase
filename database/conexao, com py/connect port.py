import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="iot_monitoramento",
    port=3306
)

print("Conectado ao banco!")

cursor = conexao.cursor()

cursor.execute("SELECT * FROM leituras")

dados = cursor.fetchall()

print("Total de registros:", len(dados))
print("------------------------")

for linha in dados:
    print(linha)

cursor.close()
conexao.close()