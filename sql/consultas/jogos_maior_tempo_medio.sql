USE steamdb;

SELECT
    jogo_id,
    nome,
    tempo_medio_jogo AS tempo_medio_minutos,
    tempo_mediano_jogo AS tempo_mediano_minutos
FROM jogos
WHERE tempo_medio_jogo > 0
ORDER BY tempo_medio_jogo DESC, jogo_id
LIMIT 10;
