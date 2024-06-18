-- Step 1: Identify relevant tables starting with vegeta_
WITH vegeta_tables AS (
    SELECT TABLE_NAME
    FROM INFORMATION_SCHEMA.TABLES
    WHERE TABLE_SCHEMA = 'YOUR_DATABASE_NAME'  -- Replace with your actual database name
      AND TABLE_NAME LIKE 'VEGETA_%'
),

-- Step 2: Get column information and count occurrences
column_counts AS (
    SELECT COLUMN_NAME,
           COUNT(*) AS num_occurrences,
           ARRAY_AGG(TABLE_NAME) AS tables_present
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_SCHEMA = 'YOUR_DATABASE_NAME'  -- Replace with your actual database name
      AND TABLE_NAME IN (SELECT TABLE_NAME FROM vegeta_tables)
    GROUP BY COLUMN_NAME
)

-- Step 3: Combine results to form the data dictionary
SELECT cc.COLUMN_NAME,
       cc.num_occurrences,
       ARRAY_JOIN(cc.tables_present, ', ') AS tables_present
FROM column_counts cc
ORDER BY cc.COLUMN_NAME;
