import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mysql.connector
import os
from dotenv import load_dotenv
from pathlib import Path
import numpy as np
from scipy.stats import skew, kurtosis


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



# 1. Carregar os dados de produtos
query = 'SELECT avaliacoes_positivas FROM jogos'
resultados = obter_dados_do_banco(query)

if not resultados:
    raise SystemExit("Nenhum dado retornado do banco.")


dados_avaliacao = np.array(
    [linha[0] for linha in resultados if linha[0] is not None],
    dtype=float
)

# 2. Calcular Medidas
media_avaliacao = np.mean(dados_avaliacao)
mediana_avaliacao = np.median(dados_avaliacao)
std_avaliacao = np.std(dados_avaliacao,ddof=0) # Desvio padrão populacional



assimetria = sns.histplot(
    np.log1p(dados_avaliacao),
    kde=True,
    bins=50,
    color='skyblue'
)

plt.title('Distribuição das Avaliações Positivas — Escala Logarítmica')
plt.xlabel('log(1 + quantidade de avaliações positivas)')
plt.ylabel('Quantidade de jogos')
plt.show()
#skew(dados_avaliacao, bias=False)
curtose = kurtosis(dados_avaliacao, fisher=False, bias=False)
curtose_real_avaliacao = kurtosis(
    dados_avaliacao,
    fisher=False,
    bias=False
)



# 3. Painel de Resultados

print("-" * 50)
print("PAINEL: DISTRIBUIÇÃO DAS AVALIAÇÕES POSITIVAS DOS JOGOS")
print("-" * 50)
print(f"Média de avaliações positivas: {media_avaliacao:.2f}")
print(f"Mediana de avaliações positivas: {mediana_avaliacao:.2f}")
print(f"Desvio padrão das avaliações positivas: {std_avaliacao:.2f}")
print("-" * 50)

print(f"Assimetria: {assimetria:.4f}")

# Interpretação da assimetria
if assimetria > 0.5:
    print(" -> Assimetria positiva (cauda à direita). Alguns jogos com muitas avaliações positivas alongam a cauda à direita.")
elif assimetria < -0.5:
    print(" -> Assimetria negativa (cauda à esquerda). Jogos com quantidades menores de avaliações positivas alongam a cauda à esquerda.")
else:
    print(" -> Assimetria pequena pelo critério adotado. Isso, isoladamente, não garante uma distribuição simétrica.")

print(f"Curtose (referência 3, distribuição normal): {curtose_real_avaliacao:.4f}")

# Interpretação da curtose: faixas aproximadas
if curtose_real_avaliacao > 3.5:
    print(" -> Leptocúrtica. Forte influência de quantidades extremas de avaliações positivas, com caudas mais pesadas em relação à normal.")
elif curtose_real_avaliacao < 2.5:
    print(" -> Platicúrtica. Menor peso relativo dos valores extremos em comparação com a distribuição normal.")
else:
    print(" -> Aproximadamente mesocúrtica. Curtose próxima à referência da normal, sem garantir que a distribuição seja normal.")

print("-" * 50)
print("-" * 50)

# 4. Boxplot das avaliações positivas
plt.figure(figsize=(8, 4))
sns.boxplot(x=dados_avaliacao)

plt.title('Boxplot das Avaliações Positivas dos Jogos')
plt.xlabel('Quantidade de avaliações positivas')
plt.tight_layout()
plt.show()

# 5. Histograma com KDE das avaliações positivas
plt.figure(figsize=(10, 6))

sns.histplot(
    dados_avaliacao,
    kde=True,
    bins=30,
    color='skyblue',
    edgecolor='black',
    stat='density'
)

# Média e mediana das avaliações positivas
plt.axvline(
    media_avaliacao,
    color='red',
    linestyle='--',
    label=f'Média de avaliações positivas: {media_avaliacao:.2f}'
)

plt.axvline(
    mediana_avaliacao,
    color='green',
    linestyle=':',
    label=f'Mediana de avaliações positivas: {mediana_avaliacao:.2f}'
)

plt.text(
    0.95, 0.95,
    f'Assimetria: {assimetria:.2f}',
    transform=plt.gca().transAxes,
    fontsize=10,
    verticalalignment='top',
    horizontalalignment='right',
    bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5)
)

plt.text(
    0.95, 0.88,
    f'Curtose (referência 3): {curtose_real_avaliacao:.2f}',
    transform=plt.gca().transAxes,
    fontsize=10,
    verticalalignment='top',
    horizontalalignment='right',
    bbox=dict(boxstyle='round,pad=0.5', fc='lightgreen', alpha=0.5)
)

plt.title(
    'Distribuição das Avaliações Positivas dos Jogos',
    fontsize=14
)
plt.xlabel('Quantidade de avaliações positivas por jogo', fontsize=12)
plt.ylabel('Densidade', fontsize=12)
plt.legend()
plt.grid(axis='y', alpha=0.75)
plt.tight_layout()
plt.show()