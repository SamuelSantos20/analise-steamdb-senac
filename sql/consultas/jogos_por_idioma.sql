USE steamdb;

SELECT
    i.idioma_id,
    i.nome AS idioma,
    COUNT(DISTINCT ji.jogo_id) AS quantidade_jogos
FROM idiomas AS i
LEFT JOIN jogos_idiomas AS ji ON ji.idioma_id = i.idioma_id
GROUP BY i.idioma_id, i.nome
ORDER BY quantidade_jogos DESC, i.nome, i.idioma_id;
