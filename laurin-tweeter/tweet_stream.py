from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

CONSUMER_KEY = 'Ll01SzXcptfheD9hTiwZVv0go'
CONSUMER_SECRET = 'y6lN2sfhMxYeELEoIU1CTfLlOvlAKFHUuy7ro9z0swmYanl1cK'
OAUTH_TOKEN = '826864721563439104-ShcuZHoWOy352xa2UbZA1yszQk2CYQt'
OAUTH_TOKEN_SECRET = '8pgxNum1pOvUF0g25WLG49SzlfqBqT78kCgxzdrHRwaY5'

keyword_list = ['python', 'java', 'c#', 'ruby'] #track list

class MyStreamListener(StreamListener):
    def on_data(self, data):
        try:
            with open('tweet_mining.json', 'a') as tweet_file:
                tweet_file.write(data)
                return True
        except BaseException as e:
            print "Failed on_data: %s" % str(e)
        return True
    def on_error(self, status):
        print status
        return True

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

tweeter_stream = Stream(auth, MyStreamListener())
tweeter_stream.filter(track=keyword_list)
