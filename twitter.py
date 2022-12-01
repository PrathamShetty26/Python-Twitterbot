import time

import tweepy

api_key='aFHPdg88r94ILXUiVCtTsLOga'
api_secret='Nqy0KWA12frxCWfp9a2gwJ6ooAw5Ehj3uCjznOZatjLTcYwWlF'
bearer_token="AAAAAAAAAAAAAAAAAAAAADryTgEAAAAAIHZubs1Mzw%2F5av8k%2BFcFVQmTuB0%3D0xt2sV8C4TUaniFO92Uf1Vch7otd4fCNLni4Z7AcUfliZmQZdE"
access_token='1393663347380260865-I4em4dbrkT1jnrjpbyrGQp54gl9TdQ'
access_token_secret='OfoVA2cm4Mvp5xghCAB1L0OtgkFzuehDeec9Hj5pyRcwX'

client=tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

class Stream(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        print(tweet.text)
        try:
            client.like(tweet.id)
            client.retweet(tweet.id)
        except Exception as error:
            print(error)
        time.sleep(1)

stream = Stream(bearer_token=bearer_token )
rule1 = tweepy.StreamRule("(#Coding AND #Python)(-is:retweet -is:reply)")
rule2 = tweepy.StreamRule("#Coding OR #Python -is:retweet -is:reply")
stream.add_rules(rule1)
stream.add_rules(rule2)

stream.filter()

