# Code by Artur Pimentel de Oliveira
import tweepy

# Please assign your keys strings to the variables below
# Consumer keys
consumer_key = ""
consumer_secret = ""

# Access keys
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
user_list = ['34373370', '26257166', '12579252']

with open("result.txt", "w") as result_file:
	for user_id in user_list:
		user = api.get_user(user_id)
		followers = api.followers(user_id)
		friends_ids = api.friends_ids(user_id, -1)

		result_file.write('User Name: ' + user.name + '\n\n')

		result_file.write('The Friends list:\n\n')
		for i in range(0, 20):
			friend = api.get_user(str(friends_ids[i]))
			result_file.write(friend.screen_name + '\n')
		result_file.write('\n')

		result_file.write('The Followers list:\n\n')
		for i in range(0, 20):
			result_file.write(followers[i].screen_name + '\n')
		result_file.write('\n')