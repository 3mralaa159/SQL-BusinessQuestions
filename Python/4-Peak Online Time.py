# Question
  You are given a dataset from Amazon that tracks and aggregates user activity on their platform in certain time periods.
  For each device type, find the time period with the highest number of active users.
  The output should contain 'user_count', 'time_period', and 'device_type',
  where 'time_period' is a concatenation of 'start_timestamp' and 'end_timestamp', like ; "start_timestamp to end_timestamp".
# Link
  https://platform.stratascratch.com/coding/10361-peak-online-time?code_type=2

# Answer
df.groupby('device_type').apply(lambda x : x.nlargest(1,'user_count'))

# Answer.2
# Import your libraries
import pandas as pd
# Load dataset 
df = pd.DataFrame(user_activity)
# Convert timestamps to datetime format
df['start_timestamp'] = pd.to_datetime(df['start_timestamp'])
df['end_timestamp'] = pd.to_datetime(df['end_timestamp'])

# Concatenate start_timestamp and end_timestamp into time_period
df['time_period'] = df['start_timestamp'].dt.strftime('%Y-%m-%d %H:%M:%S') + ' to ' + df['end_timestamp'].dt.strftime('%Y-%m-%d %H:%M:%S')

# Group by device_type and find the row with the maximum user_count
max_users_idx = df.groupby('device_type')['user_count'].idxmax()
result = df.loc[max_users_idx, ['user_count', 'time_period', 'device_type']].reset_index(drop=True)

# Display the result
print(result)
