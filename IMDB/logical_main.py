from models.User import User
from models.Movie import Movie
from models.Review import Review
from storage.File_Handler import File_Handler


#ladowanie z plikow
File_Handler.loadmoviesfromfile("./movies_saved")
users = File_Handler.loaduserfromfile("./users_saved")

# for user in users[:1]:
#     print(f"{user} :",end=" ")
#     for mov in user.watched_list:
#         print(mov)
#     print()

print("movies are:")
for movie in users[0].watched_list:
    print(movie)

users[-1].setpassword("test")

File_Handler.saveuserstofile("./users_saved",users)

