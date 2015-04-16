CREATE TABLE sqm.bug_list (
id_bug_list SERIAL NOT NULL,
bug_id	  INTEGER NOT NULL,
product	  VARCHAR(50) NOT NULL,
component   VARCHAR(80) NOT NULL,
assignee	  VARCHAR(100),
status	  VARCHAR(20),
resolution  VARCHAR(20),
summary	  VARCHAR(1000),
last_alter  TIMESTAMP,
last_update TIMESTAMP NOT NULL
);
 


ALTER TABLE sqm.bug_list
ADD CONSTRAINT PK_BUG_LIST PRIMARY KEY (id_bug_list);

ALTER TABLE sqm.bug_list
ADD CONSTRAINT UQ_bug_id UNIQUE (bug_id);



------------Inicio Comentários------------------------------------
COMMENT ON
TABLE sqm.bug_list
IS 'Tabela que armazena a lista de bug coletados do ASF Bugzilla';

COMMENT ON COLUMN
sqm.bug_list.id_bug_list
IS 'ID da tabela na forma de uma sequence/SERIAL';

COMMENT ON COLUMN
sqm.bug_list.bug_id
IS 'Indentificador único para um bug no ASF Bugzilla';

COMMENT ON COLUMN
sqm.bug_list.product
IS 'O nome da aplicação no qual ocorreu o bug';

COMMENT ON COLUMN
sqm.bug_list.component
IS 'O nome do componente da aplicação para o qual o erro foi reportado.';

COMMENT ON COLUMN
sqm.bug_list.assignee
IS 'Responsável por avaliar o bug relatado';

COMMENT ON COLUMN
sqm.bug_list.status
IS 'Indica o estado atual de um bug';

COMMENT ON COLUMN
sqm.bug_list.resolution
IS 'O campo de resolução indica o que aconteceu com um bug.';

COMMENT ON COLUMN
sqm.bug_list.summary
IS 'Uma breve descrição do bug';

COMMENT ON COLUMN
sqm.bug_list.last_alter
IS 'Data da última alteração ocorrida no bug relatado';

COMMENT ON COLUMN sqm.bug_list.last_update
IS 'Data de atualização do registro';
--------------------FIM COMENTAŔIOS-------------------
