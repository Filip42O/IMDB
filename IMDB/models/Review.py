from models.Movie import Movie


class Review:
    __global_id = 501

    def __init__(self, movie : Movie, rating : float, description : str):
        self.id = Review.__global_id
        Review.__global_id += 1

        self.rating = rating
        self.description = description
        self.movie = movie

    def __str__(self):
        return f"Review:[{self.id}] for {self.movie}: {self.rating}/10 -> {self.description}"

