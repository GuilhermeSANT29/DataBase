from flask import Flask, request
import pyodbc
from datetime import datetime

# ======================================================
# FLASK
# ======================================================
app = Flask(__name__)

# ======================================================
# CONEXÃO SQL SERVER
# SUA INSTÂNCIA:
# .\SQLEXPRESS
# ======================================================
try:

    conn = pyodbc.connect(

        "DRIVER={SQL Server};"
        "SERVER=.\\SQLEXPRESS;"
        "DATABASE=TESTE_DB;"
        "Trusted_Connection=yes;"
    )

    cursor = conn.cursor()

    print("================================")
    print("CONECTADO AO SQL SERVER")
    print("================================")

except Exception as erro:

    print("================================")
    print("ERRO AO CONECTAR SQL SERVER")
    print(erro)
    print("================================")

# ======================================================
# HOME
# ======================================================
@app.route('/')
def home():

    return """
    <h1> API SQL Server Funcionando</h1>

    <p>API conectada ao banco de dados com sucesso.</p>

    <p>Use:</p>

    <p>
    /temperatura?sensor=SalaDev&temperatura=25
    </p>
    """

# ======================================================
# RECEBER TEMPERATURA
# ======================================================
@app.route('/temperatura')
def receber():

    try:

        # ======================================================
        # RECEBER DADOS
        # ======================================================
        sensor = request.args.get('sensor')

        temperatura = request.args.get('temperatura')

        # ======================================================
        # VALIDAR DADOS
        # ======================================================
        if sensor is None or temperatura is None:

            return "Erro: informe sensor e temperatura"

        # ======================================================
        # CONVERTER TEMPERATURA
        # ======================================================
        temperatura = float(temperatura)

        # ======================================================
        # DATA/HORA
        # ======================================================
        agora = datetime.now()

        # ======================================================
        # TERMINAL
        # ======================================================
        print("================================")
        print("NOVO DADO RECEBIDO")
        print("Sensor:", sensor)
        print("Temperatura:", temperatura)
        print("Data/Hora:", agora)
        print("================================")

        # ======================================================
        # INSERT SQL
        # ======================================================
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

        # ======================================================
        # SALVAR
        # ======================================================
        conn.commit()

        print("DADOS SALVOS SQL SERVER")

        return "OK"

    except Exception as erro:

        print("================================")
        print("ERRO")
        print(erro)
        print("================================")

        return "Erro ao salvar dados"

# ======================================================
# HISTÓRICO
# ======================================================
@app.route('/historico')
def historico():

    try:

        # ======================================================
        # CONSULTA SQL
        # ======================================================
        cursor.execute("""

            SELECT TOP 20
            nome_sensor,
            temperatura,
            data_hora

            FROM Temperaturas

            ORDER BY id DESC

        """)

        dados = cursor.fetchall()

        # ======================================================
        # HTML
        # ======================================================
        html = ""

        html += "<html>"

        html += "<head>"

        html += "<meta charset='UTF-8'>"

        html += "<meta http-equiv='refresh' content='60'>"

        html += "<title>Histórico</title>"

        html += "<style>"

        html += "body {"
        html += "background:#0f172a;"
        html += "font-family:Arial;"
        html += "color:white;"
        html += "text-align:center;"
        html += "}"

        html += "table {"
        html += "margin:auto;"
        html += "margin-top:40px;"
        html += "border-collapse:collapse;"
        html += "width:80%;"
        html += "background:#1e293b;"
        html += "}"

        html += "th, td {"
        html += "padding:15px;"
        html += "border:1px solid #334155;"
        html += "}"

        html += "th {"
        html += "background:#38bdf8;"
        html += "}"

        html += "</style>"

        html += "</head>"

        html += "<body>"

        html += "<h1>🌡 Últimas 20 Temperaturas</h1>"

        html += "<table>"

        html += "<tr>"
        html += "<th>Sensor</th>"
        html += "<th>Temperatura</th>"
        html += "<th>Data/Hora</th>"
        html += "</tr>"

        # ======================================================
        # MOSTRAR DADOS
        # ======================================================
        for linha in dados:

            html += "<tr>"

            html += f"<td>{linha[0]}</td>"

            html += f"<td>{linha[1]} °C</td>"

            html += f"<td>{linha[2]}</td>"

            html += "</tr>"

        html += "</table>"

        html += "</body>"

        html += "</html>"

        return html

    except Exception as erro:

        print(erro)

        return "Erro ao carregar histórico"

# ======================================================
# EXECUTAR API
# ======================================================
if __name__ == '__main__':

    app.run(
        host='0.0.0.0',
        port=5000
    )