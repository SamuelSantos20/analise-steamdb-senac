USE steamdb;

SELECT
    p.plataforma_id,
    p.nome AS plataforma,
    COUNT(DISTINCT jp.jogo_id) AS quantidade_jogos
FROM plataformas AS p
LEFT JOIN jogos_plataformas AS jp ON jp.plataforma_id = p.plataforma_id
GROUP BY p.plataforma_id, p.nome
ORDER BY quantidade_jogos DESC, p.nome, p.plataforma_id;
