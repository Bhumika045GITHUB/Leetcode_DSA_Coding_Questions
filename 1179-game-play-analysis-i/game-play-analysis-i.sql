# Write your MySQL query statement below
select player_id , event_date as first_login  from (select *,dense_rank() over (partition by player_id order by event_date) as rn from Activity) a
 where rn=1;
