CREATE TABLE review_avro
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.avro.AvroSerDe'
STORED AS
inputformat 'org.apache.hadoop.hive.ql.io.avro.AvroContainerInputFormat'
outputformat 'org.apache.hadoop.hive.ql.io.avro.AvroContainerOutputFormat'
LOCATION '/user/romain/impala/reviews_avro'
tblproperties ('avro.schema.literal'='{
   "name": "review",
   "type": "record",
   "fields": [
      {"name":"business_id", "type":"string"},
      {"name":"cool", "type":"int"},
      {"name":"date", "type":"string"},
      {"name":"funny", "type":"int"},
      {"name":"review_id", "type":"string"},
      {"name":"stars", "type":"int"},
      {"name":"text", "type":"string"},
      {"name":"type", "type":"string"},
      {"name":"useful", "type":"int"},
      {"name":"user_id", "type":"string"}]}');

