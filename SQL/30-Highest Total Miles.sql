# Question
  You’re given a table of Uber rides that contains the mileage and the purpose for the business expense.
  You’re asked to find business purposes that generate the most miles driven for passengers that use Uber for their business transportation. Find the top 3 business purpose categories by total mileage.

# link
  https://platform.stratascratch.com/coding/10169-highest-total-miles?code_type=1

# Answer
select purpose , sum(miles) 
from my_uber_drives
WHERE 
    purpose IS NOT NULL
group by 1 
order by 2 desc 
limit 3 
