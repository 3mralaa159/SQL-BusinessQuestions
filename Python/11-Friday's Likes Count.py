# Question
  You have access to Facebook database which includes several tables relevant to user interactions. 
For this task, you are particularly interested in tables that store data about user posts, friendships, and likes. 
Calculate the total number of likes made on friend posts on Friday.
The output should contain two different columns 'likes' and 'date'.

# Link
  https://platform.stratascratch.com/coding/10364-fridays-likes-count?code_type=2

# Answer
# Import your libraries
import pandas as pd

# Start writing code
likes.head()

friday = likes[likes['date_liked'].dt.day_name() == 'Friday']
friday.head()
likes_posts = pd.merge(friday,user_posts,on='post_id')
likes_friends1 = pd.merge(likes_posts, friendships, left_on=['user_name_y', 'user_name_x'], right_on=['user_name1', 'user_name2'], how='inner')
likes_friends2 = pd.merge(likes_posts, friendships, left_on=['user_name_y', 'user_name_x'], right_on=['user_name2', 'user_name1'], how='inner')
likes_friends = pd.concat([likes_friends1, likes_friends2])
likes_count = likes_friends.groupby(likes_friends['date_liked'].dt.date).size().reset_index(name='likes')
