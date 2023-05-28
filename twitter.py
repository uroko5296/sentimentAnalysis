import tweepy
from textblob import TextBlob

# Twitter APIキー情報
consumer_key = "8QebdAgtJKXY74iJeLCER4AKZ"
consumer_secret = "0rNGrZdZ7bqcLgjdaYgog9vQXXMdLamxDvqOLAb4XvsTVbordh"
access_token = "1662739057972228097-OOzqPcGXRIAVqBM5w3q8odmOefewcv"
access_token_secret = "ntblwv7i1dQHLS4t9vsOvXrSJugHXeEXxv4tLXLeEeBq6"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# ビットコインに関するツイートを取得
public_tweets = api.search_tweets('Bitcoin', count=100, tweet_mode='extended', lang='en')

for tweet in public_tweets:
    # ツイートの本文を取得
    tweet_text = tweet.full_text
    # TextBlobオブジェクトを作成
    blob = TextBlob(tweet_text)
    # 感情分析の結果を取得
    polarity, subjectivity = blob.sentiment
    print(tweet_text, polarity, subjectivity)
