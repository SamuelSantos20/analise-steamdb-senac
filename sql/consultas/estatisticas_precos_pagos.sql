USE steamdb;

SELECT
    COUNT(*) AS jogos_pagos,
    ROUND(AVG(preco), 2) AS preco_medio_usd,
    MIN(preco) AS preco_minimo_usd,
    MAX(preco) AS preco_maximo_usd
FROM jogos
WHERE preco > 0;
