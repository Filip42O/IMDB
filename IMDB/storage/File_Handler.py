from models.Category import Category
from models.User import User
from models.Review import Review
from models.Movie import Movie

class File_Handler:
    user_list = list()
    movie_list = list()
    review_list = list()
    def __init__(self):
        pass

    def loaduserfromfile(file_name : str) -> list[User]:
        result = list()
        try:
            with open(file_name,'r') as file:
                for line in file:
                    line = line.strip() #czyscimy ze new line
                    elems = line.split(sep=':')
                    #elems ['101', 'maciekKox', 'hash', filmyid]
                    user = User()
                    user.overrideID(int(elems[0]))
                    user.setusername(elems[1].lower())
                    user.setpasswordNoHash(elems[2])

                    filmy_id_list = elems[3].split(',')
                    #print(filmy_id_list)
                    if len(filmy_id_list) != 0:
                        for mov_id in filmy_id_list:
                            if mov_id.isdigit(): #naprawa tego ze split robi puste pliki
                                #szukamy w filmach filmu o id
                                # print(File_Handler.movie_list[0])
                                movie = next((movie for movie in File_Handler.movie_list if movie.id == int(mov_id)),None)
                                if movie is not None:
                                    user.addwatched(movie)
                    File_Handler.user_list.append(user)
                    result.append(user)
                return result
        except FileNotFoundError:
            raise Exception(f"File Not Found -> {file_name}")

    def saveuserstofile(filename : str , users_list : list[User]) -> None:
        try:
            file = open(filename,'w')

            for user in users_list:
                watched : list[str] = list()
                watched_ready = ""
                for mov in user.watched_list:
                    watched.append(mov.id)
                for string in watched:
                    watched_ready += str(string)
                    watched_ready += ","
                watched_ready = watched_ready.rstrip(",") #zeby nie bylo na koncu :)
                file.write(f"{user.id}:{user.username}:{user.getpassword()}:{watched_ready}\n")
                file.flush()
                #file.close()
        except IOError as ioerror:
            print(f"Błąd podczas uruchamiania metody zapisu do pliku: {ioerror}")

    def loadmoviesfromfile(file_name : str) -> None:
        try:
            with open(file_name,'r') as file:
                for line in file:
                    line = line.strip() #czyscimy ze new line
                    elems = line.split(sep='::')
                    #404:The Godfather:175:1972:Francis Ford Coppola:Crime,Drama
                    mov = Movie(elems[1],elems[2],elems[3],elems[4])

                    categories = elems[5].split(sep=',')
                    #print(categories)
                    for category in categories:
                        mov.addcategory(Category[category])
                    mov.overrideID(int(elems[0]))
                    File_Handler.movie_list.append(mov)
        except FileNotFoundError:
            raise Exception(f"Movies file Not Found -> {file_name}")

    def save_movies_to_file(filename : str , movies_list : list[Movie]) -> None:
        # 401:The Shawshank Redemption, 142, 1994, Frank Darabont
        try:
            file = open(filename,'w')
            for movie in movies_list:
                file.write(f"{movie.id}::{movie.Title}::{movie.Length}::{movie.Year}::{movie.Director}::{movie.getCategories()}\n")
                file.flush()
                #file.close()
        except IOError as ioerror:
            print(f"Błąd podczas uruchamiania metody zapisu do pliku: {ioerror}")

    def savereviewstofile(filename : str , review_list : list[Review]) -> None:
        # [id_review:id_movie:ocena:desc]
        try:
            file = open(filename,'w')
            for review in review_list:
                file.write(f"{review.id}:{review.movie.id}:{review.rating}:{review.description}\n")
                file.flush()
        except IOError as ioerror:
            print(f"Błąd podczas uruchamiania metody zapisu do pliku: {ioerror}")

    def load_reviews_from_file(file_name : str) -> None:
        if len(File_Handler.movie_list) <=0:
            raise Exception("No movies present! Load movies first")
        if len(File_Handler.user_list) <=0:
            raise Exception("No users present! Load users first")
        try:
            with open(file_name,'r') as file:
                for line in file:
                    line = line.strip() #czyscimy ze new line
                    elems = line.split(sep=':')
                    #elems [id_review:id_movie:id_user:ocena:desc]
                    mov = next((movie for movie in File_Handler.movie_list if movie.id == int(elems[1])),None)
                    usr = next((user for user in File_Handler.user_list if user.id == int(elems[2])), None)
                    #brak znalezionego filmu!
                    if mov is None:
                        raise Exception(f"Movie ID:{elems[1]} not found!")
                    if usr is None:
                        raise Exception(f"User ID:{elems[2]} not found!")
                    rev = Review(mov,float(elems[3]),elems[4])
                    rev.overrideID(int(elems[0]))
                    #mozliwe ze tu dajemu kopii a nie oryginalowi
                    usr.addreview(rev)
                    File_Handler.review_list.append(rev)
        except FileNotFoundError:
            raise Exception(f"Review file Not Found -> {file_name}")