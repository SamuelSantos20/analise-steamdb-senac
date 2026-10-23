USE steamdb;

SELECT
    COUNT(*) AS total_jogos,
    MIN(data_lancamento) AS primeiro_lancamento,
    MAX(data_lancamento) AS ultimo_lancamento
FROM jogos;
