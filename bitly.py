import bitly_api
from secrets import getSecret

def getURL(full_url):
    
    # Get access token from bitly object in secrets.json
    access_token = getSecret('bitly','access_token')
    
    # See: https://github.com/bitly/bitly-api-python
    bitly = bitly_api.Connection(access_token=access_token)
    try:
        bitlyurl = bitly.shorten(full_url)
        #print bitlyurl
        shorturl = str(bitlyurl[u'url'])
        #print "success"
    except bitly_api.bitly_api.BitlyError, err:
        shorturl = full_url
        # logger.debug(err) # How to log from multiple files?
        #print "Error: {}".format(err)
    
    return shorturl
