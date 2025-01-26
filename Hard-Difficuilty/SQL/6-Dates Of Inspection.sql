-- Question
  Find the latest inspection date for the most sanitary restaurant(s).
Assume the most sanitary restaurant is the one with the highest number of points received in any inspection (not just the last one). 
Only businesses with 'restaurant' in the name should be considered in your analysis.
Output the corresponding facility name, inspection score, latest inspection date, previous inspection date,
and the difference between the latest and previous inspection dates. And order the records based on the latest inspection date in ascending order.

-- Link  
  https://platform.stratascratch.com/coding/9714-dates-of-inspection?code_type=1

-- Answer.1
select facility_name, score , activity_date , previous_date , extract( month from age( activity_date,previous_date)) 
from (
select facility_name, score , activity_date , pe_description , dense_rank() over(partition by facility_name order by score desc ) r ,
 lag(activity_date) over(partition by facility_name order by activity_date asc) previous_date
from los_angeles_restaurant_health_inspections 
where pe_description like '%RESTAURANT%'
order by 1 ) a 
where r = 1 
order by activity_date 

-- Answer.2
WITH restaurant_inspections AS (
    SELECT
        facility_name,
        score,
        activity_date,
        RANK() OVER (PARTITION BY facility_id ORDER BY activity_date DESC) AS rank_date
    FROM your_table_name
    WHERE facility_name ILIKE '%restaurant%'
),
most_sanitary_restaurant AS (
    SELECT
        facility_name,
        MAX(score) AS max_score
    FROM restaurant_inspections
    GROUP BY facility_name
),
latest_previous_inspections AS (
    SELECT
        ri.facility_name,
        ri.score,
        ri.activity_date AS latest_inspection_date,
        LAG(ri.activity_date) OVER (PARTITION BY ri.facility_name ORDER BY ri.activity_date asc) AS previous_inspection_date
    FROM restaurant_inspections ri
    INNER JOIN most_sanitary_restaurant msr
    ON ri.facility_name = msr.facility_name AND ri.score = msr.max_score
)
SELECT
    facility_name,
    score AS inspection_score,
    latest_inspection_date,
    previous_inspection_date,
    COALESCE(latest_inspection_date - previous_inspection_date, INTERVAL '0 days') AS difference_between_inspections
FROM latest_previous_inspections
ORDER BY latest_inspection_date ASC;
