# Import urllib
import urllib.request, urllib.parse, urllib.error
# Import augment this url and deals with authorization problem 
# it also combined with hidden.py to get token for authorization
import twurl
# Import json
import json
# Import ssl to ignore certificate errors
import ssl

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

# here is where you will go to get a friends list
TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# While loop, indefinite loop, infinite or break
while True:
    print('')

    # Twitter screen name prompt and put it in acct variable
    acct = input('Enter Twitter Account:')

    # If you hit enter you will skip out
    if (len(acct) < 1): break


    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '5'})

    # it includes login information in this url
    print('Retrieving', url)

    # file handler = urlopen
    connection = urllib.request.urlopen(url, context=ctx)

    # decode from utf-8 to string representation of the json
    data = connection.read().decode()

    # this is the line to get the headers and return as dictionary
    headers = dict(connection.getheaders())

    # x-rate-limit-remaining will give you number 12 - 0,
    # it will print out whats left
    print('Remaining', headers['x-rate-limit-remaining'])

    # json.load string from DATA and return a dictionary 
    js = json.loads(data)

    # this will pretty print it with indent of 4
    # this will look like how you see a json file
    print(json.dumps(js, indent=4))

    # for each users in js['users'] array as seen in json file
    for u in js['users']:

        # this will print the screen_name
        print(u['screen_name'])

        # filter if status not found inside the array, will print No status found then continue
        # when there is no status inside the file
        if 'status' not in u:
            print('   * No status found')
            continue

        # inside the ustatus get the text value
        s = u['status']['text']

        # print slice 0 to 50 but not 50
        print('  ', s[:50])
