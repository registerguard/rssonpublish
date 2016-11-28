### Test for tweet.py
# Should pass for tweet sent

from scripts import sendit

def test_tweet():
    
    feed_url = "http://registerguard.com/rg/sports/34996615-81/duck-pod-all-about-utah-with-kurt-kragthorpe-of-the-salt-lake-tribune.html.csp"
    feed_title = "Duck Pod: All about Utah with Kurt Kragthorpe of The Salt Lake Tribune"
    
    # Try tweet
    success = sendit(feed_url, feed_title)
    
    assert (success == True)
