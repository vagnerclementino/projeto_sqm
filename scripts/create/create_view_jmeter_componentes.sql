CREATE OR REPLACE VIEW sqm.vw_jmeter_componentes AS(
SELECT vw.product,
	  vw.product_version,
	  vw.component,
	  count(1) as Total_Bugs  
FROM sqm.vw_bugs_selecionados vw
WHERE  vw.product = 'JMeter'
and    vw.product_version in ('2.9', '2.8')
group by vw.product,
	  vw.product_version,
	  vw.component
ORDER BY vw.product ASC,
	    vw.product_version DESC
);