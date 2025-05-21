from models.User import User
from models.Movie import Movie
from models.Review import Review
from storage.File_Handler import File_Handler


#ladowanie z plikow
File_Handler.loaduserfromfile("./users_saved")
File_Handler.loadmoviesfromfile("./movies_saved")
for usr in File_Handler.user_list:
    print(usr)