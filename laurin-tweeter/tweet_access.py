import json
import tweepy
from tweepy import OAuthHandler

CONSUMER_KEY = 'Ll01SzXcptfheD9hTiwZVv0go'
CONSUMER_SECRET = 'y6lN2sfhMxYeELEoIU1CTfLlOvlAKFHUuy7ro9z0swmYanl1cK'
OAUTH_TOKEN = '826864721563439104-ShcuZHoWOy352xa2UbZA1yszQk2CYQt'
OAUTH_TOKEN_SECRET = '8pgxNum1pOvUF0g25WLG49SzlfqBqT78kCgxzdrHRwaY5'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)

count = 10
query = 'Dublin'

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

# get status
results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]
print json.dumps(results[0]._json, indent=4)

for status in results:
    print status.text.encode('utf-8')
    print status.user.id
    print status.user.screen_name
    print status.user.profile_image_url_https
    print status.user.followers_count
    print status.place

def get_lexical_diversity(items):
    return 1.0*len(set(items))/len(items)

def get_average_words(tweets):
    total_words = sum([len(tweet.split()) for tweet in tweets ])
    return 1.0*total_words/len(tweets)

print "Average words: %s" % get_average_words(status_texts)
print "Word Diversity: %s" % get_lexical_diversity(words)
print "Screen Name Diversity: %s" % get_lexical_diversity(screen_names)
print "Hashtag Diversity: %s" % get_lexical_diversity(hashtags)