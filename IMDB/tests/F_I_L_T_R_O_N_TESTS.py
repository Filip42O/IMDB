from models.Category import Category
from models.F_I_L_T_R_O_N import F_I_L_T_R_O_N
from storage.File_Handler import File_Handler
from models.Movie import Movie

movie1 = Movie("The Shawshank Redemption", 142, 1994, "Frank Darabont")
movie1.addcategory(Category.Drama)

movie2 = Movie("Pulp Fiction", 154, 1994, "Quentin Tarantino")
movie2.addcategory(Category.Action)

movie3 = Movie("Schindler's List", 195, 1993, "Steven Spielberg")
movie3.addcategory(Category.War)

movie4 = Movie("The Interstellar", 169, 2014, "Christopher Nolan")
movie4.addcategory(Category.Science_Fiction)
movie4.addcategory(Category.Drama)
movie4.addcategory(Category.Romance)

movies = [movie1, movie2, movie3, movie4]

filtron = F_I_L_T_R_O_N(movies)

filtron.filter_by_year(1994, 2015)

# filtron.filter_by_length(150, 170)

# filtron.filter_by_director("Quentin Tarantino,Frank Darabont")

# filtron.filter_by_category("Drama,Action")
#
# for res in filtron.search("THE"):
#     print(res)

for result in filtron.result:
    print(result)