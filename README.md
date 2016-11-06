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

I have not yet set up global environment variables to handle keys/secrets. For now they are stored in a config.ini file that looks like this:

```
[TWITTER]
CONSUMER_KEY = 
CONSUMER_SECRET = 
ACCESS_KEY = 
ACCESS_SECRET = 
BOT_SCREEN_NAME = @usernameofthebot

[GENERATION]
TWEETS = 50
```

`TWEETS` is the number of tweets will be used to generate the Markov chain sentence
