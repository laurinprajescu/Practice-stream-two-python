import pymongo

def mongo_connect():
    try:
        conn = pymongo.MongoClient()
        print "Mongo is connected!"
        return conn
    except pymongo.errors.ConnectionFailure, e:
        print "Could not connect to MongoDB: %s" % e

conn = mongo_connect()
db = conn['twitter_stream']
coll = db.my_collection
print conn.database_names()  # [u'local', u'test']