import os

from pathlib import Path
from dotenv import load_dotenv
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

# Usando a função
query_precos = "SELECT preco FROM jogos WHERE preco > 0"
dados_filtrados = obter_dados_do_banco(query_precos)
media_precos = np.mean(dados_filtrados)
mediana_precos = np.median(dados_filtrados)

print(f"Média dos preços: {media_precos}")
print(f"Mediana dos preços: {mediana_precos}")

if dados_filtrados:
    for jogos in dados_filtrados:
        print(jogos) 