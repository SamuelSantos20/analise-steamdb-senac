import os

from pathlib import Path
from dotenv import load_dotenv
import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from connect import obter_dados_do_banco

query_precos = "SELECT preco FROM jogos WHERE preco > 0"
dados_array =


q1 = np.percentile(precos_array, 25)
q2 = np.percentile(precos_array, 50)
q3 = np.percentile(precos_array, 75)

print(f"\nPrimeiro Quartil (Q1): R$ {q1:.2f}")
print(f"Segundo Quartil (Mediana/Q2): R$ {q2:.2f}")
print(f"Terceiro Quartil (Q3): R$ {q3:.2f}")

if q1 <= media <= q3:
    print("\nA média está DENTRO da faixa interquartil (entre Q1 e Q3).")
else:
    print("\nA média está FORA da faixa interquartil (fora de Q1 e Q3).")

plt.axvline(x=q1, color='green', linestyle='--', label=f'Q1: R$ {q1:.2f}')
plt.axvline(x=q3, color='orange', linestyle='--', label=f'Q3: R$ {q3:.2f}')
plt.axvline(x=media, color='red', linestyle='-', label=f'Média: R$ {media:.2f}')
plt.axvline(x=mediana, color='purple', linestyle='-', label=f'Mediana: R$ {mediana:.2f}')
plt.legend()
plt.show()

###################################################

# Calcular Q1 e Q3
Q1 = np.percentile(precos_array, 25)
Q3 = np.percentile(precos_array, 75)

# Calcular IQR
IQR = Q3 - Q1

# Calcular Limites
limite_superior = Q3 + (1.5 * IQR)
limite_inferior = Q1 - (1.5 * IQR)