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



















if __name__ == '__main__':
    app.run(debug=True)



