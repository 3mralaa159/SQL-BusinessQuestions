# Question
  Find the top 10 users that have traveled the greatest distance. Output their id, name and a total distance traveled.

# Link
  https://platform.stratascratch.com/coding/10324-distances-traveled?code_type=1

# Answer
lyft_rides_log.head()
df = lyft_rides_log.copy()
df1 = lyft_users.copy()
df1 = df1.rename(columns={'id':'user_id'})

df = df.groupby('user_id')['distance'].sum().reset_index()
df2 = pd.merge(df,df1,on='user_id')
df3 = df2.nlargest(10,'distance').sort_values('distance',ascending=False)
df3.iloc[:,[0,2,1]]

# Answer.2
lyft_users= lyft_users.rename(columns={'id':'user_id'})
# 1. Merge DataFrames
merged_data = pd.merge(lyft_rides_log, lyft_users, on='user_id')
# 2. Use pivot_table to aggregate
pivot_table = merged_data.pivot_table(values='distance', index=['user_id', 'name'], aggfunc='sum').reset_index()
# 3. Sort and get top 10 users
top_10_users = pivot_table.sort_values(by='distance', ascending=False).head(10)
# Rename column for clarity
top_10_users = top_10_users.rename(columns={'distance': 'total_distance'})

# Display the result
print(top_10_users[['user_id', 'name', 'total_distance']])
