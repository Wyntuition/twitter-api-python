# Ineracting with the Twitter API with Python (Tweepy)

Based on the Twitter data mining exercise from here, https://marcobonzanini.com/2015/03/09/mining-twitter-data-with-python-part-2/

## Setup

1. Create an application if you haven't yet, at `api.twitter.com`, get the credentials and put them in `config.py` as:

    ```
    consumer_key = '<ENTER>'
    consumer_secret = '<ENTER>'
    access_token = '<ENTER>'
    access_secret = '<ENTER>'
    ```

1. Run the provided Python scripts that do things such as listing tweets, timelines & friends. See the examples below.
## Functions

### Stream tweets for a given term

1. Create a directory for saving the streamed tweets to json, `mkdir data`
1. Run, replacing the -q with your query term and your file will be stored in data/, `python stream-tweets.py -q washington -d data`

### General Functions

See the `general-twitter-functions` file for some of these things that could be done: Display timeline, display tweets, display followers, display tweet metadata, display top tweets, display top tweets for topic
