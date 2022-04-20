class library:
    def __init__(self, title, release_date, genre, views):
        self.title = title
        self.release_date = release_date
        self.genre = genre
        self.views = views

    def play(self, views):
        views += 1

class movies(library):
    def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)

    def __str__(self):
        return f'{self.title} ({self.release_date})'

class series(library):
    def __init__(self, episode, season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode = episode
        self.season = season
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

sim = series(title="The Simpsons", release_date=1999, genre="action", views=55 ,season=10, episode=5)
pulp = movies(title="Pulp Fiction", release_date=1994, genre="Romantic", views=90)
print(sim)
print(pulp)

#6. Przechowuje filmy i seriale w jednej liście?
#Możesz wytłumaczyć?


