import pandas as pd
import plotly.express as px
import streamlit as st
from streamlit_option_menu import option_menu
import mysql.connector as sql
import pymongo
from googleapiclient.discovery import build
from PIL import Image

# SETTING PAGE CONFIGURATIONS
icon = Image.open("youtubelogo.jpg") 
st.set_page_config(page_title= "Youtube Data Harvesting and Warehousing | By Sagar R Sankole",
                   page_icon= icon,
                   layout= "wide",
                   initial_sidebar_state= "expanded",
                   menu_items={'About': """# This app is created by *Sagar R Sankole!*"""}
                   
# CREATING OPTION MENU
with st.sidebar:
    selected = option_menu(None, ["Home","Extract & Transform","View"], 
                           icons=["house-door-fill","tools","card-text"],
                           default_index=0,
                           orientation="vertical",
                           styles={"nav-link": {"font-size": "30px", "text-align": "centre", "margin": "0px", 
                                                "--hover-color": "#33A5FF"},
                                   "icon": {"font-size": "30px"},
                                   "container" : {"max-width": "6000px"},
                                   "nav-link-selected": {"background-color": "#33A5FF"}})

# Bridging a connection with MongoDB Atlas and Creating a new database(youtube_data)
client = pymongo.MongoClient("localhost:27017")
db = client.Youtube_Data_Arun
# CONNECTING WITH MYSQL DATABASE
mydb = sql.connect(host="127.0.0.1",
                   user="root",
                   password="Arun@mysql9398",
                   database= "youtube",
                   port = "3306"
                  )
mycursor = mydb.cursor(buffered=True)
