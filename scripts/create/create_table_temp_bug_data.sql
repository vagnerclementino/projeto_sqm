CREATE TABLE sqm.temp_bug_data(

	id_temp_bug_data 		SERIAL NOT NULL,
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

ALTER TABLE sqm.temp_bug_data
ADD CONSTRAINT PK_TEMP_BUG_DATA
PRIMARY KEY (id_temp_bug_data);

COMMENT ON TABLE sqm.temp_bug_data
IS 'Tabela para armazenar temporariamente os dados coletados do ASF Bugzilla';

