CREATE OR REPLACE VIEW sqm.vw_bug_all_componentes AS(
SELECT vw.product,
	  vw.product_version,
	  vw.component,
	  count(1) as Total_Bugs  
FROM sqm.vw_bugs_selecionados vw
group by vw.product,
	  vw.product_version,
	  vw.component
ORDER BY vw.product ASC,
	    vw.product_version DESC
);