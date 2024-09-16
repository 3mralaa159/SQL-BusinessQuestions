# Question
Identify the number of employees within each department that share the same birth month.
  Your output should list the department, birth month, and the number of employees from that department who were born in that month.
  If a month has no employees born in it within a specific department, report this month as having 0 employees. The "profession" column stores the department names of each employee.

# Link
https://platform.stratascratch.com/coding/10355-employees-with-same-birth-month?code_type=1

# Answer.1
WITH RECURSIVE all_months AS (
    SELECT 1 AS birth_month
    UNION ALL
    SELECT birth_month + 1
    FROM all_months
    WHERE birth_month < 12
),
department_months AS (
    SELECT DISTINCT profession, all_months.birth_month
    FROM employee_list
    CROSS JOIN all_months
)
SELECT dm.profession,
       dm.birth_month,
       COALESCE(COUNT(el.employee_id), 0) AS employee_count
FROM department_months dm
left JOIN employee_list el
ON dm.profession = el.profession 
AND dm.birth_month = EXTRACT(MONTH FROM el.birthday)
GROUP BY dm.profession, dm.birth_month
ORDER BY dm.profession, dm.birth_month;


# Answer2.
# Using case
SELECT dm.profession,
       dm.birth_month,
       CASE 
           WHEN COUNT(el.employee_id) IS NULL THEN 0
           ELSE COUNT(el.employee_id)
       END AS employee_count
FROM department_months dm
LEFT JOIN employee_list el
ON dm.profession = el.profession 
   AND dm.birth_month = EXTRACT(MONTH FROM el.birthday)
GROUP BY dm.profession, dm.birth_month
ORDER BY dm.profession, dm.birth_month;
