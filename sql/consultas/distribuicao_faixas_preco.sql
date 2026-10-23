USE steamdb;

SELECT
    CASE
        WHEN preco = 0 THEN 'Gratuito'
        WHEN preco <= 5 THEN 'Ate US$ 5'
        WHEN preco <= 10 THEN 'Acima de US$ 5 ate US$ 10'
        WHEN preco <= 20 THEN 'Acima de US$ 10 ate US$ 20'
        WHEN preco <= 50 THEN 'Acima de US$ 20 ate US$ 50'
        ELSE 'Acima de US$ 50'
    END AS faixa_preco,
    COUNT(*) AS quantidade_jogos
FROM jogos
WHERE preco >= 0
GROUP BY faixa_preco
ORDER BY MIN(preco);
