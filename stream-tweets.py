# To run this code, first edit config.py with your configuration, then:
#
# mkdir data
# python twitter_stream_download.py -q apple -d data
# 
# It will produce the list of tweets for the query "apple" 
# in the file data/stream_apple.json

from tweepy import Stream
from tweepy.streaming import StreamListener
 
class MyListener(StreamListener):
 
    def on_data(self, data):
        try:
            with open('python.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#python'])