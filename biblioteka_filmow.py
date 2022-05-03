import random
from faker import Faker

fake = Faker()

class Library:
    def __init__(self, title, release_date, genre, views):
        self.title = title
        self.release_date = release_date
        self.genre = genre
        self.views = views

    def play(self, views):
        views += 1

class Movies(Library):
    def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
    def __repr__(self):
        return f'movie("{self.title}", "{self.genre}", "{self.release_date}", "{self.views}")'
    def __str__(self):
        return f'{self.title} ({self.release_date})'

class Series(Library):
    def __init__(self, episode, season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode = episode
        self.season = season
    def __repr__(self):
        return f'series("{self.title}", "{self.season}", "{self.episode}", "{self.genre}", "{self.release_date}", "{self.views}")'
    def __str__(self):
        if self.episode >= 0 and self.episode < 10:
            if self.season >= 0 and self.season < 10:
                return f'{self.title} S0{self.season}E0{self.episode}'
            else:
                return f'{self.title} S{self.season}E0{self.episode}'
        else:
            if self.season >= 0 and self.season < 10:
                return f'{self.title} S0{self.season}E{self.episode}'
            else:
                return f'{self.title} S{self.season}E{self.episode}'



def List_of_movies_and_series(number):
    empty = []
    for i in range(0, number):
        a = random.randrange(0, 2)
        if a == 0:
            type = 'movie'
        else:
            type = 'series'       
        if type == 'movie':
            genre = ['Action', 'Romanse', 'Sport', 'Horror', 'Thriller', 'Adventure', 'Documentary']
            a = random.randrange(0, 7)
            titles = fake.word()
            release_dates = fake.date()
            genres = genre[a]
            viewss = fake.pyint()
            i = Movies(title=titles, release_date=release_dates, genre=genres, views=viewss)
            empty.append(i)
        elif type == 'series':
            genre = ['Action', 'Romanse', 'Sport', 'Horror', 'Thriller', 'Adventure', 'Documentary']
            a = random.randrange(0, 7)
            b = random.randrange(0, 100)
            c = random.randrange(0, 100)
            titles = fake.word()
            release_dates = fake.date()
            genres = genre[a]
            viewss = fake.pyint()
            episodes = b
            seasons = c
            i = Series(title=titles, release_date=release_dates, genre=genres, views=viewss, episode=episodes, season=seasons)
            empty.append(i)
    print(empty)
    for j in empty:
        print(j)


List_of_movies_and_series(5)

sim = Series(title="The Simpsons", release_date=1999, genre="action", views=55 ,season=10, episode=5)
pulp = Movies(title="Pulp Fiction", release_date=1994, genre="Romantic", views=90)
