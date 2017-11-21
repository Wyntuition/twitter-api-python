# To run this code, first edit config.py with your configuration, then:
#   -d  Data directory to save json file of strem
#   -q  Query for tweets
#
# mkdir data
# python twitter_stream_download.py -q apple -d data
# 
# It will produce the list of tweets for the query "apple" 
# in the file data/stream_apple.json

import config
import argparse
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

def get_parser():
    """Get parser for command line arguments."""
    parser = argparse.ArgumentParser(description="Twitter Downloader")
    parser.add_argument("-q",
                        "--query",
                        dest="query",
                        help="Query/Filter",
                        default='-')
    parser.add_argument("-d",
                        "--data-dir",
                        dest="data_dir",
                        help="Output/Data Directory")
    return parser

class MyListener(StreamListener):
 
    def __init__(self, data_dir, query):
        query_fname = ''.join(one_char for one_char in query)
        self.outfile = "%s/stream_%s.json" % (data_dir, query_fname)

    def on_data(self, data):
        try:
            with open(self.outfile, 'a') as f:
                f.write(data)
                print(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
            time.sleep(5)
        return True
 
    def on_error(self, status):
        print(status)
        return True


parser = get_parser()
args = parser.parse_args()

auth = OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_secret)

twitter_stream = Stream(auth, MyListener(args.data_dir, args.query))
twitter_stream.filter(track=[args.query])
