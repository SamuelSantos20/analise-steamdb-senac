USE steamdb;

SELECT
    jogo_id,
    nome,
    dlc_count AS quantidade_dlcs
FROM jogos
WHERE dlc_count > 0
ORDER BY dlc_count DESC, jogo_id
LIMIT 10;
