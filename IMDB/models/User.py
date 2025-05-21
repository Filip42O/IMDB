from models.Movie import Movie
from models.Review import Review
import bcrypt

class User:
    __global_id = 101

    #za kazdym razem jak przypisujemy id dodajmy je do seta
    taken_id = set()

    #remove user by id
    #nazwa klasy w cudzyslowach forward reference :)
    def remove_by_id_from_list(user_list: list['User'], id: int) -> list['User']:
        #returns true if removed, false if not
        for i in range(len(user_list)):
            if id == user_list[i].id:
                user_list.pop(i)
                return True
        return False

    #sortuje liste po id rosnaco
    def sort_user_list_by_id(user_list: list['User']) -> list['User']:
        return sorted(user_list, key=lambda user: user.id)

    def clear_data():
        User.taken_id.clear()
        User.__global_id = 101

    def __init__(self):
        self.id = User.__global_id
        User.taken_id.add(self.id)
        User.__global_id += 1
        self.username = "<No_Username>"
        self.watched_list = list()
        self.review_list = list()
        _password = "<DEFAULT>"




    #ta metoda upewnia sie ze z naturalnych przyczyn id nie bedzie takie samo jak usera ktorego wczytalismy
    def overrideID(self, new_id: int) -> None:
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

    def setusername(self, new_username: str) -> None:
        self.username = new_username.lower()

    def setpassword(self, new_password: str) -> None:
        self._password = bcrypt.hashpw(new_password.encode("utf-8"), bcrypt.gensalt()).decode('utf-8')

    def setpasswordNoHash(self, new_password: str) -> None:
        self._password = new_password

    def getpassword(self) -> str:
        return self._password

    def checkpassword(self, to_be_checked_pass: str) -> bool:
        #jezeli haslo nie bylo zinicjalizowane
        if self._password == "<DEFAULT>":
            print(f"Password for user:{self.id} nie jest zinicjalizowane")
            #self.setpassword(str(input("Prosze podać swoje hasło: ")))
            self.setpassword(str(to_be_checked_pass))
            return True  #manualnie zwracamy bo skoro podal haslo no to git
        return bcrypt.checkpw(to_be_checked_pass.encode("utf-8"), self._password.encode("utf-8"))



    #MOVIES
    def addwatched(self, movie: Movie) -> None:
        self.watched_list.append(movie)

    def removewatched(self, movie: Movie) -> None:
        self.watched_list.remove(movie)

    def clonewatched(self, Movies_list: list[Movie]) -> None:
        for mov in Movies_list:
            self.addwatched(mov)

    #REVIEWS
    def addreview(self, Review) -> None:
        self.review_list.append(Review)

    def removereview(self, input_movie: Movie) -> None:
        for review in self.review_list:
            if review.movie == input_movie:
                self.review_list.remove(review)
            else:
                raise Exception("Review for that movie doesnt exist!")

    def print_reviews(self) -> None:
        for review in self.review_list:
            print(review)

    def inputreviewwalkthrough(self, input_film: Movie) -> Review:
        print(f"Dodajesz recenzje do filmu: {input_film.Title}")
        rating: float = float(input(f"Podaj ocene w skali 0 - 10:"))

        while rating < 0 or rating > 10:
            print(f"Podano złą ocene!")
            rating = float(input(f"Podaj ocene w skali 0 - 10:"))

        description: str = str(input(f"Podaj opis swojej recenzji\n"))

        return Review(input_film, rating, description)

    #DRUKOWANIE USERA
    def __str__(self) -> str:
        return f"[{self.id}]: {self.username}"
