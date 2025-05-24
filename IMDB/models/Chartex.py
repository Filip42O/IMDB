import matplotlib.pyplot as plt
import numpy as np
from models.Movie import Movie

from storage.File_Handler import File_Handler


class CHARTEX:

    def get_categories_chart(movies_list : list[Movie]):
        movies_cats = dict()
        for movie in movies_list:
            for category in movie.Categories:
                key = category.name.replace("_", " ")
                movies_cats[key] = movies_cats.get(key, 0) + 1

        plt.figure()
        plt.bar(movies_cats.keys(), movies_cats.values())
        plt.xticks(rotation=60, ha='right')
        plt.xlabel('Categories')
        plt.ylabel('Number')
        plt.title('Movie Categories')
        plt.tight_layout()
        # plt.show()
        return plt

    def __init__(self):
        File_Handler.loadmoviesfromfile("../movies_saved")
        self.movies = File_Handler.movie_list
    
    
    def get_length_chart(self):
        lengths = [int(movie.Length) for movie in self.movies]
        min_len = min(lengths)
        max_len = max(lengths)
        movies_lens = dict()
        for i in range(min_len,max_len+1):
            movies_lens[i] = movies_lens.get(i, 0)
        for movie in self.movies:
            movies_lens[movie.Length] = movies_lens.get(movie.Length, 0)+1
        print(movies_lens)
        plt.figure()
        plt.bar(movies_lens.keys(), movies_lens.values())
        plt.xlabel('Length')
        plt.ylabel('Number')
        plt.title('Movie Length')
        plt.tight_layout()
        plt.show()
