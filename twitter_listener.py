'''
Start a Stream Listener
'''
import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

class TwitterListener:
    def __init__(self, survey_id):
        with open('config/surveys.json') as data_file:
            surveys = json.load(data_file)

        self.survey = surveys[survey_id]
        track_list = []
        topics = dict()
        for topic in self.survey["topics"]:
            track_list.append(topic["key"])
            topics[topic["key"]] = topic["words"]

        self.track_list = track_list

        print(topics)

        # Twitter credentials are stored in a json file
        with open('config/credentials.json') as data_file:
            credentials = json.load(data_file)

        self.consumer_key = credentials["consumer_key"]
        self.consumer_secret = credentials["consumer_secret"]
        self.access_token = credentials["access_token"]
        self.access_token_secret = credentials["access_token_secret"]

    def start(self):
        auth = OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)

        stream = Stream(auth, TwitterStreamListener())
        stream.filter(track=self.track_list)

class TwitterStreamListener(StreamListener):
    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    tl = TwitterListener("sevilla-football").start()