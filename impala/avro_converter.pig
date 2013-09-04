
REGISTER piggybank.jar


data = load '/user/hive/warehouse/review/yelp_academic_dataset_review_clean.json'
    AS (funny:INT, useful:INT, cool:INT, user_id:CHARARRAY, review_id:CHARARRAY, text:CHARARRAY, business_id:CHARARRAY, stars:INT, date:CHARARRAY, type:CHARARRAY);
    
data_clean = FILTER data BY business_id IS NOT NULL AND text IS NOT NULL;    
    
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
      {"name":"text", "type":"string"},
      {"name":"business_id", "type":"string"},
      {"name":"stars", "type":"int"},
      {"name":"date", "type":"string"},      
      {"name":"type", "type":"string"},
   ]}
}'); 

