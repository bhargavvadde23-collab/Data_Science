import streamlit as st

import pandas as pd
import numpy as np



#Title of the application
st.title("Hello Welcome")

st.write("This is a Streamlit web application")


df=pd.DataFrame(
    {
        'First column':[1,2,3,4],
        'Second column':[5,6,7,8]
    }
)

#Writing a Dataset


st.write("Here is the dataframe")
st.write(df)

chart_data=pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.write(chart_data)

st.line_chart(chart_data)
