import os

def info():
    data = {}
    data['program_path'] = os.path.join(os.path.abspath(os.path.dirname(__file__)))
    data['type'] = 'twitter-staging'
    data['url'] = "http://registerguard.com/csp/cms/sites/rg/feeds/rss.csp"
    data['payload'] = {'pub': 'rg', 'section': 'staging', 'area': 'Top Stories'}
    return data

