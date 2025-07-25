from flask import Flask, render_template, request
import pymongo
from dotenv import load_dotenv
import os

load_dotenv()
MONGO_URI = os.getenv('MONGO_URI')

client = pymongo.MongoClient(MONGO_URI)

db=client.test1
collection = db['git_assignment_db']


app = Flask(__name__)
@app.route('/')
def home():
    a="Hello, Guys! Welcome to the To-Do App!."
    print(a)
    # return render_template('to_do.html',a=a)
    items = list(collection.find())
    return render_template('to_do.html', items=items ,a=a)

@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    item_name = request.form.get('item_name')  # <-- changed here
    item_desc = request.form.get('itemDescription')
    item_id = request.form.get('itemID')
    item_uuid = request.form.get('itemUUID')

    if item_name and item_desc and item_id:
        collection.insert_one({
            "item_name": item_name,
            "item_desc": item_desc,
            "item_id": item_id,
            "item_uuid": item_uuid

        })
        print(f"Item Name: {item_name}, Item Description: {item_desc}, Item ID: {item_id}, Item UUID: {item_uuid}")
        return "Item added successfully!"
    else:
        return "Missing data", 400

















if __name__ == '__main__':
    app.run(debug=True)



