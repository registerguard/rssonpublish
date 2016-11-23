import logging, os
from utilities.onpublish import checknsend

#path = "/Users/rdenton/github/registerguard/rssonpublish"
path = log_file_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)))
name = "tweet_news"

logging.basicConfig(filename="{0}/logs/{1}.log".format(path, name),level=logging.ERROR,format="%(asctime)s --- %(levelname)s: %(message)s")
logging.debug("***ENTER {}.py***".format(name))

# Set vars
url = "http://registerguard.com/csp/cms/sites/rg/feeds/rss.csp"
payload = {'pub': 'rg', 'section': 'local', 'area': 'Updates'}
id_file = "{0}/id_files/{1}.id".format(path, name)

logging.debug

checknsend(url, payload, id_file)

logging.debug("***ENDING tweet_news.py***")
logging.debug("**************************************************")
