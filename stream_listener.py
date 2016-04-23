'''
Start a Stream Listener
'''
import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


class FansListener(StreamListener):
    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)

def start():
    # Twitter credentials are stored in a json file
    with open('credentials.json') as data_file:
        credentials = json.load(data_file)

    # We will record all entries with words 'betis' or 'sevilla' ,
    # Then, we will discard those that are not relevant to the study
    # (Eg "... the University of Sevilla ..." or "... on the street Betis ..."

    track_list = ['betis', 'sevilla']
    auth = OAuthHandler(credentials["consumer_key"], credentials["consumer_secret"])
    auth.set_access_token(credentials["access_token"], credentials["access_token_secret"])
    stream = Stream(auth, FansListener())
    stream.filter(track=track_list)


if __name__ == '__main__':
    start()
