In this code, we first create a pymongo client object by specifying the MongoDB server URL. We then get the desired database and collection to store the data in.

We define the data we want to store in the collection in the form of a Python dictionary. In this case, we define a simple example document with name, age, and email fields.

Finally, we insert the data into the collection using the insert_one() method, which returns a pymongo.results.InsertOneResult object. We print out the ID of the inserted document to confirm that the data was saved successfully.

Note that the code assumes that MongoDB is running on the default port (27017) on the local machine. If you are using a remote MongoDB server or a different port, you will need to modify the pymongo.MongoClient() call accordingly.

You can similarly use the appropriate library for other NoSQL databases like Redis and Apache Cassandra to store data in their respective databases.