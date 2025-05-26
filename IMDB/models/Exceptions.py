
class UserIdTaken(Exception):
    def __init__(self,userid : int):
        custom = f"Id {userid} jest juz zajete!"
        super().__init__(custom)

class ReviewNotFound(Exception):
    def __init__(self):
        super().__init__("Review for that movie doesn't exist!")

class MovieIdTaken(Exception):
    def __init__(self,movieid : int):
        super().__init__(f"Film o id:{movieid} jest juz zajete!")

#Exception(f"Nie można usunąć {user.username} w usuwaniu filmu! ")
class CannotDeleteUserFromMovie(Exception):
    def __init__(self,username : str):
        super().__init__(f"User: {username} cannot be deleted from movie!")

class CannotDeleteReview(Exception):
    def __init__(self,review_id : int):
        super().__init__(f"Review: {review_id} cannot be deleted!")