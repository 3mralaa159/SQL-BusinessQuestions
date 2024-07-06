# Question
    As a data scientist at Amazon Prime Video, you are tasked with enhancing the in-flight entertainment experience 
    for Amazon’s airline partners. Your challenge is to develop a feature that suggests individual movies from Amazon's content database that fit within a given flight's duration.
    For flight 101, find movies whose runtime is less than or equal to the flight's duration.
    The output should list suggested movies for the flight, including 'flight_id', 'movie_id', and 'movie_duration'.'
# Link
  https://platform.stratascratch.com/coding/10360-movie-duration-match?code_type=1
# Answer
select b.flight_id , a.movie_id , a.duration
from entertainment_catalog a
join flight_schedule b
on a.duration <= b.flight_duration
where b.flight_id = '101'
