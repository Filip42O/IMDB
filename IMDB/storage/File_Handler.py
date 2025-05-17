from models.User import User
from models.Review import Review

class File_Handler:
    user_list = list()
    def __init__(self):
        pass

    def loaduserfromfile(file_name : str):
        try:
            with open(file_name,'r') as file:
                for line in file:
                    line = line.strip() #czyscimy ze new line
                    elems = line.split(sep=':')
                    #elems ['101', 'maciekKox', 'hash']
                    user = User()
                    user.overrideID(int(elems[0]))
                    user.setusername(elems[1].lower())
                    user.setpasswordNoHash(elems[2])
                    File_Handler.user_list.append(user)
        except FileNotFoundError:
            raise Exception(f"File Not Found -> {file_name}")

    def saveuserstofile(filename : str , users_list : list[User]):
        try:
            file = open(filename,'w')
            for user in users_list:
                file.write(f"{user.id}:{user.username}:{user.getpassword()}\n")
        except IOError as ioerror:
            print(f"Błąd podczas uruchamiania metody zapisu do pliku: {ioerror}")

    def savereviewstofile(filename : str , review_list : list[Review]):
        pass