-- Importação dos dados da Steam
-- Ajuste o caminho e as colunas de acordo com o CSV tratado.

SET search_path TO steam;

-- Recomendação:
-- 1. Preserve o arquivo bruto em dados/original/.
-- 2. Gere um CSV tratado em dados/tratados/.
-- 3. Importe primeiro para uma tabela staging.
-- 4. A partir da staging, distribua os dados nas tabelas normalizadas.

-- Exemplo de fluxo:
--
-- CREATE TABLE steam.staging_jogos (...);
--
-- \copy steam.staging_jogos
-- FROM 'dados/tratados/steam_cleaned_2026_legivel.csv'
-- WITH (
--     FORMAT csv,
--     HEADER true,
--     DELIMITER ';',
--     ENCODING 'UTF8'
-- );
--
-- IMPORTANTE:
-- Não execute o exemplo acima antes de definir as colunas da staging
-- exatamente de acordo com o cabeçalho do arquivo CSV.
