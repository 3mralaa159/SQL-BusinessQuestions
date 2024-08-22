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
