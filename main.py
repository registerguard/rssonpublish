from rss import getit
from tweet import sendit
import os

### Set vars
# RSS
url = 'http://registerguard.com/csp/cms/sites/rg/feeds/rss.csp'
payload = {'pub': 'rg', 'section': 'local', 'area': 'Updates'}
# Main
id_file = 'id.txt'

feed = getit(url, payload)

#if the rss feed has items
if feed.entries:
    
    #initiate new list
    id_list = []
    #populate list of ids
    for entry in feed.entries:
        id_list.append(entry.id)
    
    if (not os.path.isfile(id_file)):
        
        open(id_file, 'w')
        
    
    #read past list of ids
    with open(id_file, 'r') as f:
        file_data = f.read()
        
    print "beginning: {}".format(file_data)
    
    # loop over items in list
    for i, single_id in enumerate(id_list):
        
        # if item in list is not in data
        if single_id not in file_data:
            
            # set these vars
            feed_url = feed.entries[i].link
            feed_title = feed.entries[i].title
            
            if feed_url and feed_title:
                
                #print "{0}: {1} {2}\n\n".format(single_id, feed_title, feed_url)
                sendit(feed_url, feed_title)
                response = "success"
                
            else:
                response = "missing title or url"
                
            
        
    
    # overwrite the file
    with open(id_file, 'w') as text_file:
        text_file.write('{}'.format(id_list))
        
    
#return response