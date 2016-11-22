### Test for onpublish/main.py
# Should pass getting feed and sending tweet

from utilities.onpublish import checknsend

def test_main():
    
    url = 'http://registerguard.com/csp/cms/sites/rg/feeds/rss.csp'
    payload = {'pub': 'rg', 'section': 'sports', 'area': 'Top%20Updates'}
    
    # Try tweet
    responses = checknsend(url,payload)
    
    for key, value in responses:
        assert ( value == "success")
