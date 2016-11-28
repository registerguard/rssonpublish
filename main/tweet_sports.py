import logging, os
from scripts import main

# Set vars
path = log_file_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)))
name = "tweet_sports"
url = "http://registerguard.com/csp/cms/sites/rg/feeds/rss.csp"
payload = {'pub': 'rg', 'section': 'sports', 'area': 'Top Updates'}
id_file = "{0}/id_files/{1}.id".format(path, name)

main(url, payload, id_file, name)
