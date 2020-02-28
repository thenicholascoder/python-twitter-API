# import urllibrary, import twurl.py, import ssl
import urllib.request, urllib.parse, urllib.error
import twurl
import ssl

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

# base for twitter url
TWITTER_URL = 'https://api.twitter.com/1.1/statuses/user_timeline.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# indefinite, infinite loop, will stop only on break
while True:

    # space

    # prompt input then put inside the acct
    print('')
    acct = input('Enter Twitter Account:')

    # definite loop when user just enter, loop will go out the program
    if (len(acct) < 1): break

    # this will get TWITTER_URL base as first parameter
    # the second parameter is a dictionary with scree_name and count
    # then pass these parameters inside augment method
    # this will return signature with keys augmented after the base url
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '2'})
    
    # this will print the resulting url
    print('Retrieving', url)

    # create a file handler with context=ctx that will ignore ssl errors
    connection = urllib.request.urlopen(url, context=ctx)
    
    # this will read the file handler and then decode from string to utf-8
    data = connection.read().decode()
    
    # will print all the data from start to 250 but not 250 position
    print(data[:250])
    
    # will get the headers and then put it inside a dictionary
    headers = dict(connection.getheaders())

    # print headers
    print('Remaining', headers['x-rate-limit-remaining'])
