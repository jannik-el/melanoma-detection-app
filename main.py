from tracemalloc import start
from numpy import take
import streamlit as st
import datetime as dt
import pandas as pd
import json
import folium
from streamlit_folium import folium_static
import time
st.set_page_config(layout="wide")

##### HEADER #####

st.title("Melanoma Detection App")
st.subheader("First Year Project, Image Analysis")
st.caption("*IT-University of Copenhagen, Bsc. in Data Science*")
st.caption("By Juraj Septak, Gusts Gustav, Franek Liszka, Mirka and Jannik Elsäßer")

sidebar_options = ("Start Page", "Algorithm Description", "Results of the example image dataset", "Take your own picture and test", "Test bulk images")

def start_page():
    st.sidebar.write("---------------------")
    st.sidebar.success("Start Page showing on the right:")
    
    st.text("""
    This interactive app is designed as a representation of our groups submission
    for the First Year Project 2, detecting melanoma on skin using image 
    analysis algorithms.  

    On the left hand side you can choose different options from the sidebar.
    These include a complete breakdown of our algorithm, a example using images provided
    in the image example data set, and also an app with which you can take a 
    picture yourself and immediately test it.  
    """)

def alg_descrip_page():
    st.sidebar.write("---------------------")
    st.sidebar.success("Page showing on the right:")

def example_results_page():
    st.sidebar.write("---------------------")
    st.sidebar.success("Page showing on the right:")

    return

def take_pic_page():
    st.sidebar.write("---------------------")
    st.sidebar.success("Page showing on the right:")
    
    return

def test_bulk_img():
    st.sidebar.write("---------------------")
    st.sidebar.success("Page showing on the right:")

    return

def main():

    st.sidebar.title("Explore the following:")
    st.sidebar.write("---------------------")
    app_mode = st.sidebar.selectbox("Please select from the following:", sidebar_options)

    if app_mode == "Start Page":
        start_page()

    elif app_mode == "Algorithm Description":
        alg_descrip_page()

    elif app_mode == sidebar_options[2]:
        example_results_page()

    elif app_mode == sidebar_options[3]:
        take_pic_page()

    elif app_mode == sidebar_options[4]:
        test_bulk_img()


main()