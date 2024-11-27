# Import required libraries
from flask import Flask,request # type: ignore
import pandas as pd 
import numpy as np
import pickle
from flasgger import Swagger # type: ignore

# Initialize flask
app = Flask(__name__)

# Initialize app inside Swagger
Swagger(app)

# Read trained model
with open('./model/classifier.pkl','rb') as pickle_in:
    clf = pickle.load(pickle_in)

# Function for home page
@app.route('/')
def welcome():
    return "Welcome Everyone!!"    

# Function for prediction using single input
@app.route('/predict')
def predict():
    """
    Let's authenticate the Bank Note
    This is using docstrings for specifications.
    ---
    parameters:
        - name: variance
          in: query
          type: number
          required: true
        - name: skewness
          in: query
          type: number
          required: true
        - name: curtosis
          in: query
          type: number
          required: true
        - name: entropy
          in: query
          type: number
          required: true
    responses:
          200:
                description: The output values
    """
    variance = request.args.get('variance')
    skewness = request.args.get('skewness')
    curtosis = request.args.get('curtosis')
    entropy = request.args.get('entropy')
    prediction = clf.predict([[variance,skewness,curtosis,entropy]])
    return "The predicted value is " + str(prediction)

# Function for prediction using test file
@app.route('/predict_file',methods=['POST'])
def predict_file():
    """
    Let's authenticate the Bank Note
    This is using docstrings for specifications.
    ---
    parameters:
        - name: file
          in: formData
          type: file
          required: true
    responses:
          200:
                description: The output values
    """
    df = pd.read_csv(request.files.get('file'))
    prediction = clf.predict(df)
    return "The predicted values for the CSV is " + str(list(prediction))

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)