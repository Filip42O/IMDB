from models.User import User
from models.Movie import Movie
from models.Review import Review
from storage.File_Handler import File_Handler
import streamlit as st
import os

#/mount/src/imdb/IMDB

st.set_page_config(
    page_title="IMDB",
    page_icon=":movie_camera:",
)
st.header(":orange[IM]:grey[DB]", divider="orange")
st.header("Imperium mitów, dezinformacji i bredni", divider="grey")

@st.cache_data
def loadusers():
    #File_Handler.loaduserfromfile("/mount/src/imdb/IMDB/users_saved")
    File_Handler.loaduserfromfile("./users_saved")
    return File_Handler.user_list


users : list[User] = loadusers()

if "page" not in st.session_state:
    st.session_state.page = 1
if "user" not in st.session_state:
    st.session_state.user : User = None

username_input = st.text_input("Username")
if st.session_state.page == 1:
    if username_input:
        st.session_state.user = next((user for user in users if user.username == username_input), None)
        if st.session_state.user is not None:
            print(st.session_state.user)
            st.success(f"Pomyślnie znaleziono usera o ID:{st.session_state.user.id}")
            st.session_state.page = 2
            st.rerun()
        else:
            st.error(f"Brak użytkownika {username_input} w bazie danych!")
            st.rerun()
elif st.session_state.page == 2:
    st.success(f"Pomyślnie znaleziono usera o ID:{st.session_state.user.id}")
    #haslo jest domyslne to trzeba je ustawic
    if st.session_state.user.getpassword() == "<DEFAULT>":
        st.text("Twoje konto nie ma założonego hasła!")
        input = st.text_input("Podaj nowe hasło",type="password")
        #jak poda haslo
        if input:
            print(f"po input {st.session_state.user}")
            User.remove_by_id_from_list(users,st.session_state.user.id)
            st.session_state.user.setpassword(input)
            st.success("Pomyślnie ustawiono hasło!")
            users.append(st.session_state.user)#tu dodaje ale to jest nie dobry pomysl
            users = User.sort_user_list_by_id(users)
            st.session_state.page = 3
    else:
        password_input = st.text_input("Password",type="password")
        #uzytkownik cos wpisal
        if password_input:
            if st.session_state.user.checkpassword(password_input):
                st.success("Podano prawidłowe hasło!")
                st.session_state.page = 3
            else:
                st.error("Hasło nieprawidłowe")

File_Handler.saveuserstofile("./users_saved",users)
print(f"saved users")
print(f"print last {users[0].checkpassword("turbo")}")

st.stop()