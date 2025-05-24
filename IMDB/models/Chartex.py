import matplotlib.pyplot as plt
import numpy as np
from models.Movie import Movie
from models.Review import Review
from models.User import User

from storage.File_Handler import File_Handler


class CHARTEX:
    colors = [
    '#8000ff', '#6a22fe', '#5247fc', '#3c68f9', '#2489f5',
    '#0ca7ef', '#00c6e7', '#00deb3', '#23f47b', '#6ffb3f',
    '#baff00', '#f5f100', '#f5cc00', '#f5a800', '#f58600',
    '#f46800', '#f24b00', '#ec2b00', '#e60b00', '#ff0000',
    '#ff2211', '#ff4724', '#ff6835']
            
    def get_categories_chart(movies_list : list[Movie]):
        movies_cats = dict()
        for movie in movies_list:
            for category in movie.Categories:
                key = category.name.replace("_", " ")
                movies_cats[key] = movies_cats.get(key, 0) + 1

        plt.figure()
        plt.bar(movies_cats.keys(), movies_cats.values(), color=CHARTEX.colors)
        plt.xticks(rotation=60, ha='right')
        plt.xlabel('Categories')
        plt.ylabel('Number')
        plt.title('Movie Categories')
        plt.tight_layout()
        # plt.show()
        return plt

    def get_reviews_chart(reviews_list : list[Review], users_list : list[User]):
        usrID_revCNT = dict[str,int]()
        
        #init mapki
        for user in users_list:
            usrID_revCNT[user.username] = 0
            for review in reviews_list:
                #[id_review:id_movie:id_user:ocena:desc]
                if user.id == review.user_id:
                    usrID_revCNT[user.username] += 1
        
        
        usrID_revCNT = dict(sorted(usrID_revCNT.items(),key=lambda x: x[1], reverse=True))
        plt.figure()
        plt.bar(usrID_revCNT.keys(), usrID_revCNT.values(),color=CHARTEX.colors)
        plt.xticks(rotation=60, ha='right')
        plt.xlabel('Usernames')
        plt.ylabel('Number of Reviews')
        plt.title('Users reviews count')
        plt.tight_layout()
        #plt.show()
        plt.gca().yaxis.set_major_locator(plt.MaxNLocator(integer=True))  # Ensure y-axis has integer ticks
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
