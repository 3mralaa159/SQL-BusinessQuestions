# Question
  Find the top 10 users that have traveled the greatest distance. Output their id, name and a total distance traveled.

# Link
  https://platform.stratascratch.com/coding/10324-distances-traveled?code_type=1

# Answer
select user_id , name , total
from (
select a.user_id , b.name , sum(a.distance) total , row_number() over(order by sum(a.distance) desc)
from lyft_rides_log a
join lyft_users b 
on a.user_id = b.id
group by 1 , 2 
order by 3 desc 
) p
where row_number <=10

# Answer.2
SELECT a.user_id, b.name, SUM(a.distance) AS total
FROM lyft_rides_log a
JOIN lyft_users b ON a.user_id = b.id
GROUP BY a.user_id, b.name
HAVING SUM(a.distance) >= (
    SELECT MIN(total)
    FROM (
        SELECT SUM(distance) AS total
        FROM lyft_rides_log
        GROUP BY user_id
        ORDER BY total DESC
        LIMIT 10
    ) t
)
ORDER BY total DESC;
