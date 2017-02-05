import json
import tweepy
from tweepy import OAuthHandler
from collections import Counter
from prettytable import PrettyTable
from operator import itemgetter

CONSUMER_KEY = 'Ll01SzXcptfheD9hTiwZVv0go'
CONSUMER_SECRET = 'y6lN2sfhMxYeELEoIU1CTfLlOvlAKFHUuy7ro9z0swmYanl1cK'
OAUTH_TOKEN = '826864721563439104-ShcuZHoWOy352xa2UbZA1yszQk2CYQt'
OAUTH_TOKEN_SECRET = '8pgxNum1pOvUF0g25WLG49SzlfqBqT78kCgxzdrHRwaY5'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)

count = 150
query = 'Ireland'

# get all tweets for search query
results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]

min_retweets = 10

pop_tweets = [status
              for status in results
                    if status._json['retweet_count'] > min_retweets]

#create a dictionary of tweet text and associate re tweets
tweets_tup = tuple([(tweet._json['text'].encode('utf-8'), tweet._json['retweet_count']) for tweet in pop_tweets])

#remove duplicates
pop_tweets_set = sorted(tweets_tup)

#sort the tuples entries in descending order

sorted_tweets_tup = sorted(pop_tweets_set, key=itemgetter(1), reverse=True)[:5]

#prettify

table = PrettyTable(field_names=['Text', 'Retweet Count'])
for key, val in sorted_tweets_tup:
    table.add_row([key, val])
table.max_width['Text'] = 50
table.align['Text'], table.align['Retweet Count'] = 'l', 'r' #align columns
print table