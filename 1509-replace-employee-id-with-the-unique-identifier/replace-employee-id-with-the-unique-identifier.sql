# Write your MySQL query statement below
select u.unique_id,  e.name from Employees E
Left join EmployeeUNI U on e.id=u.id