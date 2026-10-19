# Análise de Dados da Steam

Projeto desenvolvido no **Senac** com o objetivo de realizar uma análise de dados de jogos disponíveis na Steam, utilizando técnicas de tratamento, organização, modelagem e análise de dados.

## Objetivo do projeto

O projeto busca analisar informações relacionadas aos jogos da Steam para identificar padrões, tendências e comparações entre diferentes períodos.

Entre as análises previstas estão:

- quantidade de jogos lançados por ano;
- comparação entre os anos de 2020 e 2025;
- evolução dos lançamentos ao longo do tempo;
- gêneros mais frequentes;
- categorias mais utilizadas;
- preços dos jogos;
- avaliações dos usuários;
- desenvolvedoras e publicadoras;
- idiomas disponíveis;
- plataformas suportadas;
- relação entre preço, avaliação e popularidade;
- análise de jogos gratuitos e pagos.

## Base de dados

O projeto utiliza bases de dados relacionadas à Steam e ao SteamDB.

Os dados possuem informações como:

- AppID;
- nome do jogo;
- data de lançamento;
- ano de lançamento;
- preço;
- avaliações;
- gêneros;
- categorias;
- tags;
- desenvolvedoras;
- publicadoras;
- idiomas;
- plataformas;
- quantidade de conquistas;
- quantidade de DLCs;
- estimativa de proprietários;
- imagens e mídias relacionadas aos jogos.

Os dados originais serão mantidos separados dos dados tratados para preservar a integridade da fonte.

## Tecnologias utilizadas

- MySQL
- SQL
- Python
- Pandas
- Jupyter Notebook
- Git
- GitHub

## Estrutura do projeto

```text
analise-steamdb-senac/
├── dados/
│   ├── originais/              # reservado para arquivos brutos
│   └── tratados/
│       ├── csv/               # arquivos usados na carga do banco
│       ├── parquet/           # exportação da planilha em Parquet
│       └── planilhas/         # versões XLSX dos dados tratados
├── sql/
│   ├── esquema/              # criação do banco e das tabelas
│   └── consultas/            # consultas de análise
├── src/
│   ├── analises/             # estatísticas e gráficos em Python
│   ├── banco/                # consulta e conexão de teste
│   └── carga/                # importação e exportação dos dados
├── notebooks/                # relatório executável da análise
├── resultados/
│   ├── graficos/             # figuras das análises
│   └── relatorios/           # resultados tabulares da validação
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Modelagem do banco de dados

A base é carregada no MySQL utilizando um modelo relacional.

A estrutura contém as tabelas `jogos`, `idiomas` e `plataformas`, além de `jogos_idiomas` e `jogos_plataformas` para as relações muitos-para-muitos. Os gêneros ficam na coluna `generos` de `jogos`, sem tabela própria.

Para uma evolução futura da modelagem, outras entidades poderão ser separadas em tabelas como:

- empresas;
- jogos_empresas;
- categorias;
- jogos_categorias;
- tags;
- jogos_tags;
- mídias.

Essa divisão permite reduzir duplicações e organizar melhor informações que possuem múltiplos valores para um mesmo jogo.

## Etapas do projeto

1. Coleta da base de dados.
2. Análise inicial das colunas.
3. Limpeza e tratamento dos dados.
4. Criação da coluna de ano de lançamento.
5. Modelagem do banco de dados.
6. Criação das tabelas no MySQL.
7. Importação dos dados.
8. Criação de consultas SQL.
9. Análise exploratória dos dados.
10. Criação de gráficos e indicadores.
11. Comparação entre períodos.
12. Documentação dos resultados.

## Análises previstas

Algumas perguntas que o projeto pretende responder:

- Quantos jogos foram lançados em cada ano?
- Quais gêneros possuem mais jogos?
- Quais anos tiveram maior número de lançamentos?
- Qual foi a diferença entre 2020 e 2025?
- Quais jogos possuem melhores avaliações?
- Existe relação entre preço e avaliação?
- Quais desenvolvedoras possuem mais jogos publicados?
- Quais plataformas aparecem com maior frequência?
- Qual a proporção entre jogos gratuitos e pagos?

## Organização dos dados

Os arquivos serão separados em duas categorias:

### Dados originais

Arquivos obtidos diretamente da fonte, sem alterações.

```text
dados/originais/
```

### Dados tratados

Arquivos utilizados após limpeza, organização ou criação de novas colunas.

```text
dados/tratados/csv/
dados/tratados/parquet/
dados/tratados/planilhas/
```

Essa separação permite preservar os dados originais e manter um histórico das transformações realizadas.

## Status do projeto

Projeto em desenvolvimento.

Atualmente estão sendo realizadas as etapas de:

- organização da base de dados;
- tratamento dos arquivos CSV;
- planejamento da modelagem no MySQL;
- definição das análises que serão realizadas.

## Projeto acadêmico

Projeto desenvolvido para fins acadêmicos durante o curso do **Senac**, com foco em análise de dados, banco de dados e utilização de dados públicos relacionados à plataforma Steam.

## Configuração da conexão MySQL

Instale as dependências com `pip install -r requirements.txt`. Copie `.env.example` para `.env` na raiz do projeto e preencha `MYSQL_HOST`, `MYSQL_USER`, `MYSQL_PASSWORD` e `MYSQL_DATABASE`.

O carregador lê esse arquivo independentemente da pasta de execução. Variáveis já definidas no ambiente têm prioridade. O `.env` é ignorado pelo Git e deve permanecer apenas na sua máquina.

Crie o banco com `CREATE DATABASE.sql`. Execute os scripts de `jogos`, `idiomas` e `plataformas` antes dos scripts `JOGOS_IDIOMAS` e `JOGOS_PLATAFORMAS`, pois as chaves estrangeiras dependem das tabelas principais. Depois execute `python src/carga/carregar_dados.py` a partir da raiz do projeto. O carregador usa os três arquivos de `dados/tratados/csv/` por caminhos relativos ao projeto. O CSV de jogos já contém `generos` e `idade_minima`; gêneros ausentes são carregados como texto vazio.

Para preencher as tabelas de associação a partir de `dados/tratados/planilhas/steam_2026_organizada.xlsx`, execute `python src/carga/carregar_relacoes.py` para validar os dados e gerar `resultados/relatorios/idiomas_nao_mapeados.csv`. Depois execute `python src/carga/carregar_relacoes.py --apply` para inserir os pares válidos. A carga pode ser repetida sem duplicar os pares.

As tabelas de conexão são definidas em `sql/esquema/CREATE TABLE JOGOS_IDIOMAS.sql` e `sql/esquema/CREATE TABLE JOGOS_PLATAFORMAS.sql`.

Os scripts de análise ficam em `src/analises/`; o script de consulta de teste fica em `src/banco/`. Execute cada script com `python src/analises/NOME_DO_SCRIPT.py`. Os quatro gráficos fornecidos para o projeto estão em `resultados/graficos/`.

O relatório executável com as consultas, resultados e quatro gráficos está em `notebooks/relatorio_analise_steam.ipynb`.

Para gerar a versão Parquet da aba `Jogos` da planilha, execute `python src/carga/exportar_parquet.py`. O arquivo resultante fica em `dados/tratados/parquet/`.
