import requests, feedparser

def getit(url, payload):
    
    # Make request
    r = requests.get(url, params=payload)
    #print r.url
    html = r.text
    
    # Parse the RSS
    feed = feedparser.parse(html)
    
    return feed
    
