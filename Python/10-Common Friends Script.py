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
-------------------------------------------------------------------
# Answer.2
>> Query
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
-------------------------------------------------------------------
# Answer.3
>> Merge
# Get user IDs
karl_id = users[users['user_name'] == 'Karl']['user_id'].iloc[0]
hans_id = users[users['user_name'] == 'Hans']['user_id'].iloc[0]

# Karl's friends
karl_friends = friends[friends['user_id'] == karl_id]
# Hans' friends
hans_friends = friends[friends['user_id'] == hans_id]

# Merge to find mutual friends
mutual_friends = pd.merge(karl_friends, hans_friends, on='friend_id')['friend_id']
users[users['user_id'].isin(mutual_friends)]
-------------------------------------------------------------------
# Answer.4
>> intersection + groupby using set method
karl_id = users[users['user_name'] == 'Karl']['user_id'].iloc[0]
hans_id = users[users['user_name'] == 'Hans']['user_id'].iloc[0]

friends_grouped = friends.groupby('user_id')['friend_id'].apply(set)
mutual_friends = friends_grouped[karl_id].intersection(friends_grouped[hans_id])

users[users['user_id'].isin(mutual_friends)]
-------------------------------------------------------------------
# Answer.5
>> intersection + set method 
karl_id = users[users['user_name'] == 'Karl']['user_id'].iloc[0]
hans_id = users[users['user_name'] == 'Hans']['user_id'].iloc[0]

karl_friends_set = set(friends[friends['user_id'] == karl_id]['friend_id'])
hans_friends_set = set(friends[friends['user_id'] == hans_id]['friend_id'])

mutual_friends = karl_friends_set.intersection(hans_friends_set)
users[users['user_id'].isin(mutual_friends)]
-------------------------------------------------------------------
# Answer.6
>> Self join
karl_id = users[users['user_name'] == 'Karl']['user_id'].iloc[0]
hans_id = users[users['user_name'] == 'Hans']['user_id'].iloc[0]

friends_self_join = pd.merge(friends, friends, on='friend_id')
mutual_friends = friends_self_join[(friends_self_join['user_id_x'] == karl_id) & 
                                   (friends_self_join['user_id_y'] == hans_id)]['friend_id']

users[users['user_id'].isin(mutual_friends)]
