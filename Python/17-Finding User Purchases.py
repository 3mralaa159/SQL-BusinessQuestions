# Question
  Write a query that will identify returning active users. A returning active user is a user that has made a second purchase within 7 days of any other of their purchases.
Output a list of user_ids of these returning active users.

# Link
  https://platform.stratascratch.com/coding/10322-finding-user-purchases?code_type=1

# Answer
# Import your libraries
import pandas as pd
from datetime import timedelta

# Start writing code
amazon_transactions.head()
df = amazon_transactions.copy()
df1 = pd.merge(df,df,on='user_id',suffixes=['_first','_sec'])[['id_first','user_id','created_at_first','id_sec','created_at_sec']]
df1['third'] = df1['created_at_first'] + timedelta(days =7)
df1
result = df1.query(
    'id_first != id_sec & '
    'created_at_first <= created_at_sec & '
    'created_at_sec <= third'
).sort_values('user_id', ascending=True)

# Answer.2
# equal to row_number in sql
def find_purchases_within_7_days(group):
    result = []
    for i in range(len(group)):
        for j in range(i + 1, len(group)):
            first_purchase = group.iloc[i]
            second_purchase = group.iloc[j]
            if (second_purchase['created_at'] <= first_purchase['created_at'] + timedelta(days=7)):
                result.append({
                    'user_id': first_purchase['user_id'],
                    'created_at_first': first_purchase['created_at'],
                    'created_at_second': second_purchase['created_at']
                })
    return pd.DataFrame(result)

# Group by user and apply the function
result = df.groupby('user_id').apply(find_purchases_within_7_days).reset_index(drop=True)

# Sort the results for better readability
result = result.sort_values(by=['user_id', 'created_at_first'])
