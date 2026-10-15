import polars as pl
import os

from pathlib import Path
from dotenv import load_dotenv
import matplotlib.pyplot as plt

import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


load_dotenv(Path(__file__).resolve().parents[1] / ".env")

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


query = 'SELECT preco FROM jogos'

dados = obter_dados_do_banco(query)

df = pl.DataFrame(dados, schema = ['preco'], orient = 'row')

precos = df['preco'].to_list()

plt.hist(precos, bins = 30)
plt.title('PREÇOS DOS JOGOS')
plt.xlabel('PREÇO')
plt.ylabel('QUANTIDADE DE JOGOS')
plt.show()
