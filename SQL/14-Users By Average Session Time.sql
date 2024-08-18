# Question
  Calculate each user average session time. A session is defined as the time difference between a page_load and page_exit.
  For simplicity, assume a user has only 1 session per day and if there are multiple of the same events on that day, consider only the latest page_load and earliest page_exit,
  with an obvious restriction that load time event should happen before exit time event . Output the user_id and their average session time.

# link
  https://platform.stratascratch.com/coding/10352-users-by-avg-session-time?code_type=1

# Answer.1
select a.user_id , avg(mx - m)
from(
select  user_id  ,timestamp::date ,min(timestamp :: time) m
from facebook_web_log
where action = 'page_load'
group by 1 ,2)a
inner join
(
select user_id ,timestamp::date, max(timestamp :: time) mx
from facebook_web_log
where action = 'page_exit'
group by 1,2) b
on a.user_id = b.user_id
and a.timestamp = b.timestamp
  and b.mx > a.m
group by 1 

# Answer.2
WITH SessionTimes AS (
    -- Get the latest page_load and earliest page_exit for each user per day
    SELECT 
        user_id,
        date(timestamp) AS session_date,
        MAX(CASE WHEN action = 'page_load' THEN timestamp END) AS load_time,
        MIN(CASE WHEN action = 'page_exit' THEN timestamp END) AS exit_time
    FROM 
        facebook_web_log
    WHERE 
        action IN ('page_load', 'page_exit')
    GROUP BY 
        user_id, session_date
)
-- Filter out invalid sessions where page_load happens after page_exit
SELECT 
    user_id,
    AVG(load_time- exit_time) AS avg_session_time_seconds
FROM 
    SessionTimes
WHERE 
    load_time < exit_time
GROUP BY 
    user_id;

# Answer.3
WITH ordered_actions AS (
    SELECT 
        user_id, 
        timestamp, 
        action,
        ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY timestamp) as seq_num
    FROM 
        facebook_web_log
    WHERE 
        action IN ('page_load', 'page_exit')
),
matched_sessions AS (
    SELECT
        a.user_id,
        a.timestamp AS load_time,
        b.timestamp AS exit_time,
        b.timestamp - a.timestamp AS session_duration
    FROM 
        ordered_actions a
    JOIN 
        ordered_actions b 
    ON 
        a.user_id = b.user_id 
        AND a.seq_num = b.seq_num - 1
    WHERE 
        a.action = 'page_load' 
        AND b.action = 'page_exit'
        AND a.timestamp < b.timestamp  -- Ensure load_time is before exit_time
)
SELECT 
    user_id, 
    AVG(session_duration) AS avg_session_duration
FROM 
    matched_sessions
GROUP BY 
    user_id;
