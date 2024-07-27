# Question
  Write a query that calculates the difference between the highest salaries found in the marketing and engineering departments.
  Output just the absolute difference in salaries.
# Link
  https://platform.stratascratch.com/coding/10308-salaries-differences?code_type=1

# Answer 
SELECT
  ABS((SELECT max(salary)
   FROM db_employee emp
   JOIN db_dept dept ON emp.department_id = dept.id
   WHERE department = 'marketing') -
  (SELECT max(salary)
   FROM db_employee emp
   JOIN db_dept dept ON emp.department_id = dept.id
   WHERE department = 'engineering')) AS salary_difference
