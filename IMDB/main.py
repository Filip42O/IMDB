import time

from models.User import User
from models.Movie import Movie
from models.Review import Review
from storage.File_Handler import File_Handler
import streamlit as st
import os



#/mount/src/imdb/IMDB

st.header(":orange[IM]:grey[DB]",divider="orange")
st.header("Imperium mitów, dezinformacji i bredni",divider="grey")

@st.cache_data
def loadusers():
    File_Handler.loaduserfromfile("/mount/src/imdb/IMDB/users_saved")
    return File_Handler.user_list


data = loadusers()

for user in data:
    st.text(user)
