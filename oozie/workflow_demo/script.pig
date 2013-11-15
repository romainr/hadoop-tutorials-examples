REGISTER piggybank.jar;

data = LOAD '$input' as (text:CHARARRAY);
upper_case =  FOREACH data GENERATE org.apache.pig.piggybank.evaluation.string.UPPER(text);

STORE upper_case INTO '$output' ;
