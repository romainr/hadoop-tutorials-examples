select b.business_id, cool, `date`, funny, review_id, b.stars, text, b.type, useful, user_id, name, city, full_address, latitude, longitude, neighborhoods, open, review_count, state
FROM review r join  business b on r.business_id = b.business_id
LIMIT 1000

