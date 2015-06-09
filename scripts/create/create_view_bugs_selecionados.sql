CREATE OR REPLACE VIEW sqm.vw_bugs_selecionados AS

(SELECT 	bd.bug_id,
		bd.bug_status,
		bd.product,
		bd.product_version,
		bd.component,
		bd.hardware,
		bd.importance,
		bd.target_milestone,
		bd.assigned_to,
		bd.reported_date,
		bd.reported_by,
		bd.last_modification_date,
		bd.bug_description,
		bd.update_date

FROM sqm.bug_data bd
WHERE ( LOWER(bd.product_version) <> 'unspecified' ) 
AND    ( LOWER(bd.product_version) <> 'nightly')
AND   ( bd.product_version <>  'Nightly (Please specify date)') 
AND   ( LOWER(bd.product_version) <> 'trunk')

AND bd.bug_status IN 
			('ASSIGNED',
			'CLOSED FIXED',
			'CLOSED LATER',
			'CLOSED REMIND',
			'CLOSED WONTFIX',
			'NEEDINFO',
			'NEW',
			'REOPENED',
			'RESOLVED FIXED',
			'RESOLVED LATER',
			'RESOLVED REMIND',
			'RESOLVED WONTFIX',
			'VERIFIED FIXED')

)