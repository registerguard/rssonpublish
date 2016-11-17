### Test for bitly.py
# Should pass for any shortlink with rgne.ws netloc

from bitly import getURL
import urlparse

def test_bitly():
    # Pass in url to test
    feed_url = "http://registerguard.com/rg/sports/34996615-81/duck-pod-all-about-utah-with-kurt-kragthorpe-of-the-salt-lake-tribune.html.csp"
    # Go run script and return url
    url = getURL(feed_url)
    # Netloc should be rgne.ws
    # See: https://docs.python.org/2/library/urlparse.html#urlparse.urlparse
    netloc = urlparse.urlparse(url).netloc
    
    assert (netloc == "rgne.ws")
    #print url