import tweepy
from bitly import getURL
from secrets import getSecret

def sendit(feed_url, feed_title):
    
    success = False
    
    # Get access token from bitly object in secrets.json...
    # would like to condense this into one call in future...
    # See: https://github.com/registerguard/rssonpublish/issues/2
    consumer_key = getSecret('twitter-rob','consumer_key')
    consumer_secret = getSecret('twitter-rob','consumer_secret')
    access_token = getSecret('twitter-rob','access_token')
    access_token_secret = getSecret('twitter-rob','access_token_secret')
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    
    #bitly
    shorturl = getURL(feed_url)
    
    # construct string to tweet
    tweet_text = feed_title + ' ' + shorturl
    
    # Comment out this line to not send the tweet
    try:
        # Comment out line below to not send tweet each test
        #api.update_status(status=tweet_text)
        success = True
        #logger.debug('Success! Tweet sent: ' + tweet_text)
    except tweepy.TweepError, err:
        #logger.debug(err)
        success = False
    
    # Use success as return for now...
    # would rather return api status code...
    # See: https://github.com/registerguard/rssonpublish/issues/1
    return success
