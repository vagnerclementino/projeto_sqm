--Criando o ROLE
CREATE ROLE proj_sqm_usage_all_seq NOINHERIT;

--Garantindo acesso ao schema sqm
GRANT USAGE ON SCHEMA sqm TO proj_sqm_usage_all_seq;

--Garantindo SELECT em todas as tabelas
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA sqm TO proj_sqm_usage_all_seq;