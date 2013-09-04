-- city, review_count, name, neighborhoods, type, business_id, full_address, state, longitude, stars, latitude, open, categories

REGISTER 'converter.py' USING jython AS converter;


reviews = LOAD 'yelp_academic_dataset_business.json' AS (line:CHARARRAY);

tsv = FOREACH reviews GENERATE converter.tsvify(line);

STORE tsv INTO 'yelp_academic_dataset_business.tsv';

