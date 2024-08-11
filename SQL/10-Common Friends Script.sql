# Question
  You are analyzing a social network dataset at Google. Your task is to find mutual friends between two users, Karl and Hans.
  There is only one user named Karl and one named Hans in the dataset.
  The output should contain 'user_id' and 'user_name' columns.

# Link
  https://platform.stratascratch.com/coding/10365-common-friends-script?code_type=1

# Answer
SELECT user_id, user_name 
FROM users
WHERE user_id IN (
    SELECT friend_id
    FROM friends
    WHERE user_id IN (
        SELECT user_id
        FROM users
        WHERE user_name IN ('Karl', 'Hans')
    )
    GROUP BY friend_id
    HAVING COUNT(*) > 1
);
-------------------------------------------------------------------
# Answer.2
WITH
    Karl_Friends AS (
        SELECT friend_id 
        FROM friends
        WHERE user_id = (SELECT user_id FROM users WHERE user_name = 'Karl')
    ),
    Hans_Friends AS (
        SELECT friend_id 
        FROM friends
        WHERE user_id = (SELECT user_id FROM users WHERE user_name = 'Hans')
    ),
    Mutual_Friends AS (
        SELECT friend_id 
        FROM Karl_Friends
        INTERSECT
        SELECT friend_id 
        FROM Hans_Friends
    )
SELECT 
    u.user_id, 
    u.user_name
FROM 
    users u
WHERE 
    u.user_id IN (SELECT friend_id FROM Mutual_Friends);
-------------------------------------------------------------------
# Wrong Answer
( retrieve id that may appear for karl or hans )
select user_id , user_name 
from users
where user_id in(
select user_id
from friends
where friend_id in (select user_id
from users
where user_name in ('Karl','Hans')))
