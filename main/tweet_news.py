from utilities.onpublish import checknsend

# Set vars
url = "http://registerguard.com/csp/cms/sites/rg/feeds/rss.csp"
payload = {'pub': 'rg', 'section': 'local', 'area': 'Updates'}
id_file = "id_files/tweet_news_id.txt"

checknsend(url, payload, id_file)