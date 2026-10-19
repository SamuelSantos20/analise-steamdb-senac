USE steamdb;

CREATE TABLE jogos_idiomas (
    jogo_id BIGINT NOT NULL,
    idioma_id INT NOT NULL,
    PRIMARY KEY (jogo_id, idioma_id),
    CONSTRAINT fk_jogos_idiomas_jogo
        FOREIGN KEY (jogo_id) REFERENCES jogos (jogo_id),
    CONSTRAINT fk_jogos_idiomas_idioma
        FOREIGN KEY (idioma_id) REFERENCES idiomas (idioma_id)
);
