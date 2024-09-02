# Question
  Given a list of projects and employees mapped to each project, calculate by the amount of project budget allocated to each employee .
The output should include the project title and the project budget rounded to the closest integer. Order your list by projects with the highest budget per employee first.

# Link
  https://platform.stratascratch.com/coding/10301-expensive-projects?code_type=1

# Answer
SELECT
    p.title AS project_title,
    p.budget AS project_budget,
    ROUND(p.budget / COUNT(ep.emp_id)) AS budget_per_employee
FROM
    ms_projects p
JOIN
    ms_emp_projects ep ON p.id = ep.project_id
GROUP BY
    p.id, p.title, p.budget
ORDER BY
    budget_per_employee DESC;
