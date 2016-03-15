# Code by Artur Pimentel de Oliveira
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

from tweepy.utils import import_simplejson
json = import_simplejson()

# Please assign your keys strings to the variables below
# Consumer keys
consumer_key = ""
consumer_secret = ""

# Access keys
access_token=""
access_token_secret=""

lon = 0
lat = 1

longitude_left_point = -86.33
latitude_left_point = 41.63
longitude_right_point = -86.20
latitude_right_point = 41.74

class StdOutListener(StreamListener):
	n_good_tweets = 0

	def on_data(self, raw_data):

		data = json.loads(raw_data)
		
		if data.has_key("text"):
			text = data["text"]
			if text is None:
				return True
			else:
				if self.n_good_tweets < 50:
					print str(self.n_good_tweets) + ". " + text.encode("utf-8")
					self.n_good_tweets += 1
					return True
				else:
					return False
		else:
			return True
		

	def on_error(self, status):
		print status

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['Indiana', 'weather'])
