CREATE TABLE jogos(
    jogo_id BIGINT NOT NULL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL, 
    data_lancamento DATETIME , 
    preco DECIMAL(7,2) NOT NULL, 
    dlc_count INT NOT NULL, 
    avaliacoes_positivas INT NOT NULL, 
    avaliacoes_negativas INT NOT NULL, 
    recomendacoes INT NOT NULL, 
    metacritic_score INT, 
    tempo_medio_jogo INT NOT NULL, 
    tempo_mediano_jogo INT NOT NULL);
 