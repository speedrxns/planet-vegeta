-- Step 1: Identify tables starting with 'vegeta_' and not ending with '_bc'
WITH filtered_tables AS (
    SELECT TABLE_NAME,
           REGEXP_SUBSTR(TABLE_NAME, '_v(\\d+)$', 1, 1, 'e', 1)::INTEGER AS version_number
    FROM INFORMATION_SCHEMA.TABLES
    WHERE TABLE_SCHEMA = 'YOUR_DATABASE_NAME'  -- Replace with your actual database name
      AND TABLE_NAME LIKE 'vegeta_%'
      AND TABLE_NAME NOT LIKE '%_bc'
),

-- Step 2: Filter to get the table with the highest version number
highest_version_tables AS (
    SELECT ft.TABLE_NAME
    FROM filtered_tables ft
    WHERE NOT EXISTS (
        SELECT 1
        FROM filtered_tables ft2
        WHERE ft.TABLE_NAME = ft2.TABLE_NAME
          AND ft.version_number < ft2.version_number
    )
)

-- Step 3: Select the final list of table names
SELECT TABLE_NAME
FROM highest_version_tables;
