### Test for trim()
# Should trim a string down to less than 105 characters

from scripts import trim

def test_trim():
    
    hed = "This is a really long headline that is  way, way too long for Twitter's API because of the extreme detail in the headline's text"
    
    newhed = trim(hed)
    
    assert (len(newhed) <= 105)