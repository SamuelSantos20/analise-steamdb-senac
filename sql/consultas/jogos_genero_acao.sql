USE steamdb;

SELECT
    jogo_id,
    nome,
    data_lancamento,
    generos,
    preco AS preco_usd
FROM jogos
WHERE generos LIKE '%Action%'
ORDER BY data_lancamento DESC, jogo_id;
