'''
Description: Load the raw data from text files, clean it and save it into repository
'''
import re


class TwitterDataProcess():
    def __init__(self, survey, topics):
        self.survey = survey
        self.topics = topics

    @staticmethod
    def compact_tweet_text(tweet_text):
        return tweet_text.replace('\n', ' ').replace('\r', '').lower()

    @staticmethod
    def to_dictionary(coordinate):
        keys = ["lat", "lng"]
        return dict(zip(keys, coordinate))

    def check_key_words(self, topic_key, tweet_text):
        if re.search(topic_key, tweet_text):
            for word in self.topics.get(topic_key):
                if re.search(word, tweet_text):
                    return True
        return False

    def process_tweet(self, raw_tweet):
        tweet = dict()
        tweet_valid = False
        text = TwitterDataProcess.compact_tweet_text(raw_tweet['text'])
        for topic_key in self.topics:
            if self.check_key_words(topic_key, text):
                tweet_valid = True
                tweet["topic"] = topic_key
                break
        if tweet_valid:
            tweet['survey'] = self.survey
            tweet['text'] = text
            tweet['lang'] = raw_tweet['lang']
            tweet['city'] = raw_tweet['place']['name'] if raw_tweet['place'] is not None else None
            if raw_tweet['geo'] is None:
                tweet['coordinates'] = False
            else:
                tweet['coordinates'] = True
                tweet.update(TwitterDataProcess.to_dictionary(raw_tweet['geo']['coordinates']))
            return tweet
        else:
            return None

