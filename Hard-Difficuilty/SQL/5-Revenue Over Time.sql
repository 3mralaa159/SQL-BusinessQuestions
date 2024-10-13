# Question
  Find the 3-month rolling average of total revenue from purchases given a table with users, their purchase amount, and date purchased.
  Do not include returns which are represented by negative purchase values. Output the year-month (YYYY-MM) and 3-month rolling average of revenue,
  sorted from earliest month to latest month. 
  3-month rolling average is defined by calculating the average total revenue from all user purchases for the current month and previous two months.
  The first two months will not be a true 3-month rolling average since we are not given data from last year. Assume each month has at least one purchase.

# Link
  https://platform.stratascratch.com/coding/10314-revenue-over-time?code_type=1

# Answer
select date , avg(sales) over(order by date rows between 2 preceding and current row ) rolling_avg
from(
select to_char(created_at,'YYYY-MM') date  , sum(purchase_amt) sales
from amazon_purchases
where purchase_amt > 0 
group by date 
order by 1 
) a 
