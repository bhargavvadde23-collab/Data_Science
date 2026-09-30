import pandas as pd
import numpy as np
import pickle
from flask import Flask,request,jsonify,render_template
from sklearn.preprocessing import StandardScaler

application=Flask(__name__)

app=application

#import pickle files

ridge_model=pickle.load(open('ridge.pkl','rb'))
scaler_standard=pickle.load(open('scaler.pkl','rb'))

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predictdata",methods=['GET','POST'])
def predict_data():
    if request.method=='POST':
        
        Temparature=float(request.form.get('Temparature'))
        RH=float(request.form.get('RH'))
        Ws=float(request.form.get('Ws'))
        Rain=float(request.form.get('Rain'))
        FFMC=float(request.form.get('FFMC'))
        DMC=float(request.form.get('DMC'))
        ISI=float(request.form.get('ISI'))
        Classes=float(request.form.get('Classes'))
        Region=float(request.form.get('Region'))
        
        new_data_scaled=scaler_standard.transform([[Temparature,RH,Ws,Rain,FFMC,DMC,ISI,Classes,Region]])
        result=ridge_model.predict(new_data_scaled)
        
        return render_template('home.html',results=result[0])
        
        
    else:
        return render_template("home.html")
        
        

if __name__=="__main__":
    app.run(debug=True) 
