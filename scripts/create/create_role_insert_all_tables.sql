--Criando o ROLE
CREATE ROLE proj_sqm_insert_all NOINHERIT;

--Garantindo acesso ao schema sqm
GRANT USAGE ON SCHEMA sqm TO proj_sqm_insert_all;

--Garantindo SELECT em todas as tabelas
GRANT INSERT ON ALL TABLES IN SCHEMA sqm TO proj_sqm_insert_all;