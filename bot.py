import configparser, tweepy, markovify

config = configparser.ConfigParser()
config.read('config.ini')

# get keys and secrets from config.ini file
CONSUMER_KEY = config['TWITTER']['CONSUMER_KEY']
CONSUMER_SECRET = config['TWITTER']['CONSUMER_SECRET']
ACCESS_KEY = config['TWITTER']['ACCESS_KEY']
ACCESS_SECRET = config['TWITTER']['ACCESS_SECRET']
# get bot's twitter screen name (e.g. @mockingbirdbot)
BOT_NAME = config['TWITTER']['BOT_SCREEN_NAME']
# get number of tweets to analyze per user
TWEETS = config['GENERATION']['TWEETS']

# connect to Twitter API
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

class Generate:

    # getSamples(user) returns a very long string created by concatenating
    #   previous tweets from user. This will be used to generate a tweet
    def getSamples(user):
        sample = ''

        for tweet in api.user_timeline(id=user, count=TWEETS):
            sample += tweet.text + ' '

        return sample

    # generateText(sample) returns a string generated using a Markov chain
    def generateText(sample):
        return markovify.Text(sample).make_sentence(tries=300)


class Listener(tweepy.StreamListener):
    
    # findUser(tweet) returns the user id in which the bot will generate
    #   its tweet based on, or return False if not found
    def findUser(tweet):
        text = tweet.text.split()

        # if there are atleast two tokens in the received tweet and the second
        #   token is a mention:
        if len(text) > 0 and text[1][0] == '@':
            try:
                return api.lookup_users(screen_names=[text[1][1:]])[0].id
            except:
                print("Exception occurred trying to find user "+text[1][1:])
                return False
        else:   
            return tweet.user.id

    # genMention(tweet) returns a string of the mentions at the beginning of the
    #   tweet. This can be zero, one, or two users. Zero mentions only occur when
    #   the bot commands itself to tweet at itself (should only be possible by
    #   manually tweeting on twitter.com)
    def genMentions(tweet):
        mentions = [api.lookup_users(user_ids=[tweet.user.id])[0].screen_name,
                    api.lookup_users(user_ids=[Listener.findUser(tweet)])[0].screen_name]

        mentions = list(filter(lambda a: a != api.me().screen_name, mentions))
        mentions = list(set(mentions))

        if len(mentions) == 0:
            return ''
        if len(mentions) == 1:
            return '@' + mentions[0]
        else:
            return '@' + mentions[0] + ' @' + mentions[1]
        
    
    def on_status(self, status):
        userid = Listener.findUser(status)
        if userid != False:
            print(status.user.screen_name, 'Mentions: ', Listener.genMentions(status))
            try:
                genTweet = (Listener.genMentions(status) + ' ' +
                            Generate.generateText(Generate.getSamples(userid)))[:140]
                
                api.update_status(genTweet)
            except:
                print("Exception occurred trying to tweet")
        else:
            print(userid, "not found")


# set up listeners for tweets containing the bot's screen name
listener = Listener()
stream = tweepy.Stream(api.auth, listener)
stream.filter(track=[BOT_NAME])
