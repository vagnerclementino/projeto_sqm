GRANT SELECT ON sqm.temp_bug_data TO proj_sqm_select_all;

GRANT INSERT ON sqm.temp_bug_data TO proj_sqm_insert_all;

GRANT UPDATE ON sqm.temp_bug_data TO proj_sqm_update_all;

GRANT DELETE ON sqm.temp_bug_data TO proj_sqm_delete_all;

GRANT USAGE, SELECT ON SEQUENCE sqm.temp_bug_data_id_temp_bug_data_seq TO proj_sqm_usage_all_seq;