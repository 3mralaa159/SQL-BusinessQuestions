# Question
  For each week, find the total number of orders. Include only the orders that are from the first quarter of 2023
# link
  https://platform.stratascratch.com/coding/10363-weekly-orders-report?code_type=1
# Answer
select week , sum(quantity)
from orders_analysis
where date_part('quarter',week) = 1 
group by 1 
order by 1 


