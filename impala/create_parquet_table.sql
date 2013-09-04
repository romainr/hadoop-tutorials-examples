      
CREATE TABLE review_parquet LIKE review STORED AS PARQUETFILE;

INSERT OVERWRITE review_parquet  SELECT * FROM review;

