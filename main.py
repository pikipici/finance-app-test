import streamlit as st
import pandas as pd
import plotly.express as px
import json
import os

st.set_page_config(page_title="Finance App Test", page_icon="💵", layout="wide")

def load_transactions(file):
    pass 

def main():
    st.title("Finance App Test")
    
    uploaded_file = st.file_uploader("Upload FIle dalam bentuk (CSV)", type=["csv"])
    
    if uploaded_file is not None:
        df = load_transactions(uploaded_file)
        

main()