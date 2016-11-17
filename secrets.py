import json

def getSecret(service, token='null'):
    #print "Service: {}".format(service)
    #print "Token: {}".format(token)
    with open('secrets.json') as data:
        s = json.load(data)
        #print s
        #print s['{}'.format(service)]['{}'.format(token)]
        # If there is no token, return whole parent object
        if token == 'null':
            secret = s['{}'.format(service)]
        else:
            secret = s['{}'.format(service)]['{}'.format(token)]
        return secret
