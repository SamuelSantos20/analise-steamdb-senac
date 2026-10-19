USE steamdb;

CREATE TABLE jogos_plataformas (
    jogo_id BIGINT NOT NULL,
    plataforma_id INT NOT NULL,
    PRIMARY KEY (jogo_id, plataforma_id),
    CONSTRAINT fk_jogos_plataformas_jogo
        FOREIGN KEY (jogo_id) REFERENCES jogos (jogo_id),
    CONSTRAINT fk_jogos_plataformas_plataforma
        FOREIGN KEY (plataforma_id) REFERENCES plataformas (plataforma_id)
);
