# Question
  You are given a table of product launches by company by year.
  Write a query to count the net difference between the number of products companies launched in 2020 with the number of products companies launched in the previous year.
  Output the name of the companies and a net difference of net products released for 2020 compared to the previous year.

# Link
  https://platform.stratascratch.com/coding/10318-new-products?code_type=1

# Answer
select company_name , C_2020 - C_2019 AS Diff
from(
select company_name, year , count(product_name) C_2020 ,
coalesce(lag(count(product_name)) over (partition by company_name order by year),0) C_2019
from car_launches
group by 1 , 2 
order by 1 , 2 asc)a 
where C_2019 <> 0

