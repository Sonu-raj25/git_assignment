from flask import Flask, request, render_template, redirect
import pymongo
from dotenv import load_dotenv
import os

load_dotenv()
MONGO_URI = os.getenv('MONGO_URI')

client = pymongo.MongoClient(MONGO_URI)

db=client.test1
collection = db['flask_tutorial_1']

app= Flask(__name__)

@app.route('/')
def home():
    a="Hello, Guys! Welcome to the home page."
    print(a)
    return render_template('assign3index.html',a=a)

@app.route('/submit', methods=['POST'])
def submit():
  try:  
      form_data = dict(request.form)
      collection.insert_one(form_data)
    # return "Data submitted successfully!"
      return redirect('/success')
  except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        a= "hello, Guys! Welcome to the home page."
        return render_template('assign3index.html', a=a, error=error_message)

@app.route('/success')
def success():
    return render_template('success.html', message="Data submitted successfully!")

if __name__ == '__main__':
    app.run(debug=True)



# from flask import Flask, request,render_template
# from datetime import datetime

# import pymongo

# from dotenv import load_dotenv
# import os

# load_dotenv()
# MONGO_URI = os.getenv('MONGO_URI')

# # client = pymongo.MongoClient("mongodb+srv://sonu:sonu123@cluster0.mdcbbtp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
#     #   or
# client = pymongo.MongoClient(MONGO_URI)

# db=client.test1
# collection = db['flask_tutorial_1']

# app= Flask(__name__)


# @app.route('/')
# def home():
#     now = datetime.now()
#     day_of_week = now.strftime("%A")
#     current_time = now.strftime("%H:%M:%S")
#     return render_template('assign3index.html',day_of_week=day_of_week,current_time=current_time)


# @app.route('/time')
# def time():
#     current_time = datetime.now().strftime("%H:%M:%S")
#     return current_time

# @app.route('/submit', methods=['POST'])
# def submit():
#     # name=request.form.get('name')
#     # return 'Hello ,'+ name 
#     form_data = dict(request.form)
#     collection.insert_one(form_data)
#     # print(form_data)
#     # return form_data
#     return 'Data submitted successfully!'


# @app.route('/view')
# def view():
#     data= collection.find()
#     data = list(data)

#     for item in data:
#         print(item)
#         del item['_id']

#     data = { 'data': data }

#     return data



# @app.route('/api')
# def game():
#     name = request.values.get('name')
#     age = request.values.get('age')

#     result = {
#         'name' : name,
#         'age' : age
#     }

#     return result





# if __name__ == '__main__':
#     app.run(debug=True)