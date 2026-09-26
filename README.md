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

- PostgreSQL
- SQL
- Python
- Pandas
- Jupyter Notebook
- Git
- GitHub

## Estrutura do projeto

```text
analise-steamdb-senac/
│
├── dados/
│   ├── original/
│   └── tratados/
│
├── sql/
│   ├── criacao_tabelas.sql
│   ├── importacao_dados.sql
│   └── consultas.sql
│
├── notebooks/
│   └── analise_steam.ipynb
│
├── src/
│   ├── limpeza_dados.py
│   └── analise_dados.py
│
├── docs/
│   └── modelo_banco.md
│
├── resultados/
│   ├── graficos/
│   └── relatorios/
│
├── .gitignore
└── README.md
```

## Modelagem do banco de dados

A base será organizada no PostgreSQL utilizando um modelo relacional.

A estrutura inicial poderá ser dividida em tabelas como:

- jogos;
- empresas;
- jogos_empresas;
- gêneros;
- jogos_generos;
- categorias;
- jogos_categorias;
- tags;
- jogos_tags;
- idiomas;
- jogos_idiomas;
- plataformas;
- jogos_plataformas;
- mídias.

Essa divisão permite reduzir duplicações e organizar melhor informações que possuem múltiplos valores para um mesmo jogo.

## Etapas do projeto

1. Coleta da base de dados.
2. Análise inicial das colunas.
3. Limpeza e tratamento dos dados.
4. Criação da coluna de ano de lançamento.
5. Modelagem do banco de dados.
6. Criação das tabelas no PostgreSQL.
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
dados/original/
```

### Dados tratados

Arquivos utilizados após limpeza, organização ou criação de novas colunas.

```text
dados/tratados/
```

Essa separação permite preservar os dados originais e manter um histórico das transformações realizadas.

## Status do projeto

Projeto em desenvolvimento.

Atualmente estão sendo realizadas as etapas de:

- organização da base de dados;
- tratamento dos arquivos CSV;
- planejamento da modelagem no PostgreSQL;
- definição das análises que serão realizadas.

## Projeto acadêmico

Projeto desenvolvido para fins acadêmicos durante o curso do **Senac**, com foco em análise de dados, banco de dados e utilização de dados públicos relacionados à plataforma Steam.
