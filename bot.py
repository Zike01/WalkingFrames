import tweepy


class TwitterBot:
    def __init__(
        self, consumer_key, consumer_secret, access_token, access_token_secret, bearer_token
    ):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        self.bearer_token = bearer_token

    def get_twitter_v1(self):
        """
        Get twitter API v1.1.
        This method is used to upload media files
        """
        auth = tweepy.OAuth1UserHandler(
            consumer_key=self.consumer_key,
            consumer_secret=self.consumer_secret,
            access_token=self.access_token,
            access_token_secret=self.access_token_secret,
        )
        return tweepy.API(auth, wait_on_rate_limit=True)

    def get_twitter_v2(self):
        """
        Get twitter API v2.
        This method is used to post the tweet.
        """
        client = tweepy.Client(
            consumer_key=self.consumer_key,
            consumer_secret=self.consumer_secret,
            access_token=self.access_token,
            access_token_secret=self.access_token_secret,
            bearer_token=self.bearer_token
        )

        return client
