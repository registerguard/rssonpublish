### Test for rss.py
# Should return RSS feed

from utilities.rss import getit

def test_rss():
    # Set vars
    url = 'http://registerguard.com/csp/cms/sites/rg/feeds/rss.csp'
    payload = {'pub': 'rg', 'section': 'local', 'area': 'Updates'}
    
    response = getit(url, payload)
    print response
    assert (len(response))
    
