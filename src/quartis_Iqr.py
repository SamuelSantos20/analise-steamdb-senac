import os

from pathlib import Path

import media
from dotenv import load_dotenv
import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

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

query_dlc = "SELECT preco FROM jogos"
dados_array = obter_dados_do_banco(query_dlc)


q1 = np.percentile(dados_array, 25)
q2 = np.percentile(dados_array, 50)
q3 = np.percentile(dados_array, 75)

print(f"\nPrimeiro Quartil (Q1): R$ {q1:.2f}")
print(f"Segundo Quartil (Mediana/Q2): R$ {q2:.2f}")
print(f"Terceiro Quartil (Q3): R$ {q3:.2f}")

media =media = np.mean(dados_array)

if q1 <= media <= q3:
    print("\nA média está DENTRO da faixa interquartil (entre Q1 e Q3).")
else:
    print("\nA média está FORA da faixa interquartil (fora de Q1 e Q3).")

plt.axvline(x=q1, color='green', linestyle='--', label=f'Q1:  {q1:.2f}')
plt.axvline(x=q3, color='orange', linestyle='--', label=f'Q3:  {q3:.2f}')
plt.legend()
plt.show()

###################################################

# Calcular Q1 e Q3
Q1 = np.percentile(dados_array, 25)
Q3 = np.percentile(dados_array, 75)

# Calcular IQR
IQR = Q3 - Q1

# Calcular Limites
limite_superior = Q3 + (1.5 * IQR)
limite_inferior = Q1 - (1.5 * IQR)

print(f"\n--- Limites de Outliers (Preços dos Produtos) ---")
print(f"Q1 (25%): R$ {Q1:.2f}")
print(f"Q3 (75%): R$ {Q3:.2f}")
print(f"IQR: R$ {IQR:.2f}")
print(f"Limite Superior (LS): R$ {limite_superior:.2f}")
print(f"Limite Inferior (LI): R$ {limite_inferior:.2f}")