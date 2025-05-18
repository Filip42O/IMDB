from models.User import User
from storage.File_Handler import File_Handler

# File_Handler.loaduserfromfile("./test_zapis")
#
# for userek in File_Handler.user_list:
#     print(userek)
#
filip = User()
print(filip)
mikolaj = User()
mikolaj.setusername("miko_rozpruwacz")
print(mikolaj)

tomasz = User()
tomasz.setusername("tomaszkozaczek")
print(tomasz)

File_Handler.user_list.append(tomasz)
File_Handler.user_list.append(mikolaj)

File_Handler.saveuserstofile("../storage/reviews",File_Handler.user_list)