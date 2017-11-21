# Ineracting with the Twitter API with Python (Tweepy)

## Setup 

1. Create an application if you haven't yet, at `api.twitter.com`, get the credentials and put them in `config.py` as:

    ```
    consumer_key = '<ENTER>'
    consumer_secret = '<ENTER>'
    access_token = '<ENTER>'
    access_secret = '<ENTER>'
    ```

1. Run the provided Python scripts that do things such as listing tweets, timelines & friends. See the examples below.

## Get a stream a tweets, save to a file

`python stream-tweets-to-file.py -q dotnetcore -d data`

## Display tweets in file

`python display-tweet-paramaters.py`