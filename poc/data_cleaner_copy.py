'''
Description: Clean the raw data
'''

import json
import pandas as pd
import re

key_words = {'feria': ['feria'],
            'betis': ['betis'],
             'sevilla': ['sevillafc', 'sevilla fc', 'un sevilla', 'l sevilla', 'afc', 'gol', 'futbol', 'fútbol', 'sevillis', 'liga', 'leage', 'uefa']}

class Twitter_Data_Loader():
    def __init__(self,key_words):
        self.key_words = key_words

    def parse_tweet_text(self, text):
        return text.replace('\n', ' ').replace('\r', '').lower()

    # def find_word(word, text):
    #     match = re.search(word, text)
    #     if match:
    #         return True
    #     return False

    def check_key_words(self, key, tweet_text):
        words = key_words.get(key)
        for word in words:
            if(re.search(word, tweet_text)):
                return True
        return False

    def load_tweets(self, file_name):
        tweets_data_raw = []
        tweets_file = open(file_name, "r")
        for line in tweets_file:
            try:
                if line.strip() != '':
                    tweet = json.loads(line)
                    tweets_data_raw.append(tweet)
            except:
                continue

        tweets = pd.DataFrame()
        tweets['text'] = [parse_tweet_text(tweet['text']) for tweet in tweets_data_raw]
        tweets['lang'] = [tweet['lang'] for tweet in tweets_data_raw]
        tweets['city'] = [tweet['place']['name'] if tweet['place'] != None else None for tweet in tweets_data_raw]
        tweets['coordinates'] = [tweet['geo']['coordinates'] if tweet['geo'] != None else None for tweet in tweets_data_raw]
        for key in key_words:
            tweets[key] = tweets['text'].apply(lambda tweet_text: check_key_words(key, tweet_text))
        return tweets

# if __name__ == '__main__':
tweets = load_tweets('./data/tweets_data3.txt')
print('Total: %d' % len(tweets))
for key in key_words:
    print(key, ":", len(tweets[tweets[key]]))
print('Localizados: %d' % len(tweets[tweets.coordinates.notnull()]))



# Drawing
import matplotlib.pyplot as plt
print('Analyzing tweets by Team\n')
prg_langs = list(key_words.keys())
tweets_by_prg_lang = []
for key in key_words:
    tweets_by_prg_lang.append(tweets[key].value_counts()[True])
# tweets_by_prg_lang = [tweets['betis'].value_counts()[True], tweets['sevilla'].value_counts()[True]]


x_pos = list(range(len(prg_langs)))
width = 0.8
fig, ax = plt.subplots()
plt.bar(x_pos, tweets_by_prg_lang, width, alpha=1, color='g')
ax.set_ylabel('Number of tweets', fontsize=15)
ax.set_title('Ranking: Betis vs. Sevilla', fontsize=10, fontweight='bold')
ax.set_xticks([p + 0.4 * width for p in x_pos])
ax.set_xticklabels(prg_langs)
plt.grid()
plt.savefig('./out/betis_sevilla_feria.png', format='png')