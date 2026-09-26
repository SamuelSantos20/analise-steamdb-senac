"""Análises exploratórias básicas da base Steam tratada."""

from pathlib import Path

import pandas as pd


def main() -> None:
    caminho = Path("dados/tratados/steam_tratado.csv")

    if not caminho.exists():
        print(f"Arquivo não encontrado: {caminho}")
        return

    df = pd.read_csv(caminho, sep=";", low_memory=False)

    print("Dimensões da base")
    print(f"Linhas: {len(df):,}")
    print(f"Colunas: {len(df.columns)}")

    print("\nColunas disponíveis:")
    for coluna in df.columns:
        print(f"- {coluna}")

    if "ano_lancamento" in df.columns:
        print("\nJogos por ano:")
        print(
            df["ano_lancamento"]
            .value_counts(dropna=False)
            .sort_index()
            .to_string()
        )

        comparacao = df[df["ano_lancamento"].isin([2020, 2025])]
        if not comparacao.empty:
            print("\nComparação 2020 x 2025:")
            print(
                comparacao.groupby("ano_lancamento")
                .size()
                .rename("quantidade_jogos")
                .to_string()
            )


if __name__ == "__main__":
    main()
