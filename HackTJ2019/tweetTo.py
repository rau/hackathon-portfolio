import tweepy

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""


def loginTwitter():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    return api


def tweet(message, name, rep):
    api = loginTwitter()
    status = "@" + rep + " " + message + " - " + name
    api.update_status(status=status)
