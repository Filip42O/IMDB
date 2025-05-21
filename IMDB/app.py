from models.User import User
from models.Movie import Movie
from models.Review import Review
from storage.File_Handler import File_Handler
import streamlit as st

#/mount/src/imdb/IMDB

st.set_page_config(
    page_title="IMDB",
    page_icon=":movie_camera:",
)



def loadusers():
    #File_Handler.loaduserfromfile("/mount/src/imdb/IMDB/users_saved")
    User.clear_data()
    File_Handler.user_list.clear()
    File_Handler.loaduserfromfile("./users_saved")
    print("loading users!")
    return File_Handler.user_list


def save_users_if_needed():
    global users
    if "users_need_save" in st.session_state and st.session_state.users_need_save:
        try:
            File_Handler.saveuserstofile("./users_saved", users)
            print("Zapisano dane użytkowników")
            st.session_state.users_need_save = False
        except Exception as e:
            print(f"Błąd podczas zapisywania danych: {e}")
            st.error("Wystąpił błąd podczas zapisywania danych")
def handle_username_submit():
    username = st.session_state.username_input.lower()
    user = next((user for user in users if user.username == username), None)

    if user is not None:
        st.session_state.user = user
        st.session_state.show_password = True
        st.session_state.username_success = f"Znaleziono użytkownika {username}"
    else:
        st.session_state.username_error = f"Brak użytkownika {username} w bazie danych!"
        st.session_state.show_password = False

def handle_password_submit():
    global users
    if st.session_state.user.getpassword() == "<DEFAULT>":
        #new password init
        st.session_state.user.setpassword(st.session_state.password_input)
        if not User.remove_by_id_from_list(users, st.session_state.user.id):
            raise Exception("Użytkownik nagle zniknął z listy ???")
        users.append(st.session_state.user)
        users = User.sort_user_list_by_id(users)

        #forcujemy dane do zapisu
        st.session_state.users_need_save = True

        #instant zapisanie po update hasla
        try:
            File_Handler.saveuserstofile("./users_saved", users)
            print(f"Zapisano hasło dla użytkownika {st.session_state.user.username}")
            st.session_state.users_need_save = False
        except Exception as e:
            st.error("Coś się wysypało w zapisywaniu do pliku podczas aktualizacji hasła!")
            print(f"Błąd zapisu w aktualizacji hasła: {e}")

        User.clear_data()
        users = loadusers()
        st.session_state.user = next(u for u in users if u.id == st.session_state.user.id)
        print(f"tu sprawdzam co sie dzieje z passwordem {st.session_state.user.getpassword()}")


        #test1
        print(f"przed update {st.session_state.user.getpassword()}")
        #refresh naszego user
        st.session_state.user = next(u for u in users if u.id == st.session_state.user.id)
        #test2
        print(f"po update {st.session_state.user.getpassword()}")
        st.session_state.logged = True
        st.session_state.password_success = "Pomyślnie ustawiono nowe hasło!"
    else:
        if st.session_state.user.checkpassword(st.session_state.password_input):
            st.session_state.logged = True
            st.session_state.password_success = "Zalogowano pomyślnie!"
        else:
            st.session_state.password_error = "Nieprawidłowe hasło!"

def logout():
    #reset wszystkiego po wylogowaniu
    st.session_state.logged = False
    st.session_state.user = None
    st.session_state.show_password = False
    users.clear()
    if "username_success" in st.session_state:
        del st.session_state.username_success
    if "username_error" in st.session_state:
        del st.session_state.username_error
    if "password_success" in st.session_state:
        del st.session_state.password_success
    if "password_error" in st.session_state:
        del st.session_state.password_error

#init zmiennych session state
if "logged" not in st.session_state:
    st.session_state.logged = False
    st.session_state.user = None
if "show_password" not in st.session_state:
    st.session_state.show_password = False
if "users_need_save" not in st.session_state:
    st.session_state.users_need_save = False


users = loadusers()

#naglowki
st.header(":orange[IM]:grey[DB]", divider="orange")
st.header("Imperium mitów, dezinformacji i bredni", divider="grey")


#program
if not st.session_state.logged:
    st.title("Zaloguj się do systemu")

    #username form
    with st.form(key="username_form"):
        st.text_input("Podaj nazwę użytkownika", key="username_input")
        submit_username = st.form_submit_button("Dalej", on_click=handle_username_submit)

    #komunikaty
    if "username_success" in st.session_state:
        st.success(st.session_state.username_success)
    if "username_error" in st.session_state:
        st.error(st.session_state.username_error)

    #password form
    if st.session_state.show_password:
        with st.form(key="password_form"):

            if st.session_state.user.getpassword() == "<DEFAULT>":
                st.info("Twoje konto nie ma założonego hasła! Ustaw nowe hasło.")

            st.text_input("Podaj hasło", type="password", key="password_input")
            submit_password = st.form_submit_button(
                "Zaloguj się" if st.session_state.user.getpassword() != "<DEFAULT>" else "Ustaw hasło",
                on_click=handle_password_submit
            )

        #komunikaty hasla
        if "password_success" in st.session_state:
            st.success(st.session_state.password_success)
        if "password_error" in st.session_state:
            st.error(st.session_state.password_error)
else:
    #interfejs po logowaniu
    st.title(f"Witaj, {st.session_state.user.username}!")

    # Tu możesz dodać zawartość panelu użytkownika
    st.write("Jesteś zalogowany. Tutaj będzie panel zarządzania filmami i recenzjami.")

    # Przykładowe zakładki dla zalogowanego użytkownika
    tabs = st.tabs(["Profil", "Filmy", "Recenzje"])

    with tabs[0]:
        st.header("Twój profil")
        st.write(f"ID użytkownika: {st.session_state.user.id}")
        st.write(f"Nazwa użytkownika: {st.session_state.user.username}")


    with tabs[1]:
        st.header("Zarządzanie filmami")
        st.write("Tu będzie lista filmów.")


    with tabs[2]:
        st.header("Twoje recenzje")
        st.write("Tu będą twoje recenzje.")

    #logout button
    if st.button("Wyloguj się", on_click=logout):
        pass

save_users_if_needed()
