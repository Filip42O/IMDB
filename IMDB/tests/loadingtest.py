from models.User import User
from storage.File_Handler import File_Handler

File_Handler.loaduserfromfile("../users_saved")

for userek in File_Handler.user_list:
    print(userek)

mikolaj = User()
mikolaj.setusername("miko_rozpruwacz")
print(mikolaj)