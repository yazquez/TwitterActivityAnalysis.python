'''
Description: Load the raw data from text files, clean it and save it into repository
'''

import json
import re
from repository import Repository




class TwitterDataProcess():
    def __init__(self, topics, file_name):
        self.file_name = file_name
        self.topics = topics
        self.tweets = []
        self.repository = Repository()
        self.process_tweets()

    @staticmethod
    def compact_tweet_text(tweet_text):
        return tweet_text.replace('\n', ' ').replace('\r', '').lower()

    @staticmethod
    def to_dictionary(coordinate):
        keys = ["Lat", "Lng"]
        return dict(zip(keys, coordinate))

    def check_key_words(self, topic_key, tweet_text):
        if re.search(topic_key, tweet_text):
            for word in self.topics.get(topic_key):
                if re.search(word, tweet_text):
                    return True
        return False

    def process_tweets(self):
        self.tweets = []
        with open(self.file_name, "r") as tweets_file:
            for line in tweets_file:
                tweet = dict()
                tweet_valid = False
                try:
                    if line.strip() != '':
                        raw_tweet = json.loads(line)
                        text = TwitterDataProcess.compact_tweet_text(raw_tweet['text'])
                        for topic_key in self.topics:
                            if self.check_key_words(topic_key, text):
                                tweet_valid = True
                                tweet[topic_key] = True
                            else:
                                tweet[topic_key] = False
                        if tweet_valid:
                            tweet['text'] = text
                            tweet['lang'] = raw_tweet['lang']
                            tweet['city'] = raw_tweet['place']['name'] if raw_tweet['place'] is not None else None
                            if raw_tweet['geo'] is None:
                                tweet['coordinates'] = False
                            else:
                                tweet['coordinates'] = True
                                tweet.update(TwitterDataProcess.to_dictionary(raw_tweet['geo']['coordinates']))
                                self.tweets.append(tweet)
                            if len(self.tweets) > 1000:
                                self.repository.save_many(self.tweets)
                                self.tweets = []

                except Exception as e:
                    print(str(e))
                    continue
        self.repository.save_many(self.tweets)


# __name__ == '__main__'

if __name__ == '__main__':
    print("Init loading...")
    topics = {'feria': ['feria'],
              'betis': ['betis'],
              'sevilla': ['sevillafc', 'sevilla fc', 'un sevilla', 'l sevilla', 'afc', 'gol', 'futbol', 'fútbol',
                          'sevillis', 'liga', 'leage', 'uefa']}

    twitter_data_loader = TwitterDataProcess(topics, 'D:/Home/Projects/Twitter/Data/tweets_data7.txt')

    tweets = twitter_data_loader.tweets
    print('Total: %d' % len(tweets))


    # for x in twitter_data_loader.get_coordinates():
    #     print(x)
    #     # x.replace('[','"Lat":"').replace(',','","Long":"').replace(']','"}')
    #
    # for key_topic in topics:
    #     print(key_topic, ":", len(tweets[tweets[key_topic]]))
