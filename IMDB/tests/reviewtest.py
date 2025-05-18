from storage.File_Handler import File_Handler
from models.User import User
from models.Review import Review
from models.Movie import Movie

#z pliku pobieramy usera
File_Handler.loaduserfromfile("./single_user")
users = File_Handler.user_list
userek: User = users[0]  #giga brain patent z type hintingiem

#tworzyny filmy
File_Handler.loadmoviesfromfile("../movies")
film1 = File_Handler.movie_list[0]
film2 = File_Handler.movie_list[1]

#testowanie czy dziala
# for mov in File_Handler.movie_list:
#     print(mov)

#dodajemy filmy


userek.clonewatched(File_Handler.movie_list)

# DLA TESTU DAJEMU JUZ FILMOWI RECENZJE
userek.addreview(Review(userek.watched_list[0],9.9,"super film polecam"))

#takiego formatowania mozna uzyc potem w interfejsie
print(f"Oto lista filmów które obejrzałeś ({len(userek.watched_list)}):")
for iter in range(len(userek.watched_list)):
    print(f"{iter + 1}->[{userek.watched_list[iter]}]")

dec = int(input(f"Wybierz numer filmu do którego chcesz dodać recenzje:")) - 1

if any(review.movie == userek.watched_list[dec] for review in userek.review_list):
    print(f"Zrecenzowałeś już film! Nadpisywanie recenzji w toku")
    userek.removereview(userek.watched_list[dec])
    userek.addreview(userek.inputreviewwalkthrough(userek.watched_list[dec]))
else:
    userek.addreview(userek.inputreviewwalkthrough(userek.watched_list[dec]))

userek.print_reviews()
