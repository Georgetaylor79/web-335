
#import MongoClient
from pymongo import MongoClient

# build connection string
# substitute own connection string here
client = MongoClient()

# configure variable to access whatABook collection
db = client['whatABook']

# start mainline here