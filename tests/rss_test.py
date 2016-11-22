### Test for rss.py
# Should return RSS feed

from utilities.rss import getrss

def test_rss():
    # Set vars
    url = 'http://registerguard.com/csp/cms/sites/rg/feeds/rss.csp'
    payload = {'pub': 'rg', 'section': 'local', 'area': 'Updates'}
    
    response = getrss(url, payload)
    assert (len(response))
    
