/*select distinct customer_number from
(select * , dense_rank() over(order by cnt desc) as rnk from 
(select *, count(order_number) over(partition by customer_number) as cnt
 from Orders) a) b
 where rnk=1;*/

select customer_number 
from Orders
group by customer_number 
order by count(order_number) desc
limit 1;