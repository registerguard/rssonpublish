from utilities.rss import getrss
from utilities.tweet import sendit
import os

### Set vars
# RSS
# url = 'http://registerguard.com/csp/cms/sites/rg/feeds/rss.csp'
# payload = {'pub': 'rg', 'section': 'local', 'area': 'Updates'}


def checknsend(url, payload, id_file):
    
    # Set vars
    response = {}
    
    feed = getrss(url, payload)
    #print feed.url # THIS IS NO GOOD, need to do in get it for requests .url
    
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
                    response[single_id] = "Success"
                    
                else:
                    response[single_id] = "Bad data"
                    
                
            
        
        # overwrite the file
        with open(id_file, 'w') as text_file:
            text_file.write('{}'.format(id_list))
            
        
    #return response
    return response