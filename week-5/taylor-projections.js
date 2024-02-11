// Title: taylor-projections.js
// Author: George Taylor 
// Date: 02/11/2024
// Description: queries for displaying user information from a mongoDB database.


// query to add a new user to the user's collection
printjson( db.users.insertOne({"firstName": 'Frederic', "lastName" : 'Chopin', "employeeId": '1013', "email": 'fchopin@me.com', "dateCreated": new Date()}));

// query that updates Mozart's email address to mozart@me.com. Second, Write a query to prove the email address was updated
printjson(db.users.updateOne({"email": "wmozart@me.com"},{"$set":{"email": "mozart@me.com"}}));
printjson(db.users.findOne({"email": "mozart@me.com"}));

// query that lists all the documents in the user's collection. Only display the firstName, lastName, and email fields.
printjson(db.users.aggregate([{$project: {_id: 0,firstName: 1,lastName: 1,email: 1}}]));