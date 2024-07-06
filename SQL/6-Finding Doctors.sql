# Question
  Find doctors with the last name of 'Johnson' in the employee list. The output should contain both their first and last names.
# Link
  https://platform.stratascratch.com/coding/10356-finding-doctors?code_type=1
# Answer
select first_name , last_name 
from employee_list
where last_name ='Johnson'
  order by 1
;
