/*

  Copia os registros da tabela sqm.temp_bug_data para
  tabela sqm.bug_data.

*/



INSERT INTO sqm.bug_data(
SELECT *
FROM sqm.temp_bug_data

);

select count(1)
from sqm.bug_data;