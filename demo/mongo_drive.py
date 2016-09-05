# !/usr/bin/python

# Copyright (c) 2016 ObjectLabs Corporation
# Distributed under the MIT license - http://opensource.org/licenses/MIT

__author__ = 'mongolab'

# Written with pymongo-3.2
# Documentation: http://api.mongodb.org/python/
# A python script connecting to a MongoDB given a MongoDB Connection URI.

import sys
import pymongo

### Create seed data

# SEED_DATA = [
#     {
#         'decade': '1970s',
#         'artist': 'Debby Boone',
#         'song': 'You Light Up My Life',
#         'weeksAtOne': 10
#     },
#     {
#         'decade': '1980s',
#         'artist': 'Olivia Newton-John',
#         'song': 'Physical',
#         'weeksAtOne': 10
#     },
#     {
#         'decade': '1990s',
#         'artist': 'Mariah Carey',
#         'song': 'One Sweet Day',
#         'weeksAtOne': 16
#     }
# ]

### Standard URI format: mongodb://[dbuser:dbpassword@]host:port/dbname

MONGODB_URI = 'mongodb://spankyspankers:ispank@ds019906.mlab.com:19906/spankyspankers'


###############################################################################
# main
###############################################################################

class mongo_drive():

    def write(data):
        client = pymongo.MongoClient(MONGODB_URI)

        db = client.get_default_database()

        # First we'll add a few songs. Nothing is required to create the songs
        # collection; it is created automatically when we insert.

        songs = db['tweets']

        # Note that the insert method can take either an array or a single dict.

        songs.insert(data)

        # Then we need to give Boyz II Men credit for their contribution to
        # the hit "One Sweet Day".

        # query = {'song': 'One Sweet Day'}
        #
        # songs.update(query, {'$set': {'artist': 'Mariah Carey ft. Boyz II Men'}})

        # Finally we run a query which returns all the hits that spent 10 or
        # more weeks at number 1.

        # cursor = songs.find({'weeksAtOne': {'$gte': 10}}).sort('decade', 1)

        # for doc in cursor:
        #     print ('In the %s, %s by %s topped the charts for %d straight weeks.' %
        #            (doc['decade'], doc['song'], doc['artist'], doc['weeksAtOne']))

        ### Since this is an example, we'll clean up after ourselves.

        # db.drop_collection('songs')

        ### Only close the connection when your app is terminating

        client.close()


