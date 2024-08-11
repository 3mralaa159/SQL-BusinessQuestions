# Question
  You are analyzing a social network dataset at Google. Your task is to find mutual friends between two users, Karl and Hans.
  There is only one user named Karl and one named Hans in the dataset.
  The output should contain 'user_id' and 'user_name' columns.

# Link
  https://platform.stratascratch.com/coding/10365-common-friends-script?code_type=1

# Answer
# Step 1: Find the user IDs of Karl and Hans
karl_id = users.loc[users['user_name'] == 'Karl', 'user_id'].iloc[0]
hans_id = users.loc[users['user_name'] == 'Hans', 'user_id'].iloc[0]

# Step 2: Find users who are friends with both Karl and Hans
# Approach 1: Using separate filters
friends_of_karl = friends.query('friend_id == @karl_id')['user_id']
friends_of_hans = friends.query('friend_id == @hans_id')['user_id']

mutual_friend_ids = friends_of_karl[friends_of_karl.isin(friends_of_hans)]

# Step 3: Get the details of mutual friends from the users DataFrame
mutual_friends_df = users[users['user_id'].isin(mutual_friend_ids)]
print(mutual_friends_df)

# Answer.2
# Step 1: Find the user IDs of Karl and Hans
karl_id = users.loc[users['user_name'] == 'Karl', 'user_id'].iloc[0]
hans_id = users.loc[users['user_name'] == 'Hans', 'user_id'].iloc[0]

# Step 2: Find users who are friends with both Karl and Hans
mutual_friend_ids = friends.query('friend_id == @karl_id or friend_id == @hans_id')\
                           .groupby('user_id')\
                           .filter(lambda x: len(x) > 1)['user_id'].unique()

# Step 3: Get the details of mutual friends from the users DataFrame
mutual_friends_df = users[users['user_id'].isin(mutual_friend_ids)]
print(mutual_friends_df)
