import time

from models.User import User
from models.Movie import Movie
from models.Review import Review
from storage.File_Handler import File_Handler
import streamlit as st
import os



st.title(os.path.dirname(os.path.abspath(__file__)))

data = File_Handler.loaduserfromfile("/mount/src/imdb/IMDB/users_saved")

for user in data:
    st.text(user)

