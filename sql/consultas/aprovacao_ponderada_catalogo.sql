USE steamdb;

SELECT
    SUM(avaliacoes_positivas) AS total_avaliacoes_positivas,
    SUM(avaliacoes_negativas) AS total_avaliacoes_negativas,
    ROUND(
        100.0 * SUM(avaliacoes_positivas)
        / NULLIF(SUM(avaliacoes_positivas + avaliacoes_negativas), 0),
        2
    ) AS aprovacao_percentual
FROM jogos;
