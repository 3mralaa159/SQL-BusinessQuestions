# Question
    You are given a dataset from Amazon that tracks and aggregates user activity on their platform in certain time periods.
    For each device type, find the time period with the highest number of active users.
    The output should contain 'user_count', 'time_period', and 'device_type', 
    where 'time_period' is a concatenation of 'start_timestamp' and 'end_timestamp', like ; "start_timestamp to end_timestamp".
# Link
    https://platform.stratascratch.com/coding/10361-peak-online-time?code_type=1
# Answer
select * 
from(
select device_type , user_count , concat(start_timestamp ,' ', 'to' ,' ', end_timestamp) time_period , dense_rank() over(partition by device_type order by user_count desc) r 
from user_activity ) a
where r = 1

# Answer.2
WITH ranked_periods AS (
    SELECT
        device_type,
        start_timestamp,
        end_timestamp,
        CONCAT(start_timestamp, ' to ', end_timestamp) AS time_period,
        user_count,
        RANK() OVER(PARTITION BY device_type ORDER BY user_count DESC) AS rank_num
    FROM
        user_activity
)
SELECT
    user_count,
    time_period,
    device_type
FROM
    ranked_periods
WHERE
    rank_num = 1;
