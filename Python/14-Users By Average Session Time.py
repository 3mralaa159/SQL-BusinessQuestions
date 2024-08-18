# Question
  Calculate each user average session time. A session is defined as the time difference between a page_load and page_exit.
  For simplicity, assume a user has only 1 session per day and if there are multiple of the same events on that day, consider only the latest page_load and earliest page_exit,
  with an obvious restriction that load time event should happen before exit time event . Output the user_id and their average session time.

# link
  https://platform.stratascratch.com/coding/10352-users-by-avg-session-time?code_type=1

# Answer
import pandas as pd

# Display the first few rows of the original DataFrame
facebook_web_log.head()

# Create a copy of the DataFrame to avoid modifying the original data
df = facebook_web_log.copy()

# Extract the date and time components from the timestamp and create new columns
df['date'] = df['timestamp'].dt.date
df['time'] = df['timestamp'].dt.time

# Drop the original 'timestamp' column as it's no longer needed
df.drop('timestamp', axis=1, inplace=True)

# Filter the DataFrame to include only the actions 'page_load' and 'page_exit'
df = df[df['action'].isin(['page_load', 'page_exit'])]

# Separate the DataFrame into two based on action type
df_load = df[df['action'].isin(['page_load'])]
df_exit = df[df['action'].isin(['page_exit'])]

# For 'page_load', get the earliest time for each user on each date
lo = df_load.groupby(['user_id', 'date'])['time'].min().reset_index()

# For 'page_exit', get the latest time for each user on each date
ex = df_exit.groupby(['user_id', 'date'])['time'].max().reset_index()

# Merge the two DataFrames on 'user_id' and 'date' to combine load and exit times
one = pd.merge(ex, lo, on=['user_id', 'date'])

# Define a function to compute the difference in seconds between two times
def time_diff_in_seconds(time1, time2):
    # Convert times to datetime objects with a dummy date
    t1 = pd.to_datetime(time1.strftime('%H:%M:%S'), format='%H:%M:%S')
    t2 = pd.to_datetime(time2.strftime('%H:%M:%S'), format='%H:%M:%S')
    # Calculate the difference in seconds
    return (t2 - t1).total_seconds()

# Apply the function to compute the time difference for each row
one['time_difference_seconds'] = one.apply(lambda row: time_diff_in_seconds(row['time_x'], row['time_y']), axis=1)

# Group by 'user_id' and calculate the average time difference in seconds
average_time_diff = one.groupby('user_id')['time_difference_seconds'].mean().reset_index()

print(average_time_diff)

# Answer.2
import pandas as pd
import numpy as np

# Filter rows for 'page_load' and 'page_exit' actions
load_df = facebook_web_log[facebook_web_log['action'] == 'page_load'][['user_id', 'timestamp']]
exit_df = facebook_web_log[facebook_web_log['action'] == 'page_exit'][['user_id', 'timestamp']]

# Merge on user_id, considering only pairs where page_load timestamp is less than page_exit timestamp
df = pd.merge(load_df, exit_df, on='user_id', suffixes=['_load', '_exit'])
df = df[df['timestamp_load'] < df['timestamp_exit']]

# Convert timestamps to dates for grouping by user and date without casting
df['date'] = df['timestamp_load'].dt.floor('d')

# Group by user_id and date, then get the max page_load and min page_exit for each group
df = df.groupby(['user_id', 'date']).agg(timestamp_load=('timestamp_load', 'max'),
                                         timestamp_exit=('timestamp_exit', 'min')).reset_index()

# Calculate duration as the difference between max page_load and min page_exit
df['duration'] = (df['timestamp_exit'] - df['timestamp_load']).dt.total_seconds()  # duration in seconds

# Group by user_id and calculate the average session duration in seconds
result = df.groupby('user_id')['duration'].mean().reset_index()

