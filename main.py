import streamlit as st
import datetime as dt
import pandas as pd
import json
import folium
from streamlit_folium import folium_static
st.set_page_config(layout="wide")

st.title("Melanoma Detection App")
st.text("""
    *IT-University of Copenhagen, Bsc. in Data Science 
    2nd Semester First Year Project 
    Image Analysis Implementation*
    """)
