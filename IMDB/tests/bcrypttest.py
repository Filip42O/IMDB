import bcrypt

password = "mojesuperturbodobrehaslo"

salt = bcrypt.gensalt()
#print(salt)
hashed = bcrypt.hashpw(password.encode("utf-8"),salt)
print(hashed)
#jak jest bytowe to ma na poczatku b'tu convertuje na stringa normalnie'
print(hashed.decode("utf-8"))

#hashe zapisujemy do pliku a user jak se wpisze haslo to porwnojemy do niego
decoded = bcrypt.checkpw("dwadwa".encode("utf-8"),hashed)
print(decoded)