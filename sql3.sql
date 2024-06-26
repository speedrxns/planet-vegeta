SELECT
    DATASET_NAME,
    DATE_TRUNC('day', LOAD_UTC_TIMESTAMP) AS LOAD_DATE,
    AVG(OVERALL_SUCCESS::INTEGER) AS SUCCESS_RATE
FROM
    your_table_name
GROUP BY
    DATASET_NAME,
    DATE_TRUNC('day', LOAD_UTC_TIMESTAMP)
ORDER BY
    DATASET_NAME,
    LOAD_DATE;



SELECT
    DATASET_NAME,
    DATE_TRUNC('day', LOAD_UTC_TIMESTAMP) AS LOAD_DATE,
    AVG(UNEXPECTED_PERCENT) AS AVG_UNEXPECTED_PERCENT
FROM
    your_table_name
GROUP BY
    DATASET_NAME,
    DATE_TRUNC('day', LOAD_UTC_TIMESTAMP)
ORDER BY
    DATASET_NAME,
    LOAD_DATE;


SELECT
    DATASET_NAME,
    DATE_TRUNC('day', LOAD_UTC_TIMESTAMP) AS LOAD_DATE,
    SEVERITY,
    COUNT(*) AS FAILURE_COUNT
FROM
    your_table_name
WHERE
    SUCCESS = 'False'
GROUP BY
    DATASET_NAME,
    DATE_TRUNC('day', LOAD_UTC_TIMESTAMP),
    SEVERITY
ORDER BY
    DATASET_NAME,
    LOAD_DATE,
    SEVERITY;


SELECT
    DATASET_NAME,
    DATE_TRUNC('day', LOAD_UTC_TIMESTAMP) AS LOAD_DATE,
    COUNT(*) AS TOTAL_CHECKS,
    SUM(CASE WHEN SUCCESS = 'True' THEN 1 ELSE 0 END) AS SUCCESS_COUNT,
    SUM(CASE WHEN SUCCESS = 'False' THEN 1 ELSE 0 END) AS FAILURE_COUNT
FROM
    your_table_name
GROUP BY
    DATASET_NAME,
    DATE_TRUNC('day', LOAD_UTC_TIMESTAMP)
ORDER BY
    DATASET_NAME,
    LOAD_DATE;


SELECT
    DATASET_NAME,
    DATE_TRUNC('day', LOAD_UTC_TIMESTAMP) AS LOAD_DATE,
    EXPECTATION,
    AVG(UNEXPECTED_PERCENT) AS AVG_UNEXPECTED_PERCENT
FROM
    your_table_name
WHERE
    EXPECTATION = 'your_specific_expectation'
GROUP BY
    DATASET_NAME,
    DATE_TRUNC('day', LOAD_UTC_TIMESTAMP),
    EXPECTATION
ORDER BY
    DATASET_NAME,
    LOAD_DATE;
