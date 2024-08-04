# Question
  You are working on a data analysis project at Deloitte where you need to analyze a dataset containing information
about various cities. Your task is to calculate the population density of these cities, rounded to the nearest integer, and identify the cities with the minimum and maximum densities.
The population density should be calculated as (Population / Area).
The output should contain 'city', 'country', 'density'.

# Link
  https://platform.stratascratch.com/coding/10368-population-density?code_type=1

# Answer
WITH one AS (
select * , round(population/area) as density
from cities_population
where area <> 0) , two AS(
select max(density) x
from one) , three AS (select min(density) m from one )
select a.city , a.country , b.x as density 
from one a 
join two b on a.density = b.x
union
select a.city ,  a.country , c.m as density 
from one a 
join three c on a.density = c.m
order by 3 desc 


