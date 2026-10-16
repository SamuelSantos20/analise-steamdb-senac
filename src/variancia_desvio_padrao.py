import os

from pathlib import Path

from dotenv import load_dotenv
import numpy as np
import mysql.connector

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

# Carregar os dados do banco (mesmo filtro da query em sql/ESTATISTICAS TEMPO MEDIO JOGO.sql)
query_tempo = "SELECT tempo_medio_jogo FROM jogos WHERE tempo_medio_jogo > 0"
resultados = obter_dados_do_banco(query_tempo)

if not resultados:
    raise SystemExit("Nenhum dado retornado do banco.")

# fetchall() retorna [(120,), (45,), ...] -> converte para array 1-D de float
dados_tempo = np.array([linha[0] for linha in resultados], dtype=float)

# Cálculo das medidas
media_tempo = dados_tempo.mean()
# Usando np.var com ddof=0 para calcular a variância populacional (equivale ao VAR_POP do MySQL)
variancia_tempo = np.var(dados_tempo, ddof=0)
# Usando np.std com ddof=0 para calcular o desvio padrão populacional (equivale ao STDDEV_POP do MySQL)
desvio_padrao_tempo = np.std(dados_tempo, ddof=0)

# Coeficiente de Variação (CV)
cv_tempo = (desvio_padrao_tempo / media_tempo) * 100

# Distância da Variância em relação à Média
distancia_tempo = variancia_tempo / (media_tempo ** 2)

print("--- Análise do Tempo Médio de Jogo ---")
print(f"\nQuantidade de Jogos: {len(dados_tempo)}")
print(f"Média do Tempo de Jogo: {media_tempo:.2f} min")
print(f"Variância do Tempo de Jogo: {variancia_tempo:.2f} min²")
print(f"Desvio Padrão do Tempo de Jogo: {desvio_padrao_tempo:.2f} min")
print("-" * 100)
print(f"Coeficiente de Variação (CV): {cv_tempo:.2f}%")
print(f"Distância da Variância / Média²: {distancia_tempo:.2f}")

# Análise de Dispersão
if distancia_tempo <= 0.10:
    analise_tempo = "Baixa dispersão dos dados em relação à média."
elif distancia_tempo < 0.25:
    analise_tempo = "Dispersão moderada dos dados em relação à média."
else:
    analise_tempo = "Alta dispersão dos dados em relação à média."

print(f"Conclusão da Dispersão: {analise_tempo}")

print("-" * 100)

# Conferência: mesma query agregada do arquivo SQL, calculada direto no MySQL
query_estatisticas = """
SELECT
    COUNT(*) AS quantidade_jogos,
    ROUND(AVG(tempo_medio_jogo), 2) AS media_tempo,
    ROUND(VAR_POP(tempo_medio_jogo), 2) AS variancia_tempo,
    ROUND(STDDEV_POP(tempo_medio_jogo), 2) AS desvio_padrao_tempo
FROM jogos
WHERE tempo_medio_jogo > 0
"""
estatisticas_sql = obter_dados_do_banco(query_estatisticas)

if estatisticas_sql:
    qtd_sql, media_sql, variancia_sql, desvio_sql = estatisticas_sql[0]
    print("--- Conferência com o MySQL ---")
    print(f"\nQuantidade (SQL): {qtd_sql}")
    print(f"Média (SQL): {float(media_sql):.2f} min")
    print(f"Variância (SQL): {float(variancia_sql):.2f} min²")
    print(f"Desvio Padrão (SQL): {float(desvio_sql):.2f} min")