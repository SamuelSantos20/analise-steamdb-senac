USE steamdb;

SELECT
    jogo_id,
    nome,
    avaliacoes_positivas,
    avaliacoes_negativas,
    avaliacoes_positivas + avaliacoes_negativas AS total_avaliacoes
FROM jogos
WHERE avaliacoes_positivas + avaliacoes_negativas > 0
ORDER BY total_avaliacoes DESC, jogo_id
LIMIT 10;
