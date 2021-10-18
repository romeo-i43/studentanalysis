import streamlit as st
import pandas as pd
import plotly_express as px

def app():
    st.title('ploty')
    st.subheader('table')
    st.markdown('---')
    df=pd.read_csv('sample.csv')
    st.dataframe(df)
