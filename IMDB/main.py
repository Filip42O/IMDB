import time

from models.User import User
from models.Movie import Movie
from models.Review import Review
from storage.File_Handler import File_Handler
import streamlit as st

@st.cache_resource
def fetch_data(file_name:str):
    result = list()
    file = open(file_name,'r')
    for line in file:
        line = line.strip() #czyscimy ze new line
        elems = line.split(sep=':')
        #elems ['101', 'maciekKox', 'hash']
        user = User()
        user.overrideID(int(elems[0]))
        user.setusername(elems[1].lower())
        user.setpasswordNoHash(elems[2])
        File_Handler.user_list.append(user)
        result.append(user)
    return result




data = fetch_data("./users_saved")

for user in data:
    st.text(user)

