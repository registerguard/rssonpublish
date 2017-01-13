import os, logging, logging.handlers
from scripts import getrss, sendit, getsecret

# onpublish
# Don't think this needs to be a function
#def main(program_path, type, url, payload):

# ----------------------------------------------------------------------------------------
# LOGGING INITIALIZATION
# ----------------------------------------------------------------------------------------

logger = logging.getLogger(__name__)
# set level
logger.setLevel(logging.DEBUG)
#logger.setLevel(logging.ERROR)

# set vars
log_file_dir = "{}/logs/".format(program_path)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
fileLogger = logging.handlers.RotatingFileHandler(filename=("{0}{1}.log".format(log_file_dir, type)), maxBytes=256*1024, backupCount=5) # 256 x 1024 = 256K
fileLogger.setFormatter(formatter)
logger.addHandler(fileLogger)

# Uncomment below to print to console
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)

# ----------------------------------------------------------------------------------------
# START MAIN SCRIPT
# ----------------------------------------------------------------------------------------

logger.debug("ENTER onpublish")
# Set vars
response = {}
id_file = "{0}/id_files/{1}.id".format(program_path, type)

feed = getrss(url, payload)
logger.debug("got feed")

#if the rss feed has items
if feed.entries:
    logger.debug("in feed.entries")
    #initiate new list
    id_list = []
    #populate list of ids
    for entry in feed.entries:
        id_list.append(entry.id)
    
    if (not os.path.isfile(id_file)):
        open(id_file, 'w')
        logger.debug("ID file does not exist, making one")
    
    #read past list of ids
    with open(id_file, 'r') as f:
        file_data = f.read()
    
    # loop over items in list
    for i, single_id in enumerate(id_list):
        # if item in list is not in data
        if single_id not in file_data:
            # set these vars
            feed_url = feed.entries[i].link
            feed_title = feed.entries[i].title.encode('utf-8')
            logger.debug("{0}: {1}".format(single_id, feed_title))
            
            if feed_url and feed_title:
                #print "{0}: {1} {2}\n\n".format(single_id, feed_title, feed_url)
                logger.debug("URL and title present")
                sendit(feed_url, feed_title)
                response[single_id] = "Success"
            else:
                response[single_id] = "Bad data"
                logger.error("{}: No url or title".format(single_id))
            
        
    
    # overwrite the file
    with open(id_file, 'w') as text_file:
        text_file.write('{}'.format(id_list))
    
logger.debug("EXIT onpublish: {}".format(response))
#return response
return response

