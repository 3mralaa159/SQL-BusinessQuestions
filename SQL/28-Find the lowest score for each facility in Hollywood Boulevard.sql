# Question
  Find the lowest score per each facility in Hollywood Boulevard.
Output the result along with the corresponding facility name.
Order the result based on the lowest score in descending order and the facility name in the ascending order.

# Link
  https://platform.stratascratch.com/coding/10180-find-the-lowest-score-for-each-facility-in-hollywood-boulevard?code_type=1

# Answer
select facility_id , facility_name , min(score)
from los_angeles_restaurant_health_inspections
group by 1 , 2 
order by 3 desc , 2 asc
