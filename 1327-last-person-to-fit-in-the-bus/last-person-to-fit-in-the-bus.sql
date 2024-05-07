# Write your MySQL query statement below
select x.person_name
from (
select person_name ,
SUM(weight) OVER(ORDER BY turn ASC) AS total_weight
 from Queue) x
where x.total_weight <= 1000
order by x.total_weight desc 
limit 1;