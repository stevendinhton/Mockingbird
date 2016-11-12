# Mockingbird
A Twitter Bot that generates tweets based on a Markov chain. Uses Tweepy and Markovify.
**This bot 'works' but is still a WORK IN PROGRESS.**

I still have to clean up the code, add a few more features, fix a few minor bugs

### How to Use

Tweet to use the bot on Twitter (replace `@username` with the actual username of the user you want the bot to replicate):
>@mockingbirdbot @username

### Installation
You're going to need [Tweepy](https://github.com/tweepy/tweepy) and [Markovify](https://github.com/jsvine/markovify).

```
pip install tweepy
pip install markovify
```

### Accessing the Twitter API
You will need to set these environment variables corresponding to the consumer/access keys and secrets of your Twitter App:

```
CONSUMER_KEY
CONSUMER_SECRET
ACCESS_KEY
ACCESS_SECRET
```


### Settings

The config.ini file looks like this:

```
[SETTINGS]
BOT_SCREEN_NAME = @usernameofthebot
TWEETS = 150
```

`TWEETS` is the number of tweets will be used to generate the Markov chain sentence. `BOT_SCREEN_NAME` is the twitter screen name of the bot, such as @mockingbirdbot
