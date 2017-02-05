import tweepy
from tweepy import OAuthHandler

CONSUMER_KEY = 'Ll01SzXcptfheD9hTiwZVv0go'
CONSUMER_SECRET = 'y6lN2sfhMxYeELEoIU1CTfLlOvlAKFHUuy7ro9z0swmYanl1cK'
OAUTH_TOKEN = '826864721563439104-ShcuZHoWOy352xa2UbZA1yszQk2CYQt'
OAUTH_TOKEN_SECRET = '8pgxNum1pOvUF0g25WLG49SzlfqBqT78kCgxzdrHRwaY5'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)

for status in tweepy.Cursor(api.home_timeline).items(10):
    #process a tweet
    print status.text