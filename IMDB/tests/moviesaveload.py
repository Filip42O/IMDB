from models.Category import Category
from storage.File_Handler import File_Handler
from models.Movie import Movie

# movie1 = Movie("The Shawshank Redemption", 142, 1994, "Frank Darabont")
# movie1.addcategory(Category.Drama)
#
# movie2 = Movie("Pulp Fiction", 154, 1994, "Quentin Tarantino")
# movie2.addcategory(Category.Drama)
#
# movie3 = Movie("Schindler's List", 195, 1993, "Steven Spielberg")
# movie3.addcategory(Category.War)
#
# movie4 = Movie("Interstellar", 169, 2014, "Christopher Nolan")
# movie4.addcategory(Category.Science_Fiction)
# movie4.addcategory(Category.Drama)
# movie4.addcategory(Category.Romance)
#
#
# movies = [movie1, movie2, movie3, movie4]

# File_Handler.save_movies_to_file("./movies_test",movies)



File_Handler.loadmoviesfromfile("./movies_test")


for mov in File_Handler.movie_list:
    print(mov)


