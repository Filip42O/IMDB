from re import search
from typing import List

from models.Category import Category
from models.Movie import Movie


class F_I_L_T_R_O_N:

    def __init__(self, movies: List[Movie]):
        self.movies = movies
        self.movies_dict = dict()
        self.result = list()

        for movie in movies:
            self.movies_dict[frozenset(movie.Title.lower().split())] = movie

    def search(self, word: str) -> List[Movie]:
        search_list = set(word.lower().split(sep=' '))
        result_list = list()
        for titleSet, movie in self.movies_dict.items():
            if search_list.issubset(titleSet):
                result_list.append(movie)
        return result_list

    def filter_by_category(self, categories_as_string: str) -> None:
        categories_splited = categories_as_string.split(sep=',')
        categories = list()

        for category in categories_splited:
            categories.append(Category[category])

        for cat in categories:
            for mov in self.movies:
                if cat in mov.Categories:
                    self.result.append(mov)

    def filter_by_director(self, directors_as_string: str) -> None:
        directors_splited = directors_as_string.split(sep=',')

        for dire in directors_splited:
            for mov in self.movies:
                if dire == mov.Director:
                    self.result.append(mov)

    def filter_by_length(self, minLength: int, maxLength: int) -> None:
        for mov in self.movies:
            if minLength <= mov.Length <= maxLength:
                self.result.append(mov)

    def filter_by_year(self, minYear: int, maxYear: int) -> None:
        for mov in self.movies:
            if minYear <= mov.Year <= maxYear:
                self.result.append(mov)