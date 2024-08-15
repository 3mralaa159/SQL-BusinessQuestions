# Question
  You have been asked to find the job titles of the highest-paid employees.
Your output should include the highest-paid title or multiple titles with the same salary.

# Link
  https://platform.stratascratch.com/coding/10353-workers-with-the-highest-salaries?code_type=2

# Answer
select a.worker_id ,  b.worker_title , a.salary
from worker a
join title b on a.worker_id = b.worker_ref_id
order by 3 desc
limit 2

# Answer.2
SELECT *
FROM
  (SELECT CASE
              WHEN salary =
                     (SELECT max(salary)
                      FROM worker) THEN worker_title
          END AS best_paid_title
   FROM worker a
   INNER JOIN title b ON b.worker_ref_id=a.worker_id
   ORDER BY best_paid_title) sq
WHERE best_paid_title IS NOT NULL

# Answer.3
SELECT
    worker_title AS best_paid_title 
FROM worker
JOIN title 
ON worker_id = worker_ref_id
WHERE salary=(SELECT MAX(salary) FROM worker)

# Answer.4
with ranked as (
select t.worker_title,
rank () over (order by w.salary desc) as r
from worker w
inner join title t on w.worker_id=t.worker_ref_id)

select * from ranked where r=1;
