from models.User import User
from models.Movie import Movie
from models.Review import Review
from storage.File_Handler import File_Handler

film_50twarzygreya = Movie("Fifty Shades of Grey", 125, 2015, "Sam Taylor-Johnson")
film_50twarzyciemniejszy = Movie("Fifty Shades Darker", 118, 2017, "James Foley")
film_50twarzywyzwolony = Movie("Fifty Shades Freed", 105, 2018, "James Foley")
film_365dni = Movie("365 Days", 114, 2020, "Barbara Białowąs")
film_after = Movie("After", 105, 2019, "Jenny Gage")
film_basicinstinct = Movie("Basic Instinct", 127, 1992, "Paul Verhoeven")
film_eyeswideshut = Movie("Eyes Wide Shut", 159, 1999, "Stanley Kubrick")
film_unfaithful = Movie("Unfaithful", 124, 2002, "Adrian Lyne")
film_fatalattraction = Movie("Fatal Attraction", 119, 1987, "Adrian Lyne")
film_thevoyeurs = Movie("The Voyeurs", 116, 2021, "Michael Mohan")

movies = [
    film_50twarzygreya,
    film_50twarzyciemniejszy,
    film_50twarzywyzwolony,
    film_365dni,
    film_after,
    film_basicinstinct,
    film_eyeswideshut,
    film_unfaithful,
    film_fatalattraction,
    film_thevoyeurs
]

maciek = User()
maciek.setusername("maciekKox")
maciek.setpassword("<NEWPASS>")

maks = User()
maks.setusername("maks_destrojer")

tomek = User()
tomek.setusername("tomeczekPL")

uzytkownicy = [tomek, maciek, maks]

# for movie in movies:
#     print(f"{movie.id} -> {movie.Title}: {movie.Lenght} minutes, {movie.Year} by {movie.Director}")

maciek.cloneliked(movies)
# print(len(maciek.liked_list))
# maciek.removeliked(film_after)
# print(len(maciek.liked_list))

maciek.addreview(Review(film_50twarzygreya, 9.9, "Super film! zabawa dla całej rodziny!!!"))
maciek.addreview(Review(film_50twarzyciemniejszy, 8, "zona mnie zostawila"))

#maciek.print_reviews()

File_Handler.saveuserstofile("../users_saved", uzytkownicy)
File_Handler.loaduserfromfile("../users_saved")

for userek in File_Handler.user_list:
    print(userek)
