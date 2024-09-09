# Question
  Find the total number of available beds per hosts nationality.
Output the nationality along with the corresponding total number of available beds.
Sort records by the total available beds in descending order.

# Link
https://platform.stratascratch.com/coding/10187-find-the-total-number-of-available-beds-per-hosts-nationality?code_type=1

# Answer 
select country , host_id , count(n_beds)
from airbnb_apartments
group by country , host_id 
order by 1 
