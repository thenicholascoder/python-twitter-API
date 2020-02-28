# REQUIREMENT update 4 keys in hidden.py first before running

# import urllib library, import augment method from twurl
import urllib.request, urllib.parse, urllib.error
from twurl import augment

# import ssl library to ignore certification errors
import ssl

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

# printing current status
print('* Calling Twitter...')

# this will ask for user timeline

# will get the base parameter, a url which is https://api.twitter.com/1.1/statuses/user_timeline.json
# then we will pass second parameter, screen_name and count
# then we will use augment method from twurl.py which will
# will use oauth, an open protocol to allow secure authorization
# augment will use the 4 keys/codes to return oauth_request.to_url()
# 4 codes/must be updated inside hidden.py
url = augment('https://api.twitter.com/1.1/statuses/user_timeline.json',
              {'screen_name': 'drchuck', 'count': '2'})

# will print the augmented url data
print(url)

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# make a file handler
# context=ctx will shut off security checking for the SSL certificate
# this also eats the headers but you can get them back
connection = urllib.request.urlopen(url, context=ctx)

# then will read the connection from file handler
data = connection.read()

# this will produce byte array since you didnt have .decode()
# the array will produce utf-8

# print the data
print(data)

print ('======================================')

# ask for headers from the connection and return it as dictionary
headers = dict(connection.getheaders())

# print the headers
print(headers)
