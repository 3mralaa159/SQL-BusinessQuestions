# Question
  You have access to Facebook database which includes several tables relevant to user interactions.
  For this task, you are particularly interested in tables that store data about user posts, friendships, and likes.
  Calculate the total number of likes made on friend posts on Friday.
  The output should contain two different columns 'likes' and 'date'.

# Link
  https://platform.stratascratch.com/coding/10364-fridays-likes-count?code_type=1

# Answer
SELECT 
    COUNT(likes.post_id) AS likes, 
    DATE(likes.date_liked) AS date
FROM 
    likes
JOIN 
    user_posts ON likes.post_id = user_posts.post_id
JOIN 
    friendships ON (user_posts.user_name = friendships.user_name1 AND likes.user_name = friendships.user_name2) 
    OR (user_posts.user_name = friendships.user_name2 AND likes.user_name = friendships.user_name1)
WHERE 
    EXTRACT(DOW FROM date_liked) = 5
GROUP BY 
    DATE(likes.date_liked)
