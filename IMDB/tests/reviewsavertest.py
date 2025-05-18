from models.Movie import Movie
from models.Review import Review
from models.User import User
from storage.File_Handler import File_Handler

def test1():
    userek = User()
    userek.setusername("userek")
    userek.setpassword("haselko")

    movie = Movie("The Shawshank Redemption", 142, 1994, "Frank Darabont")


    userek.addwatched(movie)

    # DLA TESTU DAJEMU JUZ FILMOWI RECENZJE
    rev1 = Review(movie,9.9,"super film polecam")
    userek.addreview(rev1)

    userek.print_reviews()

    File_Handler.savereviewstofile("../storage/reviewmark1",[rev1])

def test2():
    File_Handler.loaduserfromfile("./single_user")
    File_Handler.loadmoviesfromfile("../movies")
    File_Handler.load_reviews_from_file("../storage/reviewmark1")
    return File_Handler.review_list

varek = test2()
File_Handler.user_list[0].print_reviews()
print(File_Handler.movie_list[0])
print(File_Handler.review_list[0])