/*
Objetivo: Garantiar os acessos necesários para o usuário sqm
*/

--Garantindo SELECT para as tabelas
GRANT proj_sqm_select_all TO sqm;

--Garantindo acesso as sequences
GRANT proj_sqm_usage_all_seq TO sqm;

--garantindo insert nas tabelas
GRANT proj_sqm_insert_all TO sqm;

--Garantindo UPDATE nas tabelas
GRANT proj_sqm_update_all TO sqm;

--Garantindo DELETE nas tabelas
GRANT proj_sqm_delete_all TO sqm;