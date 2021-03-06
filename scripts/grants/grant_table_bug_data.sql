GRANT SELECT ON sqm.bug_data TO proj_sqm_select_all;

GRANT INSERT ON sqm.bug_data TO proj_sqm_insert_all;

GRANT UPDATE ON sqm.bug_data TO proj_sqm_update_all;

GRANT DELETE ON sqm.bug_data TO proj_sqm_delete_all;

GRANT USAGE, SELECT ON SEQUENCE sqm.bug_data_id_bug_data_seq TO proj_sqm_usage_all_seq;