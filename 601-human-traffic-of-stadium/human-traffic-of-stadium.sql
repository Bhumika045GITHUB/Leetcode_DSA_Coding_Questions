# here, conditions to note - having 3 column wont work, so use where ,
#consider all 3 edge case of 3 table joins


select DISTINCT s1.* from Stadium s1 join Stadium s2 join Stadium s3 on
(s1.id=s2.id+1 and s1.id = s3.id+2) or
(s1.id=s2.id-1 and s1.id = s3.id-2) or
(s1.id=s2.id+1 and s1.id = s3.id - 1)
where s1.people >= 100 and s2.people >= 100 and s3.people >= 100
order by s1.visit_date ;