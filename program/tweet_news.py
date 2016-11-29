import os
from scripts import main

# Set vars
program_path = log_file_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)))
type = "tweet_news"
url = "http://registerguard.com/csp/cms/sites/rg/feeds/rss.csp"
payload = {'pub': 'rg', 'section': 'local', 'area': 'Updates'}

main(program_path, type, url, payload)
