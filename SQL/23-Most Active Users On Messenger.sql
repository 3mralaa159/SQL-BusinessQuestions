# Question
  Meta/Facebook Messenger stores the number of messages between users in a table named 'fb_messages'.
In this table 'user1' is the sender, 'user2' is the receiver, and 'msg_count' is the number of messages exchanged between them.
Find the top 10 most active users on Meta/Facebook Messenger by counting their total number of messages sent and received. 
Your solution should output usernames and the count of the total messages they sent or received

# Link
  https://platform.stratascratch.com/coding/10295-most-active-users-on-messenger?code_type=1

# Answer
SELECT
    user_name,
    SUM(total_messages) AS total_msg_count
FROM (
    -- Count messages sent by user1
    SELECT user1 AS user_name, SUM(msg_count) AS total_messages
    FROM fb_messages
    GROUP BY user1

    UNION ALL

    -- Count messages received by user2
    SELECT user2 AS user_name, SUM(msg_count) AS total_messages
    FROM fb_messages
    GROUP BY user2
) AS combined
GROUP BY user_name
ORDER BY total_msg_count DESC
LIMIT 10;
