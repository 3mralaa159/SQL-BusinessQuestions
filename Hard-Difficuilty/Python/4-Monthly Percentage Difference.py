# Question
  Given a table of purchases by date, calculate the month-over-month percentage change in revenue.
  The output should include the year-month date (YYYY-MM) and percentage change, rounded to the 2nd decimal point, and sorted from the beginning of the year to the end of the year.
The percentage change column will be populated from the 2nd month forward and can be calculated as ((this month''s revenue - last month''s revenue) / last month''s revenue)*100.

# Link
  https://platform.stratascratch.com/coding/10319-monthly-percentage-difference?code_type=1

# Answer
df['created_at'] = df['created_at'].dt.strftime('%Y-%m')
df = df.groupby('created_at')['value'].sum().reset_index()

df['lag'] = df['value'].shift(1)
df['pct'] = np.round(((df['value']/df['lag'])-1)*100,2)
df.rename(columns = {'created_at':'Date'}) 
df[['created_at','pct']]

# Answer.2
def op(c,p):
    return ((c-p)/p)*100
    
df['created_at'] = df['created_at'].dt.strftime('%Y-%m')
df = df.groupby('created_at')['value'].sum().reset_index()
df['lag'] = df['value'].shift(1)
df 
df['pct'] = df.apply(lambda x : op(x['value'],x['lag']),axis =1) 
