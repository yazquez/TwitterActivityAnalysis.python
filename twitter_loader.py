'''
Description: Load the raw data from text files, clean it and save it into repository
'''

import json
from repository.repository import Repository
from twitter_process import TwitterDataProcess


class TwitterDataLoader():
    def __init__(self, survey_id, file_name):
        with open('config/surveys.json') as data_file:
            surveys = json.load(data_file)

        self.survey = surveys[survey_id]

        self.topics = dict()
        for topic in self.survey["topics"]:
            self.topics[topic["key"]] = topic["words"]

        self.file_name = file_name
        self.repository = Repository()
        self.twitterDataProcess = TwitterDataProcess(survey_id, self.topics)

    def load_tweets(self):
        tweets = []
        with open(self.file_name, "r") as tweets_file:
            for line in tweets_file:
                try:
                    if line.strip() != '':
                        tweet = self.twitterDataProcess.process_tweet(json.loads(line))
                        if tweet is not None:
                            tweets.append(tweet)
                            if len(tweets) > 1000:
                                self.repository.save_many(tweets)
                                tweets = []
                except Exception as e:
                    print("Error {0} parsing tweet: {1}".format(str(e), line))
                    continue
        if len(tweets) > 0:
            self.repository.save_many(tweets)


# __name__ == '__main__'

if __name__ == '__main__':
    print("Init loading...")
    TwitterDataLoader("spain-press", 'D:/Home/Projects/Twitter/Data/data_press0.txt').load_tweets()
    TwitterDataLoader("spain-press", 'D:/Home/Projects/Twitter/Data/data_press1.txt').load_tweets()
    TwitterDataLoader("spain-press", 'D:/Home/Projects/Twitter/Data/data_press2.txt').load_tweets()
    TwitterDataLoader("spain-press", 'D:/Home/Projects/Twitter/Data/data_press3.txt').load_tweets()

    TwitterDataLoader("sevilla-football", 'D:/Home/Projects/Twitter/Data/tweets_data1.txt').load_tweets()
    TwitterDataLoader("sevilla-football", 'D:/Home/Projects/Twitter/Data/tweets_data2.txt').load_tweets()
    TwitterDataLoader("sevilla-football", 'D:/Home/Projects/Twitter/Data/tweets_data3.txt').load_tweets()
    TwitterDataLoader("sevilla-football", 'D:/Home/Projects/Twitter/Data/tweets_data4.txt').load_tweets()
    TwitterDataLoader("sevilla-football", 'D:/Home/Projects/Twitter/Data/tweets_data5.txt').load_tweets()
    TwitterDataLoader("sevilla-football", 'D:/Home/Projects/Twitter/Data/tweets_data6.txt').load_tweets()
    TwitterDataLoader("sevilla-football", 'D:/Home/Projects/Twitter/Data/tweets_data7.txt').load_tweets()
    TwitterDataLoader("sevilla-football", 'D:/Home/Projects/Twitter/Data/tweets_data8.txt').load_tweets()
    TwitterDataLoader("sevilla-football", 'D:/Home/Projects/Twitter/Data/tweets_data9.txt').load_tweets()
    TwitterDataLoader("sevilla-football", 'D:/Home/Projects/Twitter/Data/tweets_data10.txt').load_tweets()

