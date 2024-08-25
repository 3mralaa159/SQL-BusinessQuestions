# Question
  Write a query that will identify returning active users. A returning active user is a user that has made a second purchase within 7 days of any other of their purchases.
Output a list of user_ids of these returning active users.

# Link
  https://platform.stratascratch.com/coding/10322-finding-user-purchases?code_type=1

#Answer.1
select a.user_id , a.created_at as first_p , b.created_at as second_p
from amazon_transactions a 
join amazon_transactions b
on a.user_id = b.user_id
and a.created_at < b.created_at 
and b.created_at <= a.created_at+7 
and a.id <> b.id
order by 1 

# Answer.2
SELECT a1.user_id , a1.created_at , a2.created_at
FROM amazon_transactions a1
JOIN amazon_transactions a2 
ON a1.user_id=a2.user_id
AND a1.id <> a2.id
AND a2.created_at::date-a1.created_at::date BETWEEN 1 AND 7
ORDER BY a1.user_id
