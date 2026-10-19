import mysql.connector
import matplotlib.pyplot as plt
from pathlib import Path
from dotenv import load_dotenv
import polars as pl
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
        return resultados, cursor.column_names
    except mysql.connector.Error as erro:
        print(f"Erro ao conectar ao MySQL: {erro}")
        return None, None
    finally:
        if 'conexao' in locals() and conexao.is_connected():
            cursor.close()
            conexao.close()




query = '''
	SELECT
		YEAR(data_lancamento) AS ano,
		preco
	FROM jogos
'''

dados, colunas = obter_dados_do_banco(query)

if dados is None:
	raise SystemExit("Não foi possível obter os dados do banco.")

df = pl.DataFrame(
	dados,
	schema = colunas,
	orient = 'row'
)

medianas = (
	df
	.group_by("ano")
	.agg(
		pl.col("preco").median().alias('mediana_preco')
	)
	.sort('ano')
)

plt.figure(figsize = (10, 5))

plt.plot(
	medianas['ano'].to_list(),
	medianas['mediana_preco'].to_list(),
	marker = 'o'
)

plt.xlabel("ANO")
plt.ylabel("MEDIANA DE PREÇO")
plt.title("MEDIANA DE PREÇO POR ANO")
plt.grid(True)
plt.tight_layout()
plt.show()
