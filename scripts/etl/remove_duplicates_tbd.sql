DELETE
FROM sqm.temp_bug_data t
where t.id_temp_bug_data
NOT IN (
SELECT tbd.id_temp_bug_data
FROM sqm.temp_bug_data tbd
where tbd.id_temp_bug_data = (SELECT MIN(tbd2.id_temp_bug_data)
				          FROM sqm.temp_bug_data tbd2
				         	WHERE tbd.bug_id = tbd2.bug_id
				         )
)
