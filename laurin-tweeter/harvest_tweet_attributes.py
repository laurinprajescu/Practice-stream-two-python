import json
import tweepy
from tweepy import OAuthHandler
from collections import Counter

CONSUMER_KEY = 'Ll01SzXcptfheD9hTiwZVv0go'
CONSUMER_SECRET = 'y6lN2sfhMxYeELEoIU1CTfLlOvlAKFHUuy7ro9z0swmYanl1cK'
OAUTH_TOKEN = '826864721563439104-ShcuZHoWOy352xa2UbZA1yszQk2CYQt'
OAUTH_TOKEN_SECRET = '8pgxNum1pOvUF0g25WLG49SzlfqBqT78kCgxzdrHRwaY5'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

api = tweepy.API(auth)

count = 50
query = 'Weather'

# get all tweets for the search query
results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]

status_texts = [ status._json['text'] for status in results ]

screen_names = [ status._json['user']['screen_name']
                                for status in results
                                        for mention in status._json['entities']['user_mentions'] ]

hashtags = [ hashtag['text']
                                for status in results
                                        for hashtag in status._json['entities']['hashtags'] ]

words = [ word
                        for text in status_texts
                                for word in text.split()]

for entry in [ screen_names, hashtags, words]:
    counter = Counter(entry)
    print counter.most_common()[:10] #top 10 results
    print