import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import KafkaProducer, KafkaClient
import json

access_token = '928600292408438785-MzCzpbk9FzynYLc5PYP3LPEs3tqxJT2'
access_token_secret =  'jFndq7Bz3O5uGTLz5GHJqjq8JmUTOul7KyNurKYwwKpgS'
consumer_key =  'J4QehTb6WzpQSUMStM778oI5r'
consumer_secret =  'C3MRCzY45H3pDy5rklPlE8aqon1ubxhVfT0gU7BEgCeJhYXgHY'

class StdOutListener(StreamListener):
    def on_data(self, data):
        producer.send("basic", json_["text"].encode('utf-8'))
        print (data)
        return True
    def on_error(self, status):
        print (status)

kafka = KafkaClient("localhost:9092")
producer = SimpleProducer(kafka)
l = StdOutListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, l)

