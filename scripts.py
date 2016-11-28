import os, logging, logging.handlers, requests, feedparser, tweepy, json, bitly_api

# Set vars
path = os.path.join(os.path.abspath(os.path.dirname(__file__)))

# logger --- See down in main() for more
log_file_dir = "{}/main/logs/".format(path)
log_level_set = logging.DEBUG
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# secrets
def getSecret(service, token='null'):
    logger.debug("ENTER secrets")
    #print "Service: {}".format(service)
    #print "Token: {}".format(token)
    with open("{}/secrets.json".format(path)) as data:
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

# rss
def getrss(url, payload):
    logger.debug("ENTER rss")
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
    

# bitly
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
    

# tweet
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
        logger.debug('Success! Tweet sent: ' + tweet_text)
    except tweepy.TweepError, err:
        logger.error(err)
        success = False
    logger.debug("EXIT tweet: {}".format(success))
    # Use success as return for now...
    # would rather return api status code...
    # See: https://github.com/registerguard/rssonpublish/issues/1
    return success
    

# onpublish
def main(url, payload, id_file, type):
    
    # logger --- See up at top for more...
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fileLogger = logging.handlers.RotatingFileHandler(filename=("{0}{1}.log".format(log_file_dir, type)), maxBytes=256*1024, backupCount=5) # 256 x 1024 = 256K
    fileLogger.setFormatter(formatter)
    logger.addHandler(fileLogger)
    # Uncomment below to print to console
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    logger.debug("ENTER onpublish")
    # Set vars
    response = {}
    
    feed = getrss(url, payload)
    
    #if the rss feed has items
    if feed.entries:
        
        #initiate new list
        id_list = []
        #populate list of ids
        for entry in feed.entries:
            id_list.append(entry.id)
        
        if (not os.path.isfile(id_file)):
            open(id_file, 'w')
            logger.debug("ID file does not exist, making one")
        
        #read past list of ids
        with open(id_file, 'r') as f:
            file_data = f.read()
        
        # loop over items in list
        for i, single_id in enumerate(id_list):
            # if item in list is not in data
            if single_id not in file_data:
                # set these vars
                feed_url = feed.entries[i].link
                feed_title = feed.entries[i].title.encode('utf-8')
                
                if feed_url and feed_title:
                    #print "{0}: {1} {2}\n\n".format(single_id, feed_title, feed_url)
                    logger.debug("URL and title present")
                    sendit(feed_url, feed_title)
                    response[single_id] = "Success"
                else:
                    response[single_id] = "Bad data"
                    logger.error("{}: No url or title".format(single_id))
                
            
        
        # overwrite the file
        with open(id_file, 'w') as text_file:
            text_file.write('{}'.format(id_list))
        
    logger.debug("EXIT onpublish: {}".format(response))
    #return response
    return response
    
