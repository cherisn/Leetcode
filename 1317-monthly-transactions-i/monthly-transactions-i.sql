# Write your MySQL query statement below
/*
select month (trans_date) as month,
country, 
(Select count(*) from transactions group by trans_date)
as trans_count,
(select count(*) from transactions where state="approved")
as approved_count,
sum(amount) as trans_total_amount,
(select sum(amount) from transactions where state="approved")
as approved_total_amount
from transactions 
group by state
*/

/*
SELECT CONCAT(YEAR(trans_date), '-', LPAD(MONTH(trans_date), 2, '0')) as month,
country,
count(*) as trans_count,
sum(case when state = "approved" then 1 else 0 end) as approved_count,
sum(amount) as trans_total_amount,
sum(case when state="approved" then amount else 0 end) as approved_total_amount
from Transactions
group by MONTH(trans_date);
*/

SELECT 
    CONCAT(YEAR(trans_date), '-', LPAD(MONTH(trans_date), 2, '0')) AS month,
    country,
    COUNT(*) AS trans_count,
    SUM(CASE WHEN state = 'approved' THEN 1 ELSE 0 END) AS approved_count,
    SUM(amount) AS trans_total_amount,
    SUM(CASE WHEN state = 'approved' THEN amount ELSE 0 END) AS approved_total_amount
FROM 
    transactions
GROUP BY 
    CONCAT(YEAR(trans_date), '-', LPAD(MONTH(trans_date), 2, '0')), country;