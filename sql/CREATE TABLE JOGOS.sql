CREATE TABLE jogos(
jogo_id VARCHAR(10) NOT NULL PRIMARY KEY,
 nome VARCHAR(100), 
 data_lancamento YEAR , 
 preco DECIMAL(7,2), 
 dlc_count INT, 
 avaliacoes_positivas INT, 
 avaliacoes_negativas INT, 
 recomendacoes INT, 
 metacritic_score INT, 
 tempo_medio_jogo INT, 
 tempo_mediano_jogo INT);
 