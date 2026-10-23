USE steamdb;

SELECT
    YEAR(data_lancamento) AS ano,
    COUNT(*) AS jogos_lancados
FROM jogos
WHERE YEAR(data_lancamento) IN (2020, 2025)
GROUP BY YEAR(data_lancamento)
ORDER BY ano;
