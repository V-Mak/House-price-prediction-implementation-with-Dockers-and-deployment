import pickle
import bz2file as bz2
from flask import Flask,request,app,jsonify,url_for,render_template,redirect
import numpy as np
import pandas as pd

app=Flask(__name__)
regmodel=pickle.load(bz2.BZ2File('regmodel.pbz2','rb'))
scalar=pickle.load(open('scaling.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api',methods=['POST'])
def predict_api():
    data=request.json['data']
    print(data)
    print(np.array(list(data.values())).reshape(1,-1))
    new_data=scalar.transform(np.array(list(data.values())).reshape(1,-1))
    output=regmodel.predict(new_data)
    print(output[0])
    return jsonify(output[0])

@app.route('/predict',methods=['POST'])
def predict():
    data=[float(x) for x in request.form.values()]
    final_input=scalar.transform(np.array(data).reshape(1,-1))
    print(final_input)
    output=regmodel.predict(final_input)[0]
    return render_template('home.html',prediction_text="The House Price Prediction is {}".format(output))

if __name__=="__main__":
    app.run(host="0.0.0.0",port=8080)

