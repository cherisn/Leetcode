# Write your MySQL query statement below
select DISTINCT activity_date as DAY,
COUNT(distinct user_id) as active_users
from activity
where activity_date between DATE_SUB('2019-07-27', INTERVAL 29 DAY) AND '2019-07-27'
GROUP BY activity_date;