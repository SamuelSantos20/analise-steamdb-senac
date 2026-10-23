# Análise de Dados da Steam — Senac

Projeto acadêmico desenvolvido no **Senac**, com tratamento de dados da Steam/SteamDB, modelagem e carga no MySQL, estatística descritiva, exploração com Python e Polars, regressão linear e visualização no Power BI Desktop.

## Etapas e situação atual

| Etapa | Entregas | Situação |
| --- | --- | --- |
| Organização e banco de dados | Planilhas, CSVs tratados, esquema MySQL, carga e relações | Arquivos e scripts disponíveis no repositório |
| Análises e estatística | Consultas SQL, gráficos, relatório executável, exploração em Parquet, dispersões e regressões | Scripts e notebooks disponíveis no repositório |
| Power BI | Modelo analítico, medidas DAX, filtros e oito páginas | Dashboard montado e salvo localmente; arquivos do BI ainda não versionados neste repositório |

O projeto continua em evolução. A organização dos dados, a modelagem e as análises já possuem implementação; não são apenas etapas planejadas.

## Base de dados e resultados documentados

A base tratada contém **114.172 jogos**, identificados pelo AppID (`jogo_id` no MySQL), com datas de lançamento entre **30/06/1997 e 05/01/2026**. Os dados incluem preços, avaliações, recomendações, DLCs, tempos de jogo, gêneros e plataformas. A planilha completa também contém informações usadas nas análises de popularidade, idiomas, categorias e empresas.

O [relatório de análise](notebooks/relatorio_analise_steam.ipynb) documenta:

- **8.733 lançamentos em 2020** e **21.680 em 2025**, crescimento de aproximadamente **148,3%** na base;
- **637.678 vínculos jogo–idioma** e **151.023 vínculos jogo–plataforma**;
- forte concentração das avaliações positivas, com valores extremos que justificam comparar média, mediana e quartis;
- consultas de verificação da integridade das chaves e associações.

Esses números representam a versão analisada da base, não uma consulta em tempo real à Steam. Os **84 registros de 2026** cobrem um período incompleto e não devem ser comparados diretamente com anos fechados.

## Tecnologias

- **MySQL e SQL:** armazenamento relacional, consultas e estatísticas.
- **Python, Pandas, NumPy e SciPy:** tratamento e estatística descritiva.
- **Polars e PyArrow/Parquet:** leitura, consultas lazy e exploração.
- **Matplotlib e Seaborn:** gráficos.
- **scikit-learn:** regressão linear e métricas de ajuste.
- **Jupyter Notebook:** análises executáveis.
- **Power BI Desktop e DAX:** relatório interativo.
- **Git e GitHub:** versionamento.

## Estrutura do repositório

```text
analise-steamdb-senac/
├── dados/
│   ├── originais/              # reservado; contém apenas .gitkeep
│   └── tratados/
│       ├── csv/                # jogos, catálogos e associações
│       ├── parquet/            # exportação da aba Jogos
│       └── planilhas/          # planilhas organizadas em XLSX
├── sql/
│   ├── esquema/               # criação do banco e das cinco tabelas
│   └── consultas/             # estatísticas de tempo de jogo
├── src/
│   ├── analises/              # estatística e gráficos via MySQL
│   ├── banco/                 # conexão e consulta de teste
│   └── carga/                 # carga, validação e exportação Parquet
├── notebooks/                 # relatório, exploração e regressões
├── resultados/
│   ├── graficos/              # quatro figuras PNG exportadas
│   └── relatorios/            # idiomas não mapeados
├── requirements.txt
├── .env.example
├── .gitignore
├── LICENSE
└── README.md
```

## Modelagem MySQL

| Tabela | Conteúdo |
| --- | --- |
| `jogos` | Um registro por jogo, com lançamento, preço, avaliações, DLCs, tempos, gêneros e idade mínima |
| `idiomas` | Catálogo de idiomas |
| `plataformas` | Catálogo de plataformas |
| `jogos_idiomas` | Relação muitos-para-muitos entre jogos e idiomas |
| `jogos_plataformas` | Relação muitos-para-muitos entre jogos e plataformas |

Os gêneros permanecem na coluna `generos` de `jogos`; não há tabela própria de gêneros no MySQL. Categorias e empresas usadas no Power BI pertencem ao modelo analítico do BI e não devem ser confundidas com tabelas já criadas neste banco.

## Como executar

### 1. Preparar o ambiente Python

Na raiz do repositório, crie um ambiente virtual:

```bash
python -m venv .venv
```

Ative-o no Windows/PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instale as dependências:

```bash
python -m pip install -r requirements.txt
python -m pip install scipy scikit-learn
```

A instalação adicional é necessária porque `assimetria.py` importa SciPy e os notebooks de regressão importam scikit-learn, mas esses pacotes ainda não estão declarados diretamente em `requirements.txt`.

Use um editor com suporte a Jupyter e selecione esse ambiente como kernel. Para usar JupyterLab, instale com `python -m pip install jupyterlab` e inicie com `python -m jupyter lab`.

### 2. Configurar e carregar o MySQL

Copie `.env.example` para `.env` na raiz e preencha `MYSQL_HOST`, `MYSQL_USER`, `MYSQL_PASSWORD` e `MYSQL_DATABASE`. O `.env` é ignorado pelo Git e deve permanecer local. Os scripts localizam esse arquivo pela raiz do projeto; variáveis já definidas no ambiente têm prioridade.

Com o MySQL disponível, execute os arquivos de [sql/esquema](sql/esquema) nesta ordem, selecionando o banco criado antes de criar as tabelas:

1. `CREATE DATABASE.sql`.
2. `CREATE TABLE JOGOS.sql`, `CREATE TABLE IDIOMAS.sql` e `CREATE TABLE PLATAFORMAS.sql`.
3. `CREATE TABLE JOGOS_IDIOMAS.sql` e `CREATE TABLE JOGOS_PLATAFORMAS.sql`.

Execute a partir da raiz:

```bash
python src/carga/carregar_dados.py
python src/carga/carregar_relacoes.py
python src/carga/carregar_relacoes.py --apply
```

O primeiro script lê os CSVs tratados com separador `;` e decimal `,`, atualizando registros existentes pela chave. Gêneros ausentes viram texto vazio.

O carregador de relações extrai os pares da planilha completa. Sem `--apply`, valida sem inserir e gera `resultados/relatorios/idiomas_nao_mapeados.csv`. Com `--apply`, insere os pares válidos; a carga pode ser repetida sem duplicá-los.

### 3. Executar os scripts de análise

Os scripts em [src/analises](src/analises) consultam o MySQL configurado no `.env`.

| Script | Análise |
| --- | --- |
| `grafico_barra.py` | Quantidade de lançamentos por ano |
| `grafico_linha.py` | Mediana do preço por ano de lançamento |
| `histograma.py` | Distribuição dos preços |
| `media_mediana.py` | Média e mediana dos preços dos jogos pagos |
| `quartis_Iqr.py` | Quartis, IQR e distribuição da quantidade de DLCs |
| `variancia_desvio_padrao.py` | Dispersão do tempo médio de jogo |
| `assimetria.py` | Distribuição, assimetria, curtose e boxplot das avaliações positivas |

Exemplo:

```bash
python src/analises/grafico_barra.py
```

As quatro figuras já exportadas estão em [resultados/graficos](resultados/graficos). O relatório incorpora essas imagens; executar novamente suas consultas não atualiza automaticamente as figuras incorporadas.

### 4. Usar Parquet e os notebooks

Para exportar a aba `Jogos` da planilha organizada:

```bash
python src/carga/exportar_parquet.py
```

A saída é `dados/tratados/parquet/steam_2026_organizada_PANDAS.parquet`.

| Notebook | Conteúdo |
| --- | --- |
| [relatorio_analise_steam.ipynb](notebooks/relatorio_analise_steam.ipynb) | Consultas MySQL, estatísticas, integridade das relações e quatro gráficos incorporados |
| [carregar_parquet.ipynb](notebooks/carregar_parquet.ipynb) | Consulta lazy com Polars, plano de execução e seleção dos lançamentos de 2025 |
| [barras_lacamento_por_ano.ipynb](notebooks/barras_lacamento_por_ano.ipynb) | Contagem anual de lançamentos com Polars |
| [grafico_dipercao.ipynb](notebooks/grafico_dipercao.ipynb) | Avaliações positivas versus pico de jogadores simultâneos em escala logarítmica |
| [regressao_lienar.ipynb](notebooks/regressao_lienar.ipynb) | Regressão do preço médio por ano de lançamento, com equação, R² e MSE |
| [correlacao_tempo_avaliacao.ipynb](notebooks/correlacao_tempo_avaliacao.ipynb) | Apesar do nome, analisa **preço versus pico de jogadores simultâneos**, com regressão, R² e RMSE |

