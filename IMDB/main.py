import time

from models.User import User
from models.Movie import Movie
from models.Review import Review
from storage.File_Handler import File_Handler
import streamlit as st
import os

#/mount/src/imdb/IMDB

st.header(":orange[IM]:grey[DB]", divider="orange")
st.header("Imperium mitów, dezinformacji i bredni", divider="grey")


@st.cache_data
def loadusers():
    File_Handler.loaduserfromfile("/mount/src/imdb/IMDB/users_saved")
    return File_Handler.user_list


users = loadusers()

title = st.text_input("Username")
if title:
    user_var: User = next((user for user in users if user.username == title), None)
    if user_var != None:
        st.success(f"Pomyślnie znaleziono usera o ID:{user_var.id}")
    else:
        st.error(f"Brak użytkownika {title} w bazie danych!")
