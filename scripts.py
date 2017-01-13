import os, logging, logging.handlers, requests, feedparser, tweepy, json, bitly_api

# # logger
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)
# #logger.setLevel(logging.ERROR)

# ----------------------------------------------------------------------------------------
# SECRETS
# ----------------------------------------------------------------------------------------

def getSecret(service, token='null'):
    
    secrets_path = os.path.join(os.path.abspath(os.path.dirname(__file__)))
    #print "Service: {}".format(service)
    #print "Token: {}".format(token)
    with open("{}/secrets.json".format(secrets_path)) as data:
        s = json.load(data)
        #print s
        #print s['{}'.format(service)]['{}'.format(token)]
        # If there is no token, return whole parent object
        if token == 'null':
            secret = s['{}'.format(service)]
        else:
            secret = s['{}'.format(service)]['{}'.format(token)]
        logger.debug("EXIT secrets: {}".format(len(secret)))
        return secret

# ----------------------------------------------------------------------------------------
# RSS
# ----------------------------------------------------------------------------------------

def getrss(url, payload):
    
    # Make request
    # See: http://stackoverflow.com/a/16511493
    try:
        r = requests.get(url, params=payload, timeout=5)
        logger.debug("rss success")
    except requests.exceptions.RequestException as e:
        # catastrophic error. bail.
        print e
        logger.error("Requests error: {}".format(e))
    
    #print r.url
    html = r.text
    
    # Parse the RSS
    feed = feedparser.parse(html)
    logger.debug("EXIT rss: Feed length {}".format(len(feed)))
    return feed
    

# ----------------------------------------------------------------------------------------
# BITLY
# ----------------------------------------------------------------------------------------

def getURL(full_url):
    logger.debug("ENTER bitly")
    # Get access token from bitly object in secrets.json
    access_token = getSecret('bitly','access_token')
    
    # See: https://github.com/bitly/bitly-api-python
    bitly = bitly_api.Connection(access_token=access_token)
    try:
        bitlyurl = bitly.shorten(full_url)
        #print bitlyurl
        shorturl = str(bitlyurl[u'url'])
        logger.debug("ShortURL: {}".format(shorturl))
        #print "success"
    except bitly_api.bitly_api.BitlyError, err:
        shorturl = full_url
        logger.error(err)
        #print "Error: {}".format(err)
    logger.debug("EXIT bitly: {}".format(shorturl))
    return shorturl
    

# ----------------------------------------------------------------------------------------
# TWEET
# ----------------------------------------------------------------------------------------

def sendit(feed_url, feed_title):
    logger.debug("ENTER tweet")
    success = False
    
    # Get access token from secrets.json
    secrets = getSecret('twitter-rob')
    consumer_key = secrets['consumer_key']
    consumer_secret = secrets['consumer_secret']
    access_token = secrets['access_token']
    access_token_secret = secrets['access_token_secret']
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    
    #bitly
    shorturl = getURL(feed_url)
    
    # construct string to tweet
    tweet_text = "{0} {1}".format(feed_title, shorturl)
    
    # Comment out this line to not send the tweet
    try:
        # Comment out line below to not send tweet each test...
        # would be nice to make this a test variable or something
        #api.update_status(status=tweet_text)
        #print tweet_text
        success = True
        #logger.debug('Success! Tweet sent: ' + tweet_text)
        logger.error('Success! Tweet sent: ' + tweet_text)
    except tweepy.TweepError, err:
        logger.error(err)
        success = False
    logger.debug("EXIT tweet: {}".format(success))
    # Use success as return for now...
    # would rather return api status code...
    # See: https://github.com/registerguard/rssonpublish/issues/1
    return success
    
