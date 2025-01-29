

SELECT 
    query_name,
    ROUND(AVG(rating / position), 2) AS quality,

    ROUND(
        (SUM(CASE WHEN RATING<3 THEN 1 ELSE 0 END)/COUNT(*))*100
        ,2)
AS  poor_query_percentage
FROM queries
GROUP BY query_name
ORDER BY QUERY_NAME ASC;