INSERT INTO TABLE top_cool
SELECT r.business_id, name, SUM(cool) AS coolness, '${date}' as `date`
FROM review r JOIN business b
ON (r.business_id = b.business_id)
WHERE categories LIKE '%Restaurants%'
AND `date` = '${date}'
GROUP BY r.business_id, name
ORDER BY coolness DESC
LIMIT 10

