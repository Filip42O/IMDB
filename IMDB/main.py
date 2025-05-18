import time

from models.User import User
from models.Movie import Movie
from models.Review import Review
from storage.File_Handler import File_Handler
import streamlit as st

@st.cache_data(ttl=15)
def fetch_data():
    File_Handler.loaduserfromfile("./users_saved")
    time.sleep(2)
    return File_Handler.user_list


data = fetch_data()

for user in data:
    print(user)