Os nomes acima correspondem aos arquivos atuais. Os notebooks que leem `steam_2026_organizada_PANDAS.parquet` por caminho relativo devem ser executados com `notebooks` como diretório de trabalho, onde há uma cópia, ou ter o caminho ajustado para o Parquet em `dados/tratados/parquet`.

O notebook `correlacao_tempo_avaliacao.ipynb` usa um caminho do Google Colab: `/content/drive/MyDrive/Big Data/steam_2026_organizada.csv`. Para executar localmente, ajuste a origem e forneça um CSV com as colunas `Preço` e `Pico de jogadores simultâneos`. Esse CSV completo com esse nome não está incluído no repositório; `dados/tratados/csv/jogos.csv` não é uma substituição direta dessa entrada.

## Parte 3 — Power BI Desktop

O dashboard foi montado com os dados tratados, complementados pela planilha completa, e contém oito páginas:

1. **Visão geral:** catálogo, gratuitos, aprovação e comparação entre 2020 e 2025.
2. **Preços:** média e mediana dos pagos, mediana anual e distribuição por faixas.
3. **Avaliações:** distribuição em `ln(1 + avaliações positivas)`, quartis, assimetria e curtose.
4. **DLCs e tempo de jogo:** quartis, valores atípicos e medidas de dispersão.
5. **Preço e popularidade:** dispersões, correlação de Pearson, R² e RMSE.
6. **Regressão do preço por ano:** média anual observada e ajuste linear, com R² e MSE.
7. **Gêneros, idiomas e plataformas:** contagens distintas de jogos e filtros cruzados.
8. **Catálogo e empresas:** consulta por desenvolvedora, editora e categoria.

O arquivo principal é `SteamDB_Dashboard.pbix`. A pasta local de entrega `outputs/parte_3_powerbi` também contém `SteamDB.pbip`, pastas do relatório e do modelo semântico, CSVs de apoio, `medidas.dax`, `validacao_dados.json` e um guia próprio. **Essa pasta está fora deste repositório e ainda não foi publicada aqui.**

O PBIX pode ser aberto no Power BI Desktop sem workspace online. Para atualizar os dados ou usar o PBIP em outra máquina, disponibilize os arquivos de apoio e ajuste os caminhos locais das fontes no Power Query.

## Critérios de análise e limitações

- **Preços:** estatísticas de jogos pagos usam `preco > 0`; a mediana anual inclui gratuitos. A moeda não está explicitada na fonte.
- **Ano de lançamento:** o preço agrupado por ano descreve jogos lançados naquele ano; não é o histórico de mudanças de preço de um mesmo jogo.
- **Avaliações e popularidade:** avaliações e pico de jogadores simultâneos são medidas diferentes. Correlação e regressão não estabelecem causalidade.
- **DLCs:** quartis consideram `dlc_count > 0`; valores atípicos usam limites de 1,5 × IQR.
- **Tempo de jogo:** estatísticas consideram valores maiores que zero. Os scripts adotam minutos, mas a unidade precisa ser confirmada na fonte original; a variância fica na unidade ao quadrado.
- **Idiomas:** há 47 nomes sem correspondência no catálogo, registrados no relatório de validação e excluídos dos vínculos carregados.
- **Grupos sobrepostos:** um jogo pode ter vários gêneros, idiomas, plataformas ou empresas; somar esses grupos não produz o total de jogos distintos.
- **Visuais do BI:** quartis e extremos são apresentados em tabela como alternativa nativa ao boxplot. Dispersões podem reduzir os pontos exibidos; as medidas usam os pares válidos do recorte.

## Próximos ajustes

- Versionar ou disponibilizar a entrega do Power BI com instruções de atualização portáveis.
- Consolidar SciPy e scikit-learn em `requirements.txt`.
- Padronizar caminhos e nomes dos notebooks, incluindo a entrada vinculada ao Colab.
- Revisar os idiomas não mapeados antes de ampliar a cobertura das associações.

Projeto desenvolvido para fins acadêmicos, com foco em análise de dados, banco de dados e visualização de informações da Steam.
