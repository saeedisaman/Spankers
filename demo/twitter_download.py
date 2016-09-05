from __future__ import absolute_import, print_function
import time
import tweepy
import pymongo
import json


MONGODB_URI = 'mongodb://spankyspankers:ispank@ds019906.mlab.com:19906/spankyspankers'


# == OAuth Authentication ==
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
consumer_key="RssIanbS5WX1XTUZ8wAQWGaGk"
consumer_secret="mfXfFyJJARsb7C4rZvhI3jvJjOE5WAIW1LgnsVpQ1qGASWc7Rn"

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located
# under "Your access token")
access_token="2155730588-Rg26W5mSYmSq2ReTbWwW4pBV4z3AdxU304fC8DO"
access_token_secret="MflGiuJ6hKiNfI3mU3GCxtgP07QbD7OwyWPa82SXBN7RO"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# If the authentication was successful, you should
# see the name of the account print out
print(api.me().name)

# If the application settings are set for "Read and Write" then
# this line should tweet out the message to your account's
# timeline. The "Read and Write" setting is on https://dev.twitter.com/apps
# api.update_status(status='Updating using OAuth authentication via Tweepy!')
search_text = "#oil since:2015-12-21"
# search_number = 2
# search_result = api.search(search_text, rpp=search_number)
# print(len(search_result))
# for i in search_result:
#     print (i.text)
#
# above omitted for brevity


class querrybuilder(object):
    def __init__(self,this_object=""):
        self.this_object = this_object
    def since(self,time):
        self.this_object += " since:"+time
        return self
    def content(self,content):
        self.this_object += " "+content
        return self
    def hashtag(self,hashtag):
        self.this_object += " #"+hashtag
        return self
    def until(self,time):
        self.this_object += " until:"+time
        return self
    def from_a(self,account):
        self.this_object += " from:"+account
        return self
    def return_q(self):
        return self.this_object


def write(data):
    client = pymongo.MongoClient(MONGODB_URI)

    db = client.get_default_database()

    # First we'll add a few songs. Nothing is required to create the songs
    # collection; it is created automatically when we insert.

    songs = db['tweets']

    # Note that the insert method can take either an array or a single dict.

    songs.insert(data)
    client.close()


q = querrybuilder("oil").hashtag("OPEC")
print(q.return_q())
c = tweepy.Cursor(api.search,
                       q=search_text,
                       include_entities=True).items()
a =100
tweets = []
while a>1:
    try:
        tweet = c.next()
        print((tweet))
        a-=1
        tweets.append(tweet._json)
        # Insert into db
    except tweepy.TweepError:
        time.sleep(60 * 15)
        continue
    except StopIteration:
        break
write(tweets)
print(q.return_q())


