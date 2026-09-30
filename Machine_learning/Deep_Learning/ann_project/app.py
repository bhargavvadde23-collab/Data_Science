import streamlit as st 
import tensorflow as tf
from sklearn.preprocessing import StandardScaler,LabelEncoder,OneHotEncoder
import pandas as pd
import numpy as np
import pickle

#Load Model
model=tf.keras.models.load_model('model.h5')

#Load transformation files
with open('label_encoder_gender.pkl','rb') as file:
    label_gender=pickle.load(file)
    
with open('onehot_encoder_geo.pkl','rb') as file:
    onehot_geo=pickle.load(file)
    
with open('scaler.pkl','rb') as file:
    scaler=pickle.load(file)
    
st.title("Churn Prediction model")


#User input

geography= st.selectbox('Geography' , onehot_geo.categories_[0])
gender= st.selectbox('Gender' , label_gender.classes_)
age=st.slider('Age', 18 ,92)
balance=st.number_input('Balance')
credit_score=st.number_input('Credit Score')
estimated_salary=st.number_input('EstimatedSalary')
tenure=st.slider('Tenure',0,10)
num_of_products=st.slider('NumOfProducts',1,10)
has_credit_card=st.selectbox('HasCrCard',[0,1])
is_active_member=st.selectbox('IsActiveMember',[0,1])


#Prepare the dataset

input_data=pd.DataFrame({
    'CreditScore':[credit_score],
    'Gender':[label_gender.transform([gender])[0]],
    'Age':[age],
    'Tenure':[tenure],
    'Balance':[balance],
    'NumOfProducts':[num_of_products],
    'HasCrCard':[has_credit_card],
    'IsActiveMember':[is_active_member],
    'EstimatedSalary':[estimated_salary],
})


#Onehot encode Geography

geo_encoded=onehot_geo.transform([[geography]]).toarray()
geo_encode_df=pd.DataFrame(geo_encoded,columns=onehot_geo.get_feature_names_out(['Geography']))


input_data=pd.concat([input_data.reset_index(drop=True),geo_encode_df],axis=1)

input_scaled=scaler.transform(input_data)

prediction=model.predict(input_scaled)
prediction_proba=prediction[0][0]

if prediction_proba > 0.5:
    st.write('Customer is likely to churn')

else:
    st.write('Customer is not likely to churn')