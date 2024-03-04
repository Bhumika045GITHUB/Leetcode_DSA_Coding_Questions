# rule for consecutive ques - is that no of consecutive , ()least three times consecutively) = no of self joins to make here 3 

select distinct a.num as ConsecutiveNums from Logs a join Logs b on
a.id=b.id+1 and a.num=b.num join Logs c on
a.id=c.id+2 and a.num=c.num;

