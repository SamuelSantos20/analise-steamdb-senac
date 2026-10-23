USE steamdb;

SELECT
    CASE
        WHEN preco = 0 THEN 'Gratuito'
        ELSE 'Pago'
    END AS tipo_jogo,
    COUNT(*) AS quantidade_jogos
FROM jogos
WHERE preco >= 0
GROUP BY tipo_jogo
ORDER BY quantidade_jogos DESC, tipo_jogo;
