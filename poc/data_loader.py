'''
Description: Clean the raw data
'''

import json
import pandas as pd
import re


class TwitterDataLoader():
    def __init__(self, topics, file_name):
        # self.file_name = file_name
        self.file_name = './data/tweets_data3.txt'
        self.topics = topics
        self.tweets = pd.DataFrame()
        self.tweets_by_topic = []
        self.coordinates = []
        self.load_tweets()

    @staticmethod
    def compact_tweet_text(tweet_text):
        return tweet_text.replace('\n', ' ').replace('\r', '').lower()

    def check_key_words(self, topic_key, tweet_text):
        for word in self.topics.get(topic_key):
            if re.search(word, tweet_text):
                return True
        return False

    def to_dictionary(self, coordinate):
        keys = ["Lat", "Lng"]
        return dict(zip(keys, coordinate))

    def load_tweets(self):
        tweets_file = open(self.file_name, "r")
        tweets_data_raw = []
        for line in tweets_file:
            try:
                if line.strip() != '':
                    tweet = json.loads(line)
                    tweets_data_raw.append(tweet)
            except:
                continue
        self.tweets['text'] = [TwitterDataLoader.compact_tweet_text(tweet['text']) for tweet in tweets_data_raw]
        self.tweets['lang'] = [tweet['lang'] for tweet in tweets_data_raw]
        self.tweets['city'] = [tweet['place']['name'] if tweet['place'] is not None else None for tweet in tweets_data_raw]
        self.tweets['coordinates'] = [self.to_dictionary(tweet['geo']['coordinates']) if tweet['geo'] is not None else None for tweet in tweets_data_raw]
        for topic_key in self.topics:
            # Add one column per each topic we are analizing
            self.tweets[topic_key] = self.tweets['text'].apply(lambda tweet_text: self.check_key_words(topic_key, tweet_text))
            # Count number of tweet of each topic
            self.tweets_by_topic.append(self.tweets[topic_key].value_counts()[True])


        self.coordinates = self.tweets[self.tweets.coordinates.notnull()]['coordinates']

            #.apply(lambda c : c.replace('[','"Lat":"').replace(',','","Long":"').replace(']','"}'))

    def get_coordinates(self):
        columns_list = []
        for topic_key in self.topics:
            columns_list.append(topic_key)

        columns_list.append('text')
        x = self.tweets[self.tweets.coordinates.notnull()][columns_list]
        return x



# __name__ == '__main__'

if __name__ == '__main__':
    print("Init loading...")
    topics = {'feria': ['feria'],
              'betis': ['betis'],
              'sevilla': ['sevillafc', 'sevilla fc', 'un sevilla', 'l sevilla', 'afc', 'gol', 'futbol', 'fútbol',
                          'sevillis', 'liga', 'leage', 'uefa']}

    twitter_data_loader = TwitterDataLoader(topics, './data/tweets_data2.txt')
    tweets = twitter_data_loader.tweets
    print('Total: %d' % len(tweets))
    print('Localizados: %d' % len(twitter_data_loader.coordinates))


    x =  twitter_data_loader.get_coordinates()

    x.to_csv("./out/dataframe.csv")
    for x in twitter_data_loader.get_coordinates():
        print(x)
        # x.replace('[','"Lat":"').replace(',','","Long":"').replace(']','"}')

    for key_topic in topics:
        print(key_topic, ":", len(tweets[tweets[key_topic]]))



    # # Drawing
    # import matplotlib.pyplot as plt
    #
    # print('Analyzing tweets by Topic\n')
    # prg_topics = list(topics.keys())
    # tweets_by_topic = twitter_data_loader.tweets_by_topic
    # x_pos = list(range(len(prg_topics)))
    #
    # width = 0.8
    # fig, ax = plt.subplots()
    # plt.bar(x_pos, tweets_by_topic, width, alpha=1, color='g')
    # ax.set_ylabel('Number of tweets', fontsize=15)
    # ax.set_title('Ranking: ' + "-".join(topics.keys()), fontsize=10, fontweight='bold')
    # ax.set_xticks([p + 0.4 * width for p in x_pos])
    # ax.set_xticklabels(prg_topics)
    # plt.grid()
    # plt.savefig('./out/betis_sevilla_feria.png', format='png')
    #
    # # Analyzing Tweets by city
    # print('Analyzing tweets by city\n')
    # tweets_by_city = tweets['city'].value_counts()
    # fig, ax = plt.subplots()
    # ax.tick_params(axis='x', labelsize=15)
    # ax.tick_params(axis='y', labelsize=10)
    # ax.set_xlabel('Countries', fontsize=15)
    # ax.set_ylabel('Number of tweets', fontsize=15)
    # ax.set_title('Top 5 countries', fontsize=15, fontweight='bold')
    # tweets_by_city[:5].plot(ax=ax, kind='bar', color='blue')
    # plt.savefig('./out/tweet_by_city.png', format='png')
