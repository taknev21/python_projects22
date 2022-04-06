# 1st Method
frompymongo import MongoClient
import ssl
import pprint

mongoDB_uri = ("mongodb://username:password@hostname.com:port/admin")
client = MongoClient (mongoDB_uri,ssl=True, ssl_cert_reqs=ssl.CERT_REQUIRED,ssl_ca_certs="/tmp/cachain.pem")

db = client.dbname

#print the number of documents in a collection
print (db.collection.count())


