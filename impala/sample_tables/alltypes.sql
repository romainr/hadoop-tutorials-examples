CREATE DATABASE IF NOT EXISTS functional;
DROP TABLE IF EXISTS functional.alltypes;
CREATE EXTERNAL TABLE IF NOT EXISTS functional.alltypes (
id int COMMENT 'Add a comment',
bool_col boolean,
tinyint_col tinyint,
smallint_col smallint,
int_col int,
bigint_col bigint,
float_col float,
double_col double,
date_string_col string,
string_col string,
timestamp_col timestamp)
PARTITIONED BY (year int, month int)
ROW FORMAT delimited fields terminated by ','  escaped by '\\'
STORED AS TEXTFILE
LOCATION '/user/admin/alltypes/alltypes';

USE functional;
ALTER TABLE alltypes ADD IF NOT EXISTS PARTITION(year=2009, month=1);
ALTER TABLE alltypes ADD IF NOT EXISTS PARTITION(year=2009, month=2);
ALTER TABLE alltypes ADD IF NOT EXISTS PARTITION(year=2009, month=3);
ALTER TABLE alltypes ADD IF NOT EXISTS PARTITION(year=2009, month=4);
ALTER TABLE alltypes ADD IF NOT EXISTS PARTITION(year=2009, month=5);
ALTER TABLE alltypes ADD IF NOT EXISTS PARTITION(year=2009, month=6);
ALTER TABLE alltypes ADD IF NOT EXISTS PARTITION(year=2009, month=7);
ALTER TABLE alltypes ADD IF NOT EXISTS PARTITION(year=2009, month=8);
ALTER TABLE alltypes ADD IF NOT EXISTS PARTITION(year=2009, month=9);
ALTER TABLE alltypes ADD IF NOT EXISTS PARTITION(year=2009, month=10);
ALTER TABLE alltypes ADD IF NOT EXISTS PARTITION(year=2009, month=11);
ALTER TABLE alltypes ADD IF NOT EXISTS PARTITION(year=2009, month=12);

ALTER TABLE alltypes ADD IF NOT EXISTS PARTITION(year=2010, month=1);
ALTER TABLE alltypes ADD IF NOT EXISTS PARTITION(year=2010, month=2);
ALTER TABLE alltypes ADD IF NOT EXISTS PARTITION(year=2010, month=3);
ALTER TABLE alltypes ADD IF NOT EXISTS PARTITION(year=2010, month=4);
ALTER TABLE alltypes ADD IF NOT EXISTS PARTITION(year=2010, month=5);
ALTER TABLE alltypes ADD IF NOT EXISTS PARTITION(year=2010, month=6);
ALTER TABLE alltypes ADD IF NOT EXISTS PARTITION(year=2010, month=7);
ALTER TABLE alltypes ADD IF NOT EXISTS PARTITION(year=2010, month=8);
ALTER TABLE alltypes ADD IF NOT EXISTS PARTITION(year=2010, month=9);
ALTER TABLE alltypes ADD IF NOT EXISTS PARTITION(year=2010, month=10);
ALTER TABLE alltypes ADD IF NOT EXISTS PARTITION(year=2010, month=11);
ALTER TABLE alltypes ADD IF NOT EXISTS PARTITION(year=2010, month=12);
