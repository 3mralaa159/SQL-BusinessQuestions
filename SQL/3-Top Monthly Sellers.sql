# Question
  You are provided with a transactional dataset from Amazon that contains detailed information about sales across different products and marketplaces.
  Your task is to list the top 3 sellers in each product category for January.

# Link
  https://platform.stratascratch.com/coding/10362-top-monthly-sellers?code_type=1

# Answer
select *
from(
select product_category , seller_id , sum(total_sales) ,  dense_rank() over(partition by product_category order by sum(total_sales) desc) as r
from sales_data
where month = '2024-01'
group by 1 , 2
order by 1 ) a
where r <= 3

