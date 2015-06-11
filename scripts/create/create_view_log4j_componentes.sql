CREATE OR REPLACE VIEW sqm.vw_log4j_componentes AS(
SELECT vw.product,
	  vw.product_version,
	  vw.component,
	  count(1) as Total_Bugs  
FROM sqm.vw_bugs_selecionados vw
WHERE vw.product = 'Log4j'
AND   vw.product_version IN ('1.2.18','1.2.17')
group by vw.product,
	  vw.product_version,
	  vw.component
ORDER BY vw.product ASC,
	    vw.product_version DESC
);