#Import the necessary methods from
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

#Variables that contains the user credentials to access Twitter API 
access_token = "2571017252-mwNaHJo1vbv4spgyWSWaOEpdCDupc6HjZ8UYd19"
access_token_secret = "pw0mv8iUHhRY4nEoqYdDuXDqWh5V7g2o9USsIwSM2Ckbc"
consumer_key = "MqGk1nzw0beQK4WBcmz1ZetVY"
consumer_secret = "tA2xi58ExDz4fLqEERce24NaI64FedCm5vqzgsekckKkLcLnfh"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print json.loads(data)['text']
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['allergy', 'restaurant', 'epipen'])


