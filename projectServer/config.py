import pymongo
import certifi

me = {"first": "Neil",
          "last": "Tejada",
          "email": "neiltejada86@gmail.com"
          }

con_string = "mongodb+srv://FSDI:Test1234@cluster0.7paka8f.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(con_string, tlsCAFile=certifi.where())
db = client.get_database("salsa_store")