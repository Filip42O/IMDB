from re import search
from typing import List

from models.Movie import Movie


class F_I_L_T_R_O_N:


    def __init__(self, movies : List[Movie]):
        self.movies = movies
        self.movies_dict = dict()

        for movie in movies:
            self.movies_dict[frozenset(movie.Title.lower().split())] = movie



    def search(self, word : str):
        search_list = set(word.lower().split(sep=' '))
        result_list = list()
        for titleSet, movie in self.movies_dict.items():
            if search_list.issubset(titleSet):
                result_list.append(movie)
        return result_list