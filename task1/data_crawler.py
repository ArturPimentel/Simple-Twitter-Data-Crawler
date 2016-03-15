# Code by Artur Pimentel de Oliveira
import tweepy

# Please assign your keys strings to the variables below
# Consumer keys
consumer_key = ""
consumer_secret = ""

# Access keys
access_token=""
access_token_secret=""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
user_list = ['34373370', '26257166', '12579252']

with open("result.txt", "w") as result_file:
	for user_id in user_list:
		user = api.get_user(user_id)
		result_file.write('Screen Name: ' + user.screen_name + '\n')
		result_file.write('User Name: ' + user.name + '\n')
		result_file.write('User Location: ' + user.location + '\n')
		result_file.write('User Description: ' + user.description + '\n')
		result_file.write('The Number of Followers: ' + str(user.followers_count) + '\n')
		result_file.write('The number of Friends: ' + str(user.friends_count) + '\n')
		result_file.write('The Number of Statuses: ' + str(user.statuses_count) + '\n')
		result_file.write('User URL: ' + str(user.url) + '\n\n')