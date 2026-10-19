USE steamdb;

SELECT * FROM steamdb.jogos;

SELECT
    COUNT(*) AS quantidade_jogos,
    ROUND(AVG(tempo_medio_jogo), 2) AS media_tempo,
    ROUND(VAR_POP(tempo_medio_jogo), 2) AS variancia_tempo,
    ROUND(STDDEV_POP(tempo_medio_jogo), 2) AS desvio_padrao_tempo
FROM jogos
WHERE tempo_medio_jogo > 0;
