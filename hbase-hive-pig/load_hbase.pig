REGISTER /usr/lib/zookeeper/zookeeper-3.4.5-cdh4.3.0.jar
REGISTER /usr/lib/hbase/hbase-0.94.6-cdh4.3.0-security.jar

set hbase.zookeeper.quorum 'hue-search.ent.cloudera.com'

data = LOAD 'hbase://top_cool'
       USING org.apache.pig.backend.hadoop.hbase.HBaseStorage('review:*', '-loadKey true')
       as (name:CHARARRAY, dates:MAP[]);
 
counts = 
    FOREACH data
    GENERATE name, dates#'2012-12-02';

DUMP counts;

