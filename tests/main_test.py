### Test for onpublish/main.py
# Should pass getting feed and sending tweet

from scripts import main

def test_main():
    
    program_path = "./program"
    type = "main_test"
    url = "http://registerguard.com/csp/cms/sites/rg/feeds/rss.csp"
    payload = {'pub': 'rg', 'section': 'local', 'area': 'Updates'}
    id_file = "id_files/id_file_example.txt"
    
    # Try tweet
    responses = main(program_path, type, url, payload)
    
    for key, value in responses:
        assert ( value == "success")
