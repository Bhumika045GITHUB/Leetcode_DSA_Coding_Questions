# Write your MySQL query statement below

with cte as(
select *, lead(student) over(order by id) as next_student, lag(student) over(order by id) as prev_student 
from seat)

select id, 
case when (id%2 = 0) then prev_student else coalesce(next_student,student) end as student
from cte;
