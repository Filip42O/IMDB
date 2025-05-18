import time

from models.User import User
from models.Movie import Movie
from models.Review import Review
from storage.File_Handler import File_Handler
import streamlit as st

@st.cache_data(show_spinner=False)
def load_users(path):
    File_Handler.loaduserfromfile(path)
    return File_Handler.user_list


#ladowanie z plikow

# Tytuł aplikacji
st.title("Witaj w Streamlit!")

# Nagłówek
st.header("Przykładowy nagłówek")

# Podtytuł
st.subheader("Przykładowy podtytuł")

# Prosty tekst
st.write("To jest przykładowy tekst wyświetlany za pomocą st.write()")

# Czcionka monospace z st.text
st.text("To jest tekst monospace z użyciem st.text()")

# Tekst sformatowany Markdown
st.markdown("**Pogrubiony tekst** oraz *kursywa* za pomocą st.markdown()")

# Aby uruchomić tę aplikację, zapisz ten plik jako app.py i w terminalu wykonaj:
# streamlit run app.py
with st.spinner("Wczytuję użytkowników z pliku…"):
    users = load_users("./users_saved")


for usr in File_Handler.user_list:
    st.text(usr)