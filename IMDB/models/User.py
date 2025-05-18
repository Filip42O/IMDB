from models.Movie import Movie
from models.Review import Review
import models.bcrypt

class User:
    __global_id = 101
    watched_list = list()
    review_list = list()
    #za kazdym razem jak przypisujemy id dodajmy je do seta
    taken_id = set()

    def __init__(self):
        self.id = User.__global_id
        User.taken_id.add(self.id)
        User.__global_id += 1
        self.username = "<No_Username>"

    _password = "<DEFAULT>"

    #ta metoda upewnia sie ze z naturalnych przyczyn id nie bedzie takie samo jak usera ktorego wczytalismy
    def overrideID(self, new_id: int):
        # User.__global_id = new_id + 1
        User.taken_id.remove(self.id)


        if len(User.taken_id) > 0:
            User.__global_id = max(User.taken_id) + 1

        #sprawdzamy czy id jest zajete
        if new_id in User.taken_id:
            raise Exception(f"Id {new_id} jest juz zajete!")
        else:
            self.id = new_id
            User.taken_id.add(self.id)
            User.__global_id = max(User.taken_id) + 1

    def setusername(self, new_username: str):
        self.username = new_username.lower()

    def setpassword(self, new_password: str):
        self._password = bcrypt.hashpw(new_password.encode("utf-8"), bcrypt.gensalt()).decode('utf-8')

    def setpasswordNoHash(self, new_password: str):
        self._password = new_password

    def getpassword(self):
        return self._password

    def checkpassword(self, to_be_checked_pass: str):
        #jezeli haslo nie bylo zinicjalizowane
        if self._password == "<DEFAULT>":
            print(f"Password for user:{self.id} nie jest zinicjalizowane")
            self.setpassword(str(input("Prosze podać swoje hasło: ")))
            return True  #manualnie zwracamy bo skoro podal haslo no to git
        return bcrypt.checkpw(to_be_checked_pass.encode("utf-8"), self._password.encode("utf-8"))

    #MOVIES
    def addwatched(self, movie: Movie):
        self.watched_list.append(movie)

    def removewatched(self, movie: Movie):
        self.watched_list.remove(movie)

    def clonewatched(self, Movies_list: list[Movie]):
        for mov in Movies_list:
            self.addwatched(mov)

    #REVIEWS
    def addreview(self, Review):
        self.review_list.append(Review)

    def removereview(self, input_movie : Movie):
        for review in self.review_list:
            if review.movie == input_movie:
                self.review_list.remove(review)
            else:
                raise Exception("Review for that movie doesnt exist!")


    def print_reviews(self):
        for review in self.review_list:
            print(review)

    def inputreviewwalkthrough(self,input_film : Movie):
        print(f"Dodajesz recenzje do filmu: {input_film.Title}")
        rating : float = float(input(f"Podaj ocene w skali 0 - 10:"))

        while rating < 0 or rating > 10:
            print(f"Podano złą ocene!")
            rating = float(input(f"Podaj ocene w skali 0 - 10:"))

        description : str = str(input(f"Podaj opis swojej recenzji\n"))

        return Review(input_film, rating, description)


    #DRUKOWANIE USERA
    def __str__(self):
        return f"[{self.id}]: {self.username}"
