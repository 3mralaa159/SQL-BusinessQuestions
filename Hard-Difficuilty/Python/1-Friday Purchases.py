# Question
IBM is working on a new feature to analyze user purchasing behavior for all Fridays in the first quarter of the year. For each Friday separately,
  calculate the average amount users have spent per order. The output should contain the week number of that Friday and average amount spent.

# Link
https://platform.stratascratch.com/coding/10358-friday-purchases?code_type=1

# Answer
df['quarter'] = df['date'].dt.quarter
df['week_number'] = df['date'].dt.isocalendar().week
df['is_friday'] = df['date'].dt.dayofweek == 4  # Friday is day 4
df_friday_q1 = df[(df['quarter'] == 1) & (df['is_friday'])]
df_friday_q1.groupby('week_number')['amount_spent'].mean().reset_index()
