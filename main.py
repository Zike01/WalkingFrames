import os
import sys
import json
from bot import TwitterBot
from dotenv import load_dotenv


load_dotenv()

consumer_key = os.getenv("API_KEY")
consumer_secret = os.getenv("API_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
bearer_token = os.getenv("BEARER_TOKEN")

twitter_bot = TwitterBot(
    consumer_key, consumer_secret, access_token, access_token_secret, bearer_token
)

clientv1 = twitter_bot.get_twitter_v1()
clientv2 = twitter_bot.get_twitter_v2()


# Get current season, ep and frame from config file
with open("config.txt", "r") as config:
    data = json.load(config)

curr_season = data["curr_season"]
curr_ep = data["curr_ep"]
curr_frame = data["curr_frame"]

image_path = f"images\\S{curr_season:02d}\\{curr_ep:02d}\\frame_{curr_frame}.jpg"

# Upload media file if image exists
try:
    media = clientv1.media_upload(image_path)
except FileNotFoundError:
    # Go to the first frame of the next episode if image path does not exist
    curr_ep += 1
    curr_frame = 1
    try:
        media = clientv1.media_upload(image_path)
    except FileNotFoundError:
        # Go to the first ep of the next season if there is no next episode
        curr_season += 1
        curr_ep = 1
        curr_frame = 1
        try:
            media = clientv1.media_upload(image_path)
        except FileNotFoundError:
            sys.exit()

# Get media id of the newly uploaded image
media_id = media.media_id

# Get the total number of frames in the episodes
current_dir = f"images\\S{curr_season:02d}\\{curr_ep:02d}"
total_frames = len(os.listdir(current_dir))


# upload the tweet
text = f"The Walking Dead - Season {curr_season:02d} Episode {curr_ep:02d} - Frame {curr_frame} of {total_frames}"
response = clientv2.create_tweet(text=text, media_ids=[media_id])

# print link to the tweet
print(text)
print(f"https://twitter.com/walking_frames/status/{response.data['id']}")

curr_frame += 1

# Store newly updated values to the config file
data["curr_season"] = curr_season
data["curr_ep"] = curr_ep
data["curr_frame"] = curr_frame

with open("config.txt", "w") as config:
    json.dump(data, config)
