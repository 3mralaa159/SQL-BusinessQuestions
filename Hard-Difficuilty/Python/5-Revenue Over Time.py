# Question
  Find the 3-month rolling average of total revenue from purchases given a table with users, their purchase amount, and date purchased.
  Do not include returns which are represented by negative purchase values. Output the year-month (YYYY-MM) and 3-month rolling average of revenue,
  sorted from earliest month to latest month. 
  3-month rolling average is defined by calculating the average total revenue from all user purchases for the current month and previous two months.
  The first two months will not be a true 3-month rolling average since we are not given data from last year. Assume each month has at least one purchase.

# Link
  https://platform.stratascratch.com/coding/10314-revenue-over-time?code_type=1

# Answer
# Import your libraries
import pandas as pd

# Start writing code
df = amazon_purchases.copy()
df = df[df['purchase_amt'] > 0 ]

df['created_at'] = df['created_at'].dt.strftime('%Y-%m')
df = df.groupby('created_at')['purchase_amt'].sum().reset_index()
df['rolling_avg'] = df['purchase_amt'].rolling(window=3, min_periods=1).mean()
df[['created_at','rolling_avg']] 
