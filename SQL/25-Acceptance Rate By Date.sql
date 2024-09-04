# Question
  What is the overall friend acceptance rate by date?
  Your output should have the rate of acceptances by the date the request was sent. Order by the earliest date to latest.
Assume that each friend request starts by a user sending (i.e., user_id_sender) a friend request to another user (i.e., user_id_receiver)
that''s logged in the table with action = 'sent'. If the request is accepted, the table logs action = 'accepted'. If the request is not accepted, no record of action = 'accepted' is logged.

# Link
  https://platform.stratascratch.com/coding/10285-acceptance-rate-by-date?code_type=1

# Answer
WITH sent_requests AS (
    SELECT  
        DATE(date) AS request_date,
        COUNT(*) AS total_sent
    FROM 
        fb_friend_requests
    WHERE 
        action = 'sent'
    GROUP BY 
        date
),
accepted_requests AS (
    SELECT  
        date AS request_date,
        COUNT(*) AS total_accepted
    FROM 
        fb_friend_requests
    WHERE 
        action = 'accepted'
    GROUP BY 
        date
)
SELECT 
    s.request_date,
    COALESCE(a.total_accepted, 0) * 1.0 / s.total_sent AS acceptance_rate
FROM 
    sent_requests s
left JOIN 
    accepted_requests a
ON 
    s.request_date = a.request_date
ORDER BY 
    s.request_date;
