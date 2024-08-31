# Question
  Identify projects that are at risk for going overbudget. A project is considered to be overbudget 
if the cost of all employees assigned to the project is greater than the budget of the project.
You wil need to prorate the cost of the employees to the duration of the project. 
For example,
if the budget for a project that takes half a year to complete is $10K, then the total half-year salary of all employees assigned to the project should not exceed $10K.
Salary is defined on a yearly basis, so be careful how to calculate salaries for the projects that last less or more than one year.
Output a list of projects that are overbudget with their project name, project budget, and prorated total employee expense (rounded to the next dollar amount).

# Link
  https://platform.stratascratch.com/coding/10304-risky-projects?code_type=1

# Answer.1
with emp_m as (
select id , salary / 12 as salary 
from linkedin_employees
) , 
p_b_m as (
select a.project_id  , sum(b.salary) S
from linkedin_emp_projects a
join emp_m b on a.emp_id = b.id
group by 1  
order by 1 ),
final as(
select id , budget , ((end_date - start_date)/30)*S as required
from linkedin_projects a 
join p_b_m b on a.id = b.project_id)
select id , budget , required
from final 
where required > budget

# Answer.2
SELECT title,
       budget,
       ceiling(prorated_expenses) AS prorated_employee_expense
FROM
  (SELECT title,
          budget,
          (end_date::date - start_date::date) * (sum(salary)/365) AS prorated_expenses
   FROM linkedin_projects a
   INNER JOIN linkedin_emp_projects b ON a.id = b.project_id
   INNER JOIN linkedin_employees c ON b.emp_id=c.id
   GROUP BY title,
            budget,
            end_date,
            start_date) a
WHERE prorated_expenses > budget
ORDER BY title ASC
