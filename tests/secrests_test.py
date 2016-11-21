### Test for secrets.py
# Should return length of secret token

from utilities.secrets import getSecret

def test_secrets():
    
    access_token = getSecret('bitly')
    
    assert (len(access_token))