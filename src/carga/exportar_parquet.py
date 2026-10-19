#Exportação para .parquet com Pandas:

import os
from pathlib import Path

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

# --- 1. Configuração ---
raiz_projeto = Path(__file__).resolve().parents[2]
arquivo_xlsx = raiz_projeto / 'dados' / 'tratados' / 'planilhas' / 'steam_2026_organizada.xlsx'
arquivo_parquet = raiz_projeto / 'dados' / 'tratados' / 'parquet' / 'steam_2026_organizada_PANDAS.parquet'
chunksize = 1_000_000 # 1 milhão de linhas por vez

# --- 2. Verificação do Arquivo de Entrada ---
if not os.path.exists(arquivo_xlsx):
    print(f"ERRO: Arquivo de entrada não encontrado em: {arquivo_xlsx}")
else:
    print("Planilha encontrada. Iniciando conversão em chunks...")
    os.makedirs(arquivo_parquet.parent, exist_ok=True)

    # --- 3. Criar o Leitor (Iterator) ---
    df_planilha = pd.read_excel(
        arquivo_xlsx,
        sheet_name='Jogos'
    )
    xlsx_reader = (
        df_planilha.iloc[inicio:inicio + chunksize]
        for inicio in range(0, len(df_planilha), chunksize)
    )

    writer = None  # Inicializa o escritor de Parquet
    schema = None  # Inicializa o schema
    count = 0

    try:
        # --- 4. Loop de Leitura e Escrita ---
        for chunk in xlsx_reader:
            count += 1
            print(f"Processando chunk {count}...")

            # Converter o DataFrame do Pandas para uma Tabela do PyArrow
            table = pa.Table.from_pandas(chunk)

            if writer is None:
                # Na primeira volta, pegamos o schema e abrimos o escritor
                schema = table.schema
                writer = pq.ParquetWriter(arquivo_parquet, schema=schema)

            # Escreve o chunk (tabela) no arquivo Parquet
            writer.write_table(table)

        if writer is not None:
            writer.close()
            print(f"\nSucesso! Arquivo '{arquivo_parquet}' foi criado.")
        else:
            print("Planilha estava vazia. Nenhum arquivo Parquet foi criado.")

    except Exception as e:
        print(f"Ocorreu um erro no processamento: {e}")
        if writer is not None:
            writer.close() # Tenta fechar o arquivo em caso de erro
