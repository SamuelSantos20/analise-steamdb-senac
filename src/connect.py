import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import mysql.connector

def obter_dados_do_banco(query):
    try:
        conexao = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="steamdb"
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
query_jogos = "SELECT * FROM jogos"
dados_filtrados = obter_dados_do_banco(query_jogos)

if dados_filtrados:
    for jogos in dados_filtrados:
        print(jogos)