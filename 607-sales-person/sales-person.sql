# Write your MySQL query statement below

select name from SalesPerson 
where name not in (
select distinct SalesPerson.name 
from SalesPerson 
left join Orders  on SalesPerson.sales_id =  Orders.sales_id

left join Company Company on Company.com_id = Orders.com_id
 
where Company.name = 'RED'
) ;