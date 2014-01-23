!connect ${connectString} systest ${hive.password} org.apache.hive.jdbc.HiveDriver
select count(*) from ${tableName};
