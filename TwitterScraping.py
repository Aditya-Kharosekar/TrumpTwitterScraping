import tweepy
import json
from tweepy import OAuthHandler
import codecs

consumer_key = "i387QW7Eqgh12UHmK3VoQO9K5"
consumer_secret = "BQI8c5eKale4etdA21mawnFqOmAziDQpnThm679V7UtLjbWlMG"
access_token = "816857419338764288-S8Ay111O2Mo32QAs88tSnv5uKvmGCkF"
access_secret = "HVU19yLuV0klltJl1fsDibAi7Hiq1U4GwsEV9kozTAc1m"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

all_tweets = []

new_tweets = api.user_timeline(screen_name="realDonaldTrump", count=200)

#all_tweets.extend(new_tweets)
#oldest = all_tweets[-1].id-1

t = new_tweets[0];
print(t.text)
print(t.created_at)

#while len(new_tweets) > 0:
#    new_tweets = api.user_timeline(screen_name = "realDonaldTrump", count=200, max_id = oldest)
#    all_tweets.extend(new_tweets)
#    oldest = all_tweets[-1].id-1;

file = codecs.open("random2.txt", "a", "utf-8")
for tweet in all_tweets:
    file.write(tweet.text)