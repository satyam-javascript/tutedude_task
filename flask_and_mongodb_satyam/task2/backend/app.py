import os
from flask import Flask, jsonify, request # type: ignore
from flask.cli import load_dotenv
from pymongo import MongoClient
import pymongo

load_dotenv()  # Load environment variables from .env file
MONGO_URI = os.getenv("MONGO_URI")  # Get the MongoDB URI from environment variables

client =pymongo.MongoClient(MONGO_URI)  # Create a MongoDB client
db = client.devtest  # Access the database (replace "mydatabase" with your database name)
collection = db["user"]  # Access the collection (replace "mycollection" with your collection name) 
app = Flask(__name__)



@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        form_data = dict(request.json)

        # Insert the form data into the MongoDB collection
        try:
            collection.insert_one(form_data)
            if "_id" in form_data:
                form_data["_id"] = str(form_data["_id"])
            return { "message": "Form submitted successfully!",
                    "data": form_data
                    }
        except Exception as e:
            return { "error": f'Error occurred while submitting form: {str(e)}' }

#view all data from the collection
@app.route('/view', methods=['GET'])
def view_data():
    data = list(collection.find({}, {'_id': 0}))  # Exclude the '_id' field from the results
    return jsonify(data)
 
if __name__ == "__main__":
    app.run(debug=True)