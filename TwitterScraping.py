import tweepy
import json
from tweepy import OAuthHandler
import codecs

#def process_or_store(tweet):
#    print(json.dumps(tweet))
#    print()
#    with open("random.txt", 'w') as outfile:
#        json.dump(tweet.text, outfile, sort_keys = True, indent=4)

consumer_key = "i387QW7Eqgh12UHmK3VoQO9K5"
consumer_secret = "BQI8c5eKale4etdA21mawnFqOmAziDQpnThm679V7UtLjbWlMG"
access_token = "816857419338764288-S8Ay111O2Mo32QAs88tSnv5uKvmGCkF"
access_secret = "HVU19yLuV0klltJl1fsDibAi7Hiq1U4GwsEV9kozTAc1m"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

stuff = api.user_timeline(screen_name="realDonaldTrump", count=200)

file = codecs.open("random.txt", "a", "utf-8")
count=1
for status in stuff:
    #print(status.text)
    #print()
    file.write(status.text)

#for tweet in tweepy.Cursor(api.home_timeline).items(10):
#    process_or_store(tweet._json)