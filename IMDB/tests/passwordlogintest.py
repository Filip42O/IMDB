from models.User import User
from storage.File_Handler import File_Handler


#tomeczekPL
#turbo

#init pliczku clear
# maciek = User()
# maciek.setusername("maciekKox")
# maks = User()
# maks.setusername("maks_destrojer")
# tomek = User()
# tomek.setusername("tomeczekPL")
# users = [maciek, maks, tomek]
# File_Handler.saveuserstofile("./users_saved",users)
# pass


File_Handler.loaduserfromfile("./users_saved")
users = list(File_Handler.user_list)
username_input = input("Please enter your username: ")
nick_obj = dict()
for user in users:
    nick_obj[user.username] = user
# print(nick_obj)

if username_input in nick_obj:
    print("found user")
    found = nick_obj[username_input]
    # print(found)
    password_input = input("Please enter your password: ")
    #found.setpassword("turbo")

    if found.checkpassword(password_input):
        print("login successful")
    else:
        print("login failed")


File_Handler.saveuserstofile("./users_saved",users)