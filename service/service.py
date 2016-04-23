from data_loader import TwitterDataLoader
from repository import Repository


class Service:
    def get_coordinates(self):
        return Repository().get_coordinates()

    # def get_coordinates(self):
    #     topics = {'feria': ['feria'],
    #               'betis': ['betis'],
    #               'sevilla': ['sevillafc', 'sevilla fc', 'un sevilla', 'l sevilla', 'afc', 'gol', 'futbol', 'fútbol',
    #                           'sevillis', 'liga', 'leage', 'uefa']}
    #
    #     return list(TwitterDataLoader(topics, '../../data/tweets_data2.txt').coordinates)