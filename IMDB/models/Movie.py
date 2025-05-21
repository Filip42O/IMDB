from models.Category import Category


class Movie:
    __global_id = 401
    taken_id = set()

    def cleardata():
        Movie.__global_id = 401
        Movie.taken_id.clear()
    def __init__(self,Title,Length,Year,Director):
        self.id = Movie.__global_id
        Movie.taken_id.add(self.id)
        Movie.__global_id += 1

        self.Title = Title
        self.Length = Length
        self.Year = Year
        self.Director = Director
        self.Categories = list()

    def addcategory(self,category : Category) -> None:
        self.Categories.append(category)

    def removecategory(self,category : Category) -> None:
        self.Categories.remove(category)

    def getCategories(self) -> str:
        result = ""
        for category in self.Categories:
            result += (str(category.name))
            result += ","
        result = result.rstrip(",")
        return result

    def showCategories(self) -> list[str]:
        result = list()
        for category in self.Categories:
            result.append(str(category.name))
        return result

    #ta metoda upewnia sie ze z naturalnych przyczyn id nie bedzie takie samo jak movie ktorego wczytalismy
    def overrideID(self, new_id: int) -> None:
        # Movie.__global_id = new_id + 1
        Movie.taken_id.remove(self.id)


        if len(Movie.taken_id) > 0:
            Movie.__global_id = max(Movie.taken_id) + 1

        #sprawdzamy czy id jest zajete
        if new_id in Movie.taken_id:
            raise Exception(f"Id filmu: {new_id} jest juz zajete!")
        else:
            self.id = new_id
            Movie.taken_id.add(self.id)
            Movie.__global_id = max(Movie.taken_id) + 1

    #Metoda na podstawie ID przekazanego zwraca TRUE lub FALSE na podstawie obecnego global_id
    def movie_exists(id) -> bool:
        if id in range(401,Movie.__global_id):
            return True
        return False

    def niceformat(self) -> str:
        return f"{self.Title} - {self.Year} - {self.Director} - {self.getCategories().replace(']',' ').replace('[',' ').replace(', ',' ')}"

    def __str__(self):
        return f"[{self.id}:{self.Title} from {self.Year} [Length:{self.Length}] by {self.Director} Categories: {self.showCategories()}]"