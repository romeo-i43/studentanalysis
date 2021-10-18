import streamlit as st
import pandas as pd
import plotly_express as px

def app():
    st.title('ploty')
    st.subheader('graph')
    st.markdown('---')
    df=pd.read_csv('sample.csv')
    graph=px.bar(
    df,
    x=df['roll_no'],
    y=[df['cgpa'],df['credits'],df['mid1']],
    )
    st.plotly_chart(graph)
