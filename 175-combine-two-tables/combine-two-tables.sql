# Write your MySQL query statement below
select p.firstName, p.lastName, a.city, a.state from Address a right outer join Person p on p.personId = a.personId;