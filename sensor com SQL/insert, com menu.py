from flask import Flask, request
import pyodbc
from datetime import datetime

app = Flask(__name__)

# ======================================================
# CONFIGURAÇÃO DO BANCO
# ======================================================
def conectar():
    return pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=.\\SQLEXPRESS;"
        "DATABASE=TESTE_DB;"
        "UID=user_adm;"
        "PWD=123456;"
    )

# ======================================================
# TESTE DE CONEXÃO
# ======================================================
def testar_conexao():
    try:
        conn = conectar()
        print("✅ CONEXÃO OK COM SQL SERVER")
        conn.close()
    except Exception as e:
        print("❌ ERRO DE LOGIN:", e)

# ======================================================
# MENU TERMINAL
# ======================================================
def menu_terminal():
    while True:
        print("\n===== MENU =====")
        print("1 - Inserir nova temperatura")
        print("2 - Ver últimas temperaturas")
        print("0 - Sair")
        
        opcao = input("Escolha: ")

        if opcao == "1":
            try:
                sensor = input("Nome do sensor: ")
                temperatura = float(input("Temperatura: "))
                agora = datetime.now()

                conn = conectar()
                cursor = conn.cursor()

                cursor.execute(
                    """
                    INSERT INTO Temperaturas
                    (nome_sensor, temperatura, data_hora)
                    VALUES (?, ?, ?)
                    """,
                    sensor,
                    temperatura,
                    agora
                )

                conn.commit()
                conn.close()

                print("✅ DADO INSERIDO COM SUCESSO")

            except Exception as erro:
                print("❌ ERRO:", erro)

        elif opcao == "2":
            try:
                conn = conectar()
                cursor = conn.cursor()

                cursor.execute("""
                    SELECT TOP 10 nome_sensor, temperatura, data_hora
                    FROM Temperaturas
                    ORDER BY id DESC
                """)

                dados = cursor.fetchall()

                print("\n===== HISTÓRICO =====")
                for linha in dados:
                    print(f"{linha[0]} | {linha[1]}°C | {linha[2]}")

                conn.close()

            except Exception as erro:
                print("❌ ERRO:", erro)

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida")

# ======================================================
# API
# ======================================================
@app.route('/')
def home():
    return "<h1>API OK</h1><p>/temperatura?sensor=X&temperatura=Y</p>"

@app.route('/temperatura')
def receber():
    try:
        sensor = request.args.get('sensor')
        temperatura = request.args.get('temperatura')

        if not sensor or not temperatura:
            return "Erro: informe sensor e temperatura"

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO Temperaturas (nome_sensor, temperatura, data_hora) VALUES (?, ?, ?)",
            sensor,
            float(temperatura),
            datetime.now()
        )

        conn.commit()
        conn.close()

        return "OK"

    except Exception as erro:
        return f"Erro: {erro}"

@app.route('/historico')
def historico():
    try:
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT TOP 20 nome_sensor, temperatura, data_hora
            FROM Temperaturas
            ORDER BY id DESC
        """)

        dados = cursor.fetchall()
        conn.close()

        html = "<h1>Histórico</h1><table border=1>"
        html += "<tr><th>Sensor</th><th>Temp</th><th>Data</th></tr>"

        for linha in dados:
            html += f"<tr><td>{linha[0]}</td><td>{linha[1]}</td><td>{linha[2]}</td></tr>"

        html += "</table>"
        return html

    except Exception as erro:
        return f"Erro: {erro}"

# ======================================================
# EXECUÇÃO
# ======================================================
if __name__ == '__main__':

    print("\n===== INICIAR SISTEMA =====")
    print("1 - Rodar API (site)")
    print("2 - Menu no terminal")

    testar_conexao()

    escolha = input("Escolha: ")

    if escolha == "1":
        app.run(host='0.0.0.0', port=5000)

    elif escolha == "2":
        menu_terminal()

    else:
        print("Opção inválida")