SELECT employee_id FROM salaries WHERE employee_id NOT IN (SELECT employee_id FROM employees) 
union all
select employee_id from employees where employee_id not in (select employee_id from salaries) order by employee_id;