# Question
  Given a table of purchases by date, calculate the month-over-month percentage change in revenue.
  The output should include the year-month date (YYYY-MM) and percentage change, rounded to the 2nd decimal point, and sorted from the beginning of the year to the end of the year.
The percentage change column will be populated from the 2nd month forward and can be calculated as ((this month''s revenue - last month''s revenue) / last month''s revenue)*100.

# Link
  https://platform.stratascratch.com/coding/10319-monthly-percentage-difference?code_type=1

# Answer
select date , round(((sales/lag)-1)*100,2) diff_pct
from (
select to_char(created_at,'YYYY-MM') as date , sum(value) sales , lag(sum(value)) over(order by to_char(created_at,'YYYY-MM'))
from sf_transactions
group by date 
order by date) a
