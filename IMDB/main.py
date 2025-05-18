import time

from models.User import User
from models.Movie import Movie
from models.Review import Review
from storage.File_Handler import File_Handler
import streamlit as st

@st.cache_data(ttl=15)
def fetch_data():
    return File_Handler.loaduserfromfile("./users_saved")


data = fetch_data()

for usr in data:
    st.text(usr)

