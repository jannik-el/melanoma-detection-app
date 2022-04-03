import streamlit as st
import datetime as dt
import pandas as pd
import json
import time
from PIL import Image

st.set_page_config(layout="wide")

##### HEADER #####

st.title("Melanoma Detection App")
st.subheader("First Year Project, Image Analysis")
st.caption("*IT-University of Copenhagen, Bsc. in Data Science*")
st.caption("By Juraj Septak, Gusts Gustav, Franek Liszka, Mirka and Jannik Elsäßer")
st.write("------------------------------------------")

sidebar_options = ("Start Page", "Algorithm Description", "Results of the example image dataset", "Take your own picture and test", "Test bulk images")

##### PAGE CODE ##########
def start_page():
    st.sidebar.write("---------------------")
    st.sidebar.success("Start Page showing on the right:")
    
    col1, col2 = st.columns(2)

    with col1:
        st.write("""
        This interactive app is designed as a representation of our groups submission
        for the First Year Project 2, detecting the presence of melanoma on skin using image 
        analysis algorithms.  

        On the left hand side you can choose different options from the sidebar.
        These include a complete breakdown of our algorithm, a example using images provided
        in the image example dataset, and also an app with which you can take a 
        picture yourself and immediately test it.  
        """)

    with col2:
        melanoma_image = Image.open(r'./styles/melanoma.jpg')
        st.image(melanoma_image, caption='Melanoma on a patients skin, https://en.wikipedia.org/wiki/Melanoma#/media/File:Melanoma.jpg')

    return

def alg_descrip_page():
    st.sidebar.write("---------------------")
    st.sidebar.success("Page showing on the right:")

    st.write("This is where a breakdown of the algorithm, using an image from the dataset as an example, goes:")

def example_results_page():
    st.sidebar.write("---------------------")
    st.sidebar.success("Page showing on the right:")

    st.write("Not quite sure what we should put here, maybe results from our analysis, idk we'll figure it out.")

    return

def take_pic_page():
    st.sidebar.write("---------------------")
    st.sidebar.success("Page showing on the right:")

    take_picture = st.camera_input("Take a picture to test it for melanoma:")

    if take_picture:
        st.image(take_picture)
    
    st.write("Currently it just shows the picture, but here we can build the algorithm in and immediately show the results which would be really cool")
    return

def test_bulk_img():
    st.sidebar.write("---------------------")
    st.sidebar.success("Page showing on the right:")

    st.write("""
    The idea is that they can upload a folder with a bunch of images and test them on this page.
    This might be a bit difficult to implement. 
    """)
    return

###### MAIN FUNCTION #######
# the st.cache suppress warning unlocks better performance, which is best for our algorithm
# @st.cache(suppress_st_warning=True)
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

if __name__ == "__main__":
    main()
