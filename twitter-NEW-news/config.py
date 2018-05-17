import os

def info():
    data = {}
    data['program_path'] = os.path.join(os.path.abspath(os.path.dirname(__file__)))
    data['type'] = 'twitter-NEW-news'
    #data['url'] = "http://www.registerguard.com/mobile-app/news"
    #data['payload'] = {'template': 'rss', 'mime': 'xml', 'c': '10'}
    data['url'] = 'http://www.registerguard.com/section/RSS-feed'
    data['payload'] = {'mime':'xml', 'profileId':'1000075', 'c':'10'}
    return data
