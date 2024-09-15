# Question
IBM is working on a new feature to analyze user purchasing behavior for all Fridays in the first quarter of the year. For each Friday separately,
  calculate the average amount users have spent per order. The output should contain the week number of that Friday and average amount spent.

# Link
https://platform.stratascratch.com/coding/10358-friday-purchases?code_type=1

# Answer
SELECT 
    EXTRACT(WEEK FROM date) AS week_number, 
    AVG(amount_spent) AS avg_amount_spent
FROM 
    your_table_name
WHERE 
    EXTRACT(QUARTER FROM date) = 1
    AND day_name = 'Friday'
GROUP BY 
    week_number
ORDER BY 
    week_number;
