data = 
   LOAD '/user/hive/warehouse/review/part-m-00000'
   AS (funny:INT, useful:INT, cool:INT, user_id:CHARARRAY, review_id:CHARARRAY,
       stars:INT, text:CHARARRAY, business_id:CHARARRAY, date:CHARARRAY, type:CHARARRAY);
       
ratings = 
  FOREACH data
  GENERATE
    funny,
    useful,
    cool,
    stars;
  
STORE ratings INTO 'review_stats' USING PigStorage(',');

