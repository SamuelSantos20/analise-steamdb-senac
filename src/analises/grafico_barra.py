import mysql.connector
import matplotlib.pyplot as plt
from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv(Path(__file__).resolve().parents[2] / ".env")

def obter_dados_do_banco(query):
    try:
        conexao = mysql.connector.connect(
            host=os.environ["MYSQL_HOST"],
            user=os.environ["MYSQL_USER"],
            password=os.environ["MYSQL_PASSWORD"],
            database=os.environ["MYSQL_DATABASE"]
        )
        cursor = conexao.cursor()
        cursor.execute(query)
        resultados = cursor.fetchall()
        return resultados
    except mysql.connector.Error as erro:
        print(f"Erro ao conectar ao MySQL: {erro}")
        return None
    finally:
        if 'conexao' in locals() and conexao.is_connected():
            cursor.close()
            conexao.close()

query = '''
	SELECT YEAR(data_lancamento), COUNT(*)
	FROM jogos
	GROUP BY YEAR(data_lancamento)
	ORDER BY YEAR(data_lancamento);
'''

resultados = obter_dados_do_banco(query)

anos = [linha[0] for linha in resultados]
quantidades = [linha[1] for linha in resultados]

plt.bar(anos, quantidades)
plt.xlabel('ANO DE LANÇAMENTO')
plt.ylabel('JOGOS LANÇADOS')
plt.title('N. DE LANÇAMENTOS POR ANO')
plt.show()
