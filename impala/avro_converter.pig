REGISTER piggybank.jar


data = load '/user/hive/warehouse/review/yelp_academic_dataset_review_clean.json'
    AS (funny:INT, useful:INT, cool:INT, user_id:CHARARRAY, review_id:CHARARRAY,
        stars:INT, text:CHARARRAY, business_id:CHARARRAY, date:CHARARRAY, type:CHARARRAY);
   
data_clean = 
  FILTER data
  BY funny IS NOT NULL 
  AND useful IS NOT NULL
  AND cool IS NOT NULL
  AND user_id IS NOT NULL
  AND review_id IS NOT NULL
  AND business_id IS NOT NULL
  AND stars IS NOT NULL
  AND date IS NOT NULL
  AND type IS NOT NULL; 
    
STORE data_clean INTO 'impala/reviews_avro'
USING org.apache.pig.piggybank.storage.avro.AvroStorage(
'{
"schema": {
   "name": "review",
   "type": "record",
   "fields": [
      {"name":"funny", "type":"int"},
      {"name":"useful", "type":"int"},
      {"name":"cool", "type":"int"},
      {"name":"user_id", "type":"string"}
      {"name":"review_id", "type":"string"},
      {"name":"stars", "type":"int"},
      {"name":"text", "type":"string"},
      {"name":"business_id", "type":"string"},
      {"name":"date", "type":"string"},      
      {"name":"type", "type":"string"},
   ]}
}'); 

