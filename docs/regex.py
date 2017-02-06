import re

regex = '([a-zA-Z0-9]\.[a-zA-Z0-9]+\.[x0-9])|(^Hed\s|\shed\s)|(\shery$|\sherey$)'

one = "This is a proper headline"
two = "cr.whatever.xxxx"
three = "a1.blah.0131"
four = "b2.cr.test2notes.03xx"
five = "Headly he go herey"
six = "Hed goes hery"
seven = "Big hed goes here"
eight = "He breathed a sigh of relief"
nine = "Blah blah asdfhery"

mylist = [one,two,three,four,five,six,seven,eight,nine]

for hed in mylist:
    if re.search(regex,hed):
        print "{0} --- TRUE".format(hed)
    else:
        print "{0} --- FALSE".format(hed)
