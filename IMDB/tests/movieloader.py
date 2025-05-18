from models.Movie import Movie
from storage.File_Handler import File_Handler


File_Handler.loadmoviesfromfile("../movies")

for mov in File_Handler.movie_list:
    print(mov)

super = Movie("sigma movie",1,3,"sigma")
print(super)
super2 = Movie("sigma movie",1,3,"sigma")
print(super2)