import bot.py, markovify

class generate:

    # getSamples(user) returns a very long string created by concatenating
    #   previous tweets from user. This will be used to generate a tweet
    def getSamples(user):
        sample = ''

        for tweet in bot.api.user_timeline(id=user, count=bot.TWEETS):
            sample += tweet.text + ' '

        return sample

    # generateText(sample) returns a string generated using a Markov chain
    def generateText(sample):
        return markovify.Text(sample).make_sentence(tries=25)

