import time

from models.User import User
from models.Movie import Movie
from models.Review import Review
from storage.File_Handler import File_Handler
import streamlit as st

@st.cache_data(show_spinner=False)
def load_users(path):
    File_Handler.loaduserfromfile(path)
    time.sleep(2)
    return File_Handler.user_list


# Inicjalizacja danych w sesji – tylko raz
if "data_loaded" not in st.session_state:
    with st.spinner("Ładowanie danych z bazy..."):
        st.session_state.users = load_users("./users_saved")
        st.session_state.data_loaded = True
    st.rerun()  # restart, aby zacząć od GUI już z danymi

# Gdy dane już załadowane – wyświetl GUI
if st.session_state.data_loaded:
    st.success("Dane załadowane!")
    selected_user = st.selectbox("Wybierz użytkownika", st.session_state.users)
    for usr in st.session_state.users:
        st.text(usr)
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

