import streamlit as st 
import pandas as pd

st.title("Stream Text-Input")

name=st.text_input("Enter your name:")
st.write(f'Hello {name}')

age=st.slider("Enter your age:",0,100,25)
st.write(f'Selected age is {age}')

options=['Python','C','Java','C++']
choice=st.selectbox("Enter your favorite lang:",options)

st.write(f'you have slected {choice}')



data={
    "Name":['bhargav','Krishna','Arjun','Ram'],
    "Age":[22,23,22,21],
    "City":['Bangalore','Kerala','AP','Chennai']
}


df=pd.DataFrame(data)

df.to_csv("sampledata.csv")

upload_file=st.file_uploader("Choose a file",type="csv")

if upload_file is not None:
    df=pd.read_csv(upload_file)
    st.write("Data is-->")
    st.write(df)

