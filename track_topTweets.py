# Import the Twython class
from twython import Twython
import json
import pandas as pd


# Load tokens from json file
with open("twitter_tokens.json", "r") as file:
    tokens = json.load(file)

# Instantiate an object
python_tweets = Twython(tokens['CONSUMER_KEY'], tokens['CONSUMER_SECRET'])

# Create our query
query = {'q': 'Breaking news',
        'result_type': 'popular',
        'count': 20,
        'lang': 'en',
        }

# Search tweets
dict_ = {'user': [], 'date': [], 'text': [], 'favorite_count': []}
for status in python_tweets.search(**query)['statuses']:
    dict_['user'].append(status['user']['screen_name'])
    dict_['date'].append(status['created_at'])
    dict_['text'].append(status['text'])
    dict_['favorite_count'].append(status['favorite_count'])


# Structure data in a pandas DataFrame for easier manipulation
df = pd.DataFrame(dict_)
df.sort_values(by='favorite_count', inplace=True, ascending=False)
df.head(5)
#export to csv
df.to_csv('output.csv', encoding='utf-8')