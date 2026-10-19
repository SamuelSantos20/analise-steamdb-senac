import os

from pathlib import Path

from dotenv import load_dotenv
import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

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

query_dlc = "SELECT dlc_count FROM jogos WHERE dlc_count >0"
resultados = obter_dados_do_banco(query_dlc)

if not resultados:
    raise SystemExit("Nenhum dado retornado do banco.")

# fetchall() retorna [(3,), (0,), ...] -> converte para array 1-D de float
dados_array = np.array([linha[0] for linha in resultados], dtype=float)

q1 = np.percentile(dados_array, 25)
q2 = np.percentile(dados_array, 50)
q3 = np.percentile(dados_array, 75)

print(f"\nPrimeiro Quartil (Q1): {q1:.2f} DLCs")
print(f"Segundo Quartil (Mediana/Q2): {q2:.2f} DLCs")
print(f"Terceiro Quartil (Q3): {q3:.2f} DLCs")

media = np.mean(dados_array)

if q1 <= media <= q3:
    print("\nA média está DENTRO da faixa interquartil (entre Q1 e Q3).")
else:
    print("\nA média está FORA da faixa interquartil (fora de Q1 e Q3).")

plt.hist(dados_array, bins=30, color='steelblue', alpha=0.7)
plt.axvline(x=q1, color='green', linestyle='--', label=f'Q1:  {q1:.2f}')
plt.axvline(x=q2, color='red', linestyle='-', label=f'Q2:  {q2:.2f}')
plt.axvline(x=q3, color='orange', linestyle='--', label=f'Q3:  {q3:.2f}')
plt.xlabel('Quantidade de DLCs')
plt.ylabel('Frequência')
plt.legend()
plt.show()

###################################################

# Reaproveita os quartis já calculados acima
Q1, Q3 = q1, q3

# Calcular IQR
IQR = Q3 - Q1

# Calcular Limites
limite_superior = Q3 + (1.5 * IQR)
limite_inferior = Q1 - (1.5 * IQR)

print(f"\n--- Limites de Outliers (Quantidade de DLCs) ---")
print(f"Q1 (25%): {Q1:.2f} DLCs")
print(f"Q3 (75%): {Q3:.2f} DLCs")
print(f"IQR: {IQR:.2f} DLCs")
print(f"Limite Superior (LS): {limite_superior:.2f} DLCs")
print(f"Limite Inferior (LI): {limite_inferior:.2f} DLCs")

outliers = dados_array[(dados_array < limite_inferior) | (dados_array > limite_superior)]
print(f"Outliers: {len(outliers)} de {len(dados_array)} jogos")
