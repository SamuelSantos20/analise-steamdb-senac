"""Rotinas iniciais de limpeza da base Steam.

O script preserva o arquivo original e grava a versão tratada em outro caminho.
"""

from pathlib import Path

import pandas as pd


def carregar_csv(caminho: Path) -> pd.DataFrame:
    """Carrega o CSV tentando os separadores mais comuns do projeto."""
    try:
        return pd.read_csv(caminho, sep=";", low_memory=False)
    except Exception:
        return pd.read_csv(caminho, low_memory=False)


def adicionar_ano_lancamento(df: pd.DataFrame) -> pd.DataFrame:
    """Cria ano_lancamento sem substituir nenhuma coluna original."""
    resultado = df.copy()

    candidatos = [
        "Release date",
        "release_date",
        "Data de lançamento",
        "data_lancamento",
    ]

    coluna_data = next((c for c in candidatos if c in resultado.columns), None)

    if coluna_data is None:
        return resultado

    datas = pd.to_datetime(resultado[coluna_data], errors="coerce")
    resultado["ano_lancamento"] = datas.dt.year.astype("Int64")
    return resultado


def main() -> None:
    origem = Path("dados/original/steam.csv")
    destino = Path("dados/tratados/steam_tratado.csv")

    if not origem.exists():
        print(f"Arquivo não encontrado: {origem}")
        print("Coloque o CSV original em dados/original/ ou ajuste o caminho no script.")
        return

    df = carregar_csv(origem)
    df_tratado = adicionar_ano_lancamento(df)

    destino.parent.mkdir(parents=True, exist_ok=True)
    df_tratado.to_csv(destino, sep=";", index=False, encoding="utf-8-sig")

    print(f"Registros: {len(df_tratado):,}")
    print(f"Colunas: {len(df_tratado.columns)}")
    print(f"Arquivo salvo em: {destino}")


if __name__ == "__main__":
    main()
