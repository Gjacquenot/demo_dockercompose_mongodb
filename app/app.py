# https://www.mongodb.com/blog/post/getting-started-with-python-and-mongodb
# https://medium.com/faun/managing-mongodb-on-docker-with-docker-compose-26bf8a0bbae3

from pymongo import MongoClient
from random import randint
import os

MONGO_DB_USERNAME = os.getenv('MONGO_DB_USERNAME', 'test-user')
MONGO_DB_PASSWORD = os.getenv('MONGO_DB_PASSWORD', 'test-password')
MONGO_DB_DATABASE = os.getenv('MONGO_DB_DATABASE', 'test-database')

# URL = 'mongodb://localhost:27017/'
# URL = 'mongodb://mongodb:27017/'
URL = 'mongodb://%s:%s@mongodb:27017/%s' % (MONGO_DB_USERNAME, MONGO_DB_PASSWORD, MONGO_DB_DATABASE)
print(URL)
#Step 1: Connect to MongoDB - Note: Change connection string as needed
client = MongoClient(URL, retryWrites=True)
print(client)
db = client[MONGO_DB_DATABASE]

#Step 2: Create sample data
names = ['Kitchen', 'Animal', 'State', 'Tastey',
         'Big', 'City', 'Fish', 'Pizza', 'Goat',
         'Salty','Sandwich','Lazy', 'Fun']
company_type = ['LLC','Inc','Company','Corporation']
company_cuisine = ['Pizza', 'Bar Food', 'Fast Food', 'Italian',
                   'Mexican', 'American', 'Sushi Bar', 'Vegetarian']
for x in range(1, 51):
    business = {
        'name': names[randint(0, (len(names)-1))] + ' ' +
                company_type[randint(0, (len(company_type)-1))],
        'rating': randint(1, 5),
        'cuisine': company_cuisine[randint(0, (len(company_cuisine)-1))]
    }
    #Step 3: Insert business object directly into MongoDB via insert_one
    result = db.reviews.insert_one(business)
    #Step 4: Print to the console the ObjectID of the new document
    print('Created {0} of 50 as {1}'.format(x, result.inserted_id))

#Step 5: Tell us that you are done
print('Finished creating 50 business reviews')

fivestar = db.reviews.find_one({'rating': 5})
print(fivestar)
fivestarcount = db.reviews.find({'rating': 5}).count()
print(f"Number of five stars: {fivestarcount}")
print(f"Number of documents: {db.reviews.count_documents({})}")
