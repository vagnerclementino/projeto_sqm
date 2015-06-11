CREATE OR REPLACE VIEW sqm.vw_tomcat7_componentes AS(
SELECT vw.product,
	  vw.product_version,
	  vw.component,
	  count(1) as Total_Bugs  
FROM sqm.vw_bugs_selecionados vw
WHERE vw.product = 'Tomcat 7'
AND   vw.product_version IN ('7.0.59','7.0.57')
group by vw.product,
	  vw.product_version,
	  vw.component
ORDER BY vw.product ASC,
	    vw.product_version DESC
);