import requests, feedparser, logging

def getrss(url, payload):
    
    # Make request
    # See: http://stackoverflow.com/a/16511493
    try:
        r = requests.get(url, params=payload, timeout=5)
        logging.debug("rss success")
    except requests.exceptions.RequestException as e:
        # catastrophic error. bail.
        print e
        logging.debug("Requests error: {}".format(e))
        
    
    #print r.url
    html = r.text
    
    # Parse the RSS
    feed = feedparser.parse(html)
    
    return feed
    
