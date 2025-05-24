import os.path

from models.User import User
from models.Movie import Movie
from models.Review import Review
from storage.File_Handler import File_Handler
import streamlit as st

#/mount/src/imdb/IMDB

path_to_review_file = os.path.join(os.getcwd(),"reviews_saved")
#path_to_review_file = "/mount/src/imdb/IMDB/reviews_saved"

path_to_movies_file = os.path.join(os.getcwd(),"movies_saved")
#path_to_movies_file = "/mount/src/imdb/IMDB/movies_saved"

path_to_users_file = os.path.join(os.getcwd(),"users_saved")
#path_to_users_file = "/mount/src/imdb/IMDB/users_saved"

st.set_page_config(
    page_title="IMDB",
    page_icon=":movie_camera:",
)

def loadusers():
    User.clear_data()
    File_Handler.user_list.clear()
    File_Handler.loaduserfromfile(path_to_users_file)
    #File_Handler.loaduserfromfile("/mount/src/imdb/IMDB/users_saved")
    #print("Load users ran !")
    return File_Handler.user_list

def loadmovies():
    File_Handler.movie_list.clear()
    Movie.cleardata()
    File_Handler.loadmoviesfromfile(path_to_movies_file)
    #File_Handler.loaduserfromfile("/mount/src/imdb/IMDB/movies_saved")
    #print("loading movies!")
    return File_Handler.movie_list

def loadreviews():
    File_Handler.review_list.clear()
    File_Handler.load_reviews_from_file(path_to_review_file)
    #File_Handler.loadreviewfromfile("/mount/src/imdb/IMDB/reviews_saved")
    #print("Loaded reviews!")
    return File_Handler.review_list

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
    user_looker = next((u for u in users if u.username == username), None)

    if user_looker is not None:
        st.session_state.user = user_looker
        st.session_state.show_password = True
        st.session_state.username_success = f"Znaleziono użytkownika {username}"
    else:
        st.session_state.username_error = f"Brak użytkownika {username} w bazie danych!"
        st.session_state.show_password = False


def handle_password_submit():
    global users
    #user = st.session_state.user
    if st.session_state.user.getpassword() == "<DEFAULT>":
        print(f"przed update{st.session_state.user.getpassword()}")
        st.session_state.user.setpassword(st.session_state.password_input)
        print(f"po update{st.session_state.user.getpassword()}")
        if not User.remove_by_id_from_list(users, st.session_state.user.id):
            raise Exception("Użytkownik nagle zniknął z listy ???")

        users.append(st.session_state.user)
        users = User.sort_user_list_by_id(users)


        st.session_state.users_need_save = True

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
    st.session_state.user : User = None
if "show_password" not in st.session_state:
    st.session_state.show_password = False
if "users_need_save" not in st.session_state:
    st.session_state.users_need_save = False

movies = loadmovies()
users = loadusers()
reviews = loadreviews()


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
    st.title(f"Witaj, :blue[{st.session_state.user.username}]!")

    #init tabelek
    tabs = st.tabs(["Profil", "Filmy", "Recenzje"])

    with tabs[0]:
        st.header("Twój profil")
        st.write(f"ID użytkownika: {st.session_state.user.id}")
        st.write(f"Nazwa użytkownika: {st.session_state.user.username}")
        st.write(f"Ilość obejrzanych filmów: {len(st.session_state.user.watched_list)}")
        st.write(f"Ilość dodanych recenzji: {len(st.session_state.user.review_list)}")
        st.image("./avatar.png",caption="Sigma sigma boi")

    with tabs[1]:
        st.header("Zarządzanie filmami")
        user: User = st.session_state.user

        #dodawanie filmow
        if st.button("Dodaj nowy film"):
            st.session_state.show_add_movie = True


        if "show_add_movie" in st.session_state and st.session_state.show_add_movie is True:
            st.subheader("Wybierz film do dodania")
        
            #duplikuje nam filmy
            movie_titles = [movie.Title for movie in movies if not user.movie_in_user_by_id(movie.id)]

            selected_movie_title = st.selectbox("Wybierz film", options=movie_titles, key="movie_select")

            if st.button("Dodaj wybrany film"):
                selected_movie = next((movie for movie in movies if movie.Title == selected_movie_title), None)
                if selected_movie:
                    
                    
                    #saving again
                    User.remove_by_id_from_list(users, user.id)
                    user.watched_list.append(selected_movie)
                    users.append(user)
                    File_Handler.saveuserstofile(path_to_users_file, users)
                    st.session_state.show_add_movie = False
                    st.rerun()

        #wyswietlanie filmow
        if len(user.watched_list) == 0:
            st.text("Obecnie nie obejrzałeś żadnych filmów :(")
        else:
            for mov in user.watched_list:
                col1, col2, col3 = st.columns([3, 1, 3])
                with col1:
                    st.text(f"{mov.niceformat()}")
                #to dziala super
                with col2:
                    if st.button(f"Usuń",type="primary", key=f"usun {mov.id}"):
                        
                        if User.remove_by_id_from_list(users, user.id):
                            print(f"Usunięto użytkownika {user.username} z listy użytkowników")
                        else:
                            raise Exception(f"Nie można usunąć {user.username} w usuwaniu filmu! ")
                        
                        user.watched_list.remove(mov)
                        users.append(user)
                        
                        File_Handler.saveuserstofile("./users_saved", users)#insta save do pliku
                        st.rerun()
                with col3:
                    if st.button(f"Recenzuj", type="secondary", key=f"recenzja {mov.id}"):
                        st.session_state.show_review_form : Movie = mov

        #recenzja form
        if "show_review_form" in st.session_state and st.session_state.show_review_form is not None:
            movie_to_review : Movie = st.session_state.show_review_form
            st.subheader(f"Dodaj recenzję do filmu -> {movie_to_review.Title}")
            #rating = st.slider("Ocena", 0, 10.0, step=0.1, key="review_rating")
            rating = st.feedback(options="stars",key="review_rating")
            description = st.text_area("Opis recenzji", key="review_description")
            if st.button("Zapisz recenzję"):
                new_review = Review(movie=movie_to_review, rating=(rating+1)*2, description=description,user_id=user.id)
                user.review_list.append(new_review)
                reviews.append(new_review)
                #instant zapis do pliku
                User.remove_by_id_from_list(users, user.id)
                users.append(user)
                File_Handler.savereviewstofile(path_to_review_file, reviews)
                #koniec zapisu
                st.session_state.show_review_form = None
                st.rerun()

    with tabs[2]:
        st.header("Twoje recenzje")
        user_reviews = Review.get_reviews_by_user_id(user.id, reviews)    
        if len(user_reviews) == 0:
            st.text("Nie dodałeś jeszcze żadnych recenzji :(")
            pass
        
        
        
        for review in user_reviews:
            col1,col2 = st.columns([3,1])
            with col1:
                st.text(f"{review.movie.Title} - {review.rating}/10")
                st.text(f"{review.description}")
            with col2:
                if st.button("Usuń", key=f"delete_review {review.id}", type="primary"):
                    if Review.remove_by_id_from_list(reviews, review.id):
                        print(f"Usunięto recenzję {review.id} z listy recenzji")
                    else:
                        raise Exception(f"Nie można usunąć recenzji {review.id} w usuwaniu recenzji!")
                    File_Handler.savereviewstofile(path_to_review_file, reviews)
                    st.rerun()

    #logout button
    if st.button("Wyloguj się", on_click=logout):
        save_users_if_needed()
        pass

save_users_if_needed() #to jest jak apka sie konczy a na streamlicie sie nie konczy wiec dodajmy to wyzej
