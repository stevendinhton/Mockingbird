import configparser
import tweepy

config = configparser.ConfigParser()
config.read('config.ini')

# get keys and secrets from config.ini file
CONSUMER_KEY = config['TWITTER']['CONSUMER_KEY']
CONSUMER_SECRET = config['TWITTER']['CONSUMER_SECRET']
ACCESS_KEY = config['TWITTER']['ACCESS_KEY']
ACCESS_SECRET = config['TWITTER']['ACCESS_SECRET']

# connect to Twitter API
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


