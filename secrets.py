import json

def getSecret(service, token):
    #print "Service: {}".format(service)
    #print "Token: {}".format(token)
    with open('secrets.json') as data:
        s = json.load(data)
        #print s
        #print s['{}'.format(service)]['{}'.format(token)]
        secret = s['{}'.format(service)]['{}'.format(token)]
        return secret
