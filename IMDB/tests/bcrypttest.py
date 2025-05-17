import bcrypt

password = "mojesuperturbodobrehaslo"

salt = bcrypt.gensalt()
#print(salt)
hashed = bcrypt.hashpw(password.encode("utf-8"),salt)
# hashed = "$2b$12$SWtnGJ/vaAcd5CIMcFtSBe4aNi/Ey4a4U7GiD8.AnPkiz/q4fwCX2".encode("utf-8")
print(hashed)
#jak jest bytowe to ma na poczatku b'tu convertuje na stringa normalnie'
print(hashed.decode("utf-8"))

#hashe zapisujemy do pliku a user jak se wpisze haslo to porwnojemy do niego
decoded = bcrypt.checkpw(password.encode("utf-8"),hashed)
print(decoded)