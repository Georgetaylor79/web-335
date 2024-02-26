# Title: taylor_usersp2.py
# Author: George Taylor
# Date: 02/25/24
# Description: Exercise 7.3 - Python with MongoDB, Part 2

# import MongoClient
from pymongo import MongoClient
import datetime

# build connection string to connect to the client
myclient = MongoClient(
    "mongodb+srv://taylor79:s3cret@cluster0.f36akkm.mongodb.net/")

db = myclient['web335DB']

# Write the Python code to create a new user document.
db.users.insert_one({
    "firstName": "Andrew",
    "lastName": "Wiggins",
    "employeeId": "1014",
    "email": "Awigg@me.com",
    "dateCreated": datetime.datetime.now()
})


# Write the Python code to display the newly created document.
print(db.users.find_one({"employeeId": "1014"}))

# Write the Python code to update the email address of the document you created in step 2.
print(db.users.update_one(
    {"email": "Awigg@me.com"},
    {"$set": {"email": "Andrewing@me.com"}}
))

# Write the Python code to display the updated document.
print(db.users.find_one({"email": "Andrewing@me.com"}))

# Write the Python code to delete the document you created in step 3.
db.users.delete_one({"email": "Andrewing@me.com"})

# Write the Python code to prove the document was deleted.
print(db.users.find_one({"email": "Andrewing@me.com"}))