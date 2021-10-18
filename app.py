import streamlit as st
from multiapp import MultiApp
import plot, table

app=MultiApp()

app.add_app("plot",plot.app)
app.add_app("table",table.app)

app.run()

