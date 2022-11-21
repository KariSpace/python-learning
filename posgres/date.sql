'''PostgreSQL stores the timestamptz in UTC value. 

When you insert a value into a timestamptz column, PostgreSQL converts 
the timestamptz value into a UTC value and stores the UTC value in the table.

When you query timestamptz from the database, PostgreSQL converts the 
UTC value back to the time value of the timezone set by the database server, 
the user, or the current database connection.'''


CREATE TABLE timestamp_demo (
    ts TIMESTAMP, 
    tstz TIMESTAMPTZ
);

INSERT INTO timestamp_demo (ts, tstz)
VALUES('2016-06-22 19:10:25-07','2016-06-22 19:10:25-07');

SELECT 
   ts, tstz
FROM 
   timestamp_demo;


-- fuctionality:

SHOW TIMEZONE;
SET timezone = 'America/Los_Angeles';

SELECT NOW();
SELECT CURRENT_TIMESTAMP;
SELECT TIMEOFDAY();
SELECT timezone('America/New_York','2016-06-01 00:00');

SELECT * FROM pg_timezone_names;
SELECT * FROM pg_timezone_names WHERE name LIKE '%Kiev%';


-- Casting:
SELECT NOW() :: DATE;
SELECT CAST(NOW() AS DATE); -- MORE COMMON WAY

-- Intervals:
SELECT (NOW() - INTERVAL '2 days') :: DATE;

-- Date_trunk
SELECT DATE_TRUNK ('hour', TIMESTAMP '2017-03-17 02:09:27') 
-- date_trunk :  '2017-03-17 02:00:00

