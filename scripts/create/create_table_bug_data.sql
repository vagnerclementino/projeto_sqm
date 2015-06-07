CREATE TABLE sqm.bug_data(

	id_bug_data 			SERIAL NOT NULL,
	bug_id		  		INTEGER NOT NULL,
	bug_status       		VARCHAR(3000),
	product	 	  		VARCHAR(3000) NOT NULL,
	component		  		VARCHAR(3000) NOT NULL,
	hardware		  		VARCHAR(3000),
	importance	  		VARCHAR(3000),
	target_milestone 	 	VARCHAR(3000),
	assigned_to	  	   	VARCHAR(3000),
	reported_date	 	   	TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
	reported_by	  	   	VARCHAR(3000),
	last_modification_date 	TIMESTAMP WITH TIME ZONE,
	bug_description		TEXT,
	update_date 			TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()

);

ALTER TABLE sqm.bug_data
ADD CONSTRAINT PK_BUG_DATA
PRIMARY KEY (id_bug_data);

ALTER TABLE sqm.bug_data
ADD CONSTRAINT UQ_BUG_ID2
UNIQUE (bug_id);

CREATE INDEX idx_bd_bstatus
ON sqm.bug_data (bug_status);

CREATE INDEX idx_bd_product
ON sqm.bug_data (product);

CREATE INDEX idx_bd_component
ON sqm.bug_data (component);

CREATE INDEX idx_bd_repdate
ON sqm.bug_data (reported_date);

COMMENT ON TABLE sqm.bug_data
IS 'Tabela que armazena os dados dos bugs que foram coletados do ASF Bugzilla e posteriomente passaram por ETL';



