# Write your MySQL query statement below

select u.name as NAME, sum(t.amount) as BALANCE from 
Users u INNER join  Transactions t on u.account=t.account
group by t.account
having  sum(t.amount)>10000;
