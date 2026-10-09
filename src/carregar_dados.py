import os
from pathlib import Path

from dotenv import load_dotenv
import pandas as pd
import mysql.connector


load_dotenv(Path(__file__).resolve().parents[1] / ".env")

def conectar():
    # conexão com o banco de dados
    return mysql.connector.connect(
        host=os.environ["MYSQL_HOST"],
        user=os.environ["MYSQL_USER"],
        password=os.environ["MYSQL_PASSWORD"],
        database=os.environ["MYSQL_DATABASE"]
    )


def ler_csv(caminho_arquivo, colunas):
    df = pd.read_csv(caminho_arquivo, sep=';', encoding='utf-8', decimal=',')

    faltando = [c for c in colunas if c not in df.columns]
    if faltando:
        raise ValueError(f"Colunas ausentes em {caminho_arquivo}: {faltando}")

    df = df[colunas].astype(object)
    return df.where(pd.notnull(df), None)


def inserir_dados(sql, dados, tabela):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.executemany(sql, dados)
        conexao.commit()
        print(f"[{tabela}] {cursor.rowcount} registros inseridos com sucesso!")

    except mysql.connector.Error as erro:
        conexao.rollback()
        print(f"[{tabela}] Erro ao inserir dados: {erro}")

    finally:
        cursor.close()
        conexao.close()


# insere os dados na tabela jogos
def carregar_jogos(caminho_arquivo):
    colunas = [
        'jogo_id', 'nome', 'data_lancamento', 'preco', 'dlc_count',
        'avaliacoes_positivas', 'avaliacoes_negativas',
        'recomendacoes', 'metacritic_score', 'tempo_medio_jogo', 'tempo_mediano_jogo'
    ]
    df = ler_csv(caminho_arquivo, colunas)

    datas = pd.to_datetime(df['data_lancamento'], format='%d/%m/%Y', errors='coerce')
    df['data_lancamento'] = datas.dt.strftime('%Y-%m-%d').astype(object)
    df = df.where(pd.notnull(df), None)

    sql = """
        INSERT INTO jogos (
            jogo_id, nome, data_lancamento, preco, dlc_count,
            avaliacoes_positivas, avaliacoes_negativas,
            recomendacoes, metacritic_score, tempo_medio_jogo, tempo_mediano_jogo
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE nome = VALUES(nome) -- Opcional: atualiza se já existir
    """

    inserir_dados(sql, list(df.itertuples(index=False, name=None)), "jogos")

# insere os dados na tabela generos
def carregar_generos(caminho_arquivo):
    df = ler_csv(caminho_arquivo, ['genero_id', 'nome'])

    sql = """
        INSERT INTO generos (genero_id, nome)
        VALUES (%s, %s)
        ON DUPLICATE KEY UPDATE nome = VALUES(nome)
    """

    inserir_dados(sql, list(df.itertuples(index=False, name=None)), "generos")

# insere os dados na tabela idiomas
def carregar_idiomas(caminho_arquivo):
    df = ler_csv(caminho_arquivo, ['idioma_id', 'nome'])

    # A tabela idiomas não tem PRIMARY KEY: rodar duas vezes duplica os registros.
    sql = "INSERT INTO idiomas (idioma_id, nome) VALUES (%s, %s)"

    inserir_dados(sql, list(df.itertuples(index=False, name=None)), "idiomas")


# insere os dados na tabela plataformas
def carregar_plataformas(caminho_arquivo):
    df = ler_csv(caminho_arquivo, ['plataforma_id', 'nome'])

    # A tabela plataformas não tem PRIMARY KEY: rodar duas vezes duplica os registros.
    sql = "INSERT INTO plataformas (plataforma_id, nome) VALUES (%s, %s)"

    inserir_dados(sql, list(df.itertuples(index=False, name=None)), "plataformas")


# main
if __name__ == "__main__":
    # Caminhos para onde estão os CSVs
    carregar_jogos(r"")
    carregar_generos(r"")
    carregar_idiomas(r"")
    carregar_plataformas(r"")
