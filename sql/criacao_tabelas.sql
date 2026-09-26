-- Modelo relacional inicial do projeto SteamDB
-- PostgreSQL

CREATE SCHEMA IF NOT EXISTS steam;
SET search_path TO steam;

CREATE TABLE IF NOT EXISTS jogos (
    app_id BIGINT PRIMARY KEY,
    nome TEXT NOT NULL,
    data_lancamento DATE,
    ano_lancamento SMALLINT,
    descricao TEXT,
    preco NUMERIC(12,2),
    idade_minima INTEGER,
    conquistas INTEGER,
    dlcs INTEGER,
    proprietarios_estimados TEXT,
    avaliacoes_positivas INTEGER,
    avaliacoes_negativas INTEGER
);

CREATE TABLE IF NOT EXISTS empresas (
    id_empresa BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nome TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS jogos_empresas (
    app_id BIGINT NOT NULL REFERENCES jogos(app_id) ON DELETE CASCADE,
    id_empresa BIGINT NOT NULL REFERENCES empresas(id_empresa) ON DELETE CASCADE,
    papel VARCHAR(20) NOT NULL CHECK (papel IN ('desenvolvedora', 'publicadora')),
    PRIMARY KEY (app_id, id_empresa, papel)
);

CREATE TABLE IF NOT EXISTS generos (
    id_genero BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nome TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS jogos_generos (
    app_id BIGINT NOT NULL REFERENCES jogos(app_id) ON DELETE CASCADE,
    id_genero BIGINT NOT NULL REFERENCES generos(id_genero) ON DELETE CASCADE,
    PRIMARY KEY (app_id, id_genero)
);

CREATE TABLE IF NOT EXISTS categorias (
    id_categoria BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nome TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS jogos_categorias (
    app_id BIGINT NOT NULL REFERENCES jogos(app_id) ON DELETE CASCADE,
    id_categoria BIGINT NOT NULL REFERENCES categorias(id_categoria) ON DELETE CASCADE,
    PRIMARY KEY (app_id, id_categoria)
);

CREATE TABLE IF NOT EXISTS tags (
    id_tag BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nome TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS jogos_tags (
    app_id BIGINT NOT NULL REFERENCES jogos(app_id) ON DELETE CASCADE,
    id_tag BIGINT NOT NULL REFERENCES tags(id_tag) ON DELETE CASCADE,
    PRIMARY KEY (app_id, id_tag)
);

CREATE TABLE IF NOT EXISTS idiomas (
    id_idioma BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nome TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS jogos_idiomas (
    app_id BIGINT NOT NULL REFERENCES jogos(app_id) ON DELETE CASCADE,
    id_idioma BIGINT NOT NULL REFERENCES idiomas(id_idioma) ON DELETE CASCADE,
    suportado BOOLEAN NOT NULL DEFAULT TRUE,
    audio_completo BOOLEAN NOT NULL DEFAULT FALSE,
    PRIMARY KEY (app_id, id_idioma)
);

CREATE TABLE IF NOT EXISTS plataformas (
    id_plataforma BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nome TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS jogos_plataformas (
    app_id BIGINT NOT NULL REFERENCES jogos(app_id) ON DELETE CASCADE,
    id_plataforma BIGINT NOT NULL REFERENCES plataformas(id_plataforma) ON DELETE CASCADE,
    PRIMARY KEY (app_id, id_plataforma)
);

CREATE TABLE IF NOT EXISTS midias (
    id_midia BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    app_id BIGINT NOT NULL REFERENCES jogos(app_id) ON DELETE CASCADE,
    tipo VARCHAR(30) NOT NULL,
    url TEXT NOT NULL,
    ordem INTEGER
);

CREATE INDEX IF NOT EXISTS idx_jogos_ano ON jogos (ano_lancamento);
CREATE INDEX IF NOT EXISTS idx_jogos_preco ON jogos (preco);
CREATE INDEX IF NOT EXISTS idx_jogos_empresas_empresa ON jogos_empresas (id_empresa);
CREATE INDEX IF NOT EXISTS idx_jogos_generos_genero ON jogos_generos (id_genero);
CREATE INDEX IF NOT EXISTS idx_jogos_tags_tag ON jogos_tags (id_tag);
