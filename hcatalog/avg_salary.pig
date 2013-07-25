-- Load table 'sample_07'
sample_07 = LOAD 'sample_07' USING org.apache.hcatalog.pig.HCatLoader();

-- Compute the average salary of the table
salaries = GROUP sample_07 ALL;
out = FOREACH salaries GENERATE AVG(sample_07.salary);
DUMP out;

