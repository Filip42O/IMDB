from models.Movie import Movie


class Review:
    __global_id = 501
    taken_id = set()

    
    def cleardata() -> None:
        Review.__global_id = 501
        Review.taken_id.clear()
    
    def __init__(self, movie : Movie, rating : float, description : str, user_id: int):
        self.id = Review.__global_id
        Review.taken_id.add(self.id)
        Review.__global_id += 1

        self.rating = rating
        self.description = description
        self.movie = movie
        self.user_id = user_id


    #ta metoda upewnia sie ze z naturalnych przyczyn id nie bedzie takie samo jak movie ktorego wczytalismy
    def overrideID(self, new_id: int) -> None:
        # Review.__global_id = new_id + 1
        Review.taken_id.remove(self.id)

        if len(Review.taken_id) > 0:
            Review.__global_id = max(Review.taken_id) + 1

        #sprawdzamy czy id jest zajete
        if new_id in Movie.taken_id:
            raise Exception(f"Id filmu: {new_id} jest juz zajete!")
        else:
            self.id = new_id
            Movie.taken_id.add(self.id)
            Movie.__global_id = max(Movie.taken_id) + 1
            
    def get_reviews_by_user_id(user_id: int, list_to_search : list['Review']) -> list['Review']:
        result = list()
        for review in list_to_search:
            #print(review.user_id)
            if int(review.user_id) == int(user_id): #trzeba castowac do inta
                result.append(review)
        return result
    #true jak success
    def remove_by_id_from_list(review_list: list['Review'], id: int) -> bool:
        #returns true if removed, false if not
        for i in range(len(review_list)):
            if id == review_list[i].id:
                review_list.pop(i)
                return True
        return False
    
    def __str__(self):
        return f"Review:[{self.id}] by {self.user_id} for {self.movie}: {self.rating}/10 -> {self.description}"

