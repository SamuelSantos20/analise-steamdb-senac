USE steamdb;

SELECT
    YEAR(data_lancamento) AS ano,
    COUNT(*) AS jogos_lancados
FROM jogos
GROUP BY YEAR(data_lancamento)
ORDER BY ano;
