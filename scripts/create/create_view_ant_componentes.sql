CREATE OR REPLACE VIEW sqm.vw_ant_componentes as(
SELECT
vw.product, vw.product_version, vw.component, count(1) AS Total_Bugs
FROM sqm.vw_bugs_selecionados vw
WHERE
(
   ((vw.product)::text = 'Ant'::text)
   AND
   (
      (
         vw.product_version
      )
      ::text = ANY
      (
         (ARRAY['1.9.4'::character varying, '1.9.3'::character varying])::text[]
      )
   )
)
GROUP BY vw.product, vw.product_version, vw.component
ORDER BY vw.product, vw.product_version DESC
);
