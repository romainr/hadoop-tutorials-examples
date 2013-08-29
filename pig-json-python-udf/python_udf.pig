REGISTER 'converter.py' USING jython AS converter;


reviews = LOAD '/user/romain/yelp/yelp_academic_dataset_business.json' AS (line:CHARARRAY);

tsv = FOREACH reviews GENERATE converter.tsvify(line);

STORE tsv INTO 'yelp_academic_dataset_business2.tsv'

