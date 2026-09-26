-- Consultas iniciais para análise
SET search_path TO steam;

-- 1. Quantidade de jogos por ano
SELECT
    ano_lancamento,
    COUNT(*) AS quantidade_jogos
FROM jogos
WHERE ano_lancamento IS NOT NULL
GROUP BY ano_lancamento
ORDER BY ano_lancamento;

-- 2. Comparação entre 2020 e 2025
SELECT
    ano_lancamento,
    COUNT(*) AS quantidade_jogos,
    ROUND(AVG(preco), 2) AS preco_medio
FROM jogos
WHERE ano_lancamento IN (2020, 2025)
GROUP BY ano_lancamento
ORDER BY ano_lancamento;

-- 3. Gêneros com mais jogos
SELECT
    g.nome AS genero,
    COUNT(*) AS quantidade_jogos
FROM jogos_generos jg
JOIN generos g ON g.id_genero = jg.id_genero
GROUP BY g.id_genero, g.nome
ORDER BY quantidade_jogos DESC, genero;

-- 4. Desenvolvedoras com mais jogos
SELECT
    e.nome AS desenvolvedora,
    COUNT(DISTINCT je.app_id) AS quantidade_jogos
FROM jogos_empresas je
JOIN empresas e ON e.id_empresa = je.id_empresa
WHERE je.papel = 'desenvolvedora'
GROUP BY e.id_empresa, e.nome
ORDER BY quantidade_jogos DESC, desenvolvedora;

-- 5. Distribuição por plataforma
SELECT
    p.nome AS plataforma,
    COUNT(*) AS quantidade_jogos
FROM jogos_plataformas jp
JOIN plataformas p ON p.id_plataforma = jp.id_plataforma
GROUP BY p.id_plataforma, p.nome
ORDER BY quantidade_jogos DESC;

-- 6. Jogos com maior percentual de avaliações positivas
SELECT
    app_id,
    nome,
    avaliacoes_positivas,
    avaliacoes_negativas,
    ROUND(
        100.0 * avaliacoes_positivas /
        NULLIF(avaliacoes_positivas + avaliacoes_negativas, 0),
        2
    ) AS percentual_positivo
FROM jogos
WHERE COALESCE(avaliacoes_positivas, 0) + COALESCE(avaliacoes_negativas, 0) > 0
ORDER BY percentual_positivo DESC;
