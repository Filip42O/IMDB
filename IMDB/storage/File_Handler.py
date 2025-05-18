from models.User import User
from models.Review import Review
from models.Movie import Movie

class File_Handler:
    user_list = list()
    movie_list = list()
    review_list = list()
    def __init__(self):
        pass

    def loaduserfromfile(file_name : str):
        try:
            with open(file_name,'r') as file:
                for line in file:
                    line = line.strip() #czyscimy ze new line
                    elems = line.split(sep=':')
                    #elems ['101', 'maciekKox', 'hash']
                    user = User()
                    user.overrideID(int(elems[0]))
                    user.setusername(elems[1].lower())
                    user.setpasswordNoHash(elems[2])
                    File_Handler.user_list.append(user)
        except FileNotFoundError:
            raise Exception(f"File Not Found -> {file_name}")

    def saveuserstofile(filename : str , users_list : list[User]):
        try:
            file = open(filename,'w')
            for user in users_list:
                file.write(f"{user.id}:{user.username}:{user.getpassword()}\n")
        except IOError as ioerror:
            print(f"Błąd podczas uruchamiania metody zapisu do pliku: {ioerror}")

    def loadmoviesfromfile(file_name : str):
        try:
            with open(file_name,'r') as file:
                for line in file:
                    line = line.strip() #czyscimy ze new line
                    elems = line.split(sep=':')
                    #elems [401:The Shawshank Redemption, 142, 1994, Frank Darabont]
                    # ['Science_Fiction', 'Drama', 'Romance']
                    mov = Movie(elems[1],elems[2],elems[3],elems[4])
                    mov.overrideID(int(elems[0]))
                    File_Handler.movie_list.append(mov)
        except FileNotFoundError:
            raise Exception(f"Movies file Not Found -> {file_name}")

    def save_movies_to_file(filename : str , movies_list : list[Movie]):
        # 401:The Shawshank Redemption, 142, 1994, Frank Darabont
        try:
            file = open(filename,'w')
            for movie in movies_list:
                file.write(f"{movie.id}:{movie.Title}:{movie.Length}:{movie.Year}:{movie.Director}:{movie.getCategories()}\n")
        except IOError as ioerror:
            print(f"Błąd podczas uruchamiania metody zapisu do pliku: {ioerror}")

    def savereviewstofile(filename : str , review_list : list[Review]):
        # [id_review:id_movie:ocena:desc]
        try:
            file = open(filename,'w')
            for review in review_list:
                file.write(f"{review.id}:{review.movie.id}:{review.rating}:{review.description}\n")
        except IOError as ioerror:
            print(f"Błąd podczas uruchamiania metody zapisu do pliku: {ioerror}")

    def load_reviews_from_file(file_name : str):
        if len(File_Handler.movie_list) <=0:
            raise Exception("No movies present! Load movies first")
        try:
            with open(file_name,'r') as file:
                for line in file:
                    line = line.strip() #czyscimy ze new line
                    elems = line.split(sep=':')
                    #elems [id_review:id_movie:ocena:desc]
                    mov = next((movie for movie in File_Handler.movie_list if movie.id == int(elems[1])),None)
                    #brak znalezionego filmu!
                    if mov is None:
                        raise Exception(f"Movie ID:{elems[1]} not found!")
                    rev = Review(mov,float(elems[2]),elems[3])
                    rev.overrideID(int(elems[0]))
                    File_Handler.review_list.append(rev)
        except FileNotFoundError:
            raise Exception(f"Review file Not Found -> {file_name}")