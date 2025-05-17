class Movie:
    __global_id = 401
    def __init__(self,Title,Length,Year,Director):
        self.id = Movie.__global_id
        Movie.__global_id += 1

        self.Title = Title
        self.Lenght = Length
        self.Year = Year
        self.Director = Director


    #Metoda na podstawie ID przekazanego zwraca TRUE lub FALSE na podstawie obecnego global_id
    def movie_exists(id):
        if id in range(401,Movie.__global_id):
            return True
        return False

    def __str__(self):
        return f"[{self.id}:{self.Title} from {self.Year} [Length:{self.Lenght}] by {self.Director}]"