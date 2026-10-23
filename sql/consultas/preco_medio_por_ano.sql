USE steamdb;

SELECT
    YEAR(data_lancamento) AS ano,
    COUNT(*) AS quantidade_jogos,
    ROUND(AVG(preco), 2) AS preco_medio_usd
FROM jogos
GROUP BY YEAR(data_lancamento)
ORDER BY ano;
