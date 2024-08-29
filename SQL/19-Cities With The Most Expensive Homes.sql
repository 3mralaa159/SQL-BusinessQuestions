# Question
  Write a query that identifies cities with higher than average home prices when compared to the national average. Output the city names.

# Link  
  https://platform.stratascratch.com/coding/10315-cities-with-the-most-expensive-homes?code_type=1

# Answer
select state , city , avg(mkt_price)
from zillow_transactions
group by 1 , 2 
having avg(mkt_price) > (
select avg(mkt_price) 
from zillow_transactions )
