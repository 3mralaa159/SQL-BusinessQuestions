# Question
  Find all the songs that were top-ranked (at first position) at least once in the past 20 years

# Link 
  https://platform.stratascratch.com/coding/10283-find-the-top-ranked-songs-for-the-past-30-years?code_type=2

# Answer
a = df['year'].max()-20

df[(df['year'] >= a) & (df['year_rank'] == 1)]
