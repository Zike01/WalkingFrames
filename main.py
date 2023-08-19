import os
import time
from datetime import datetime
from bot import TwitterBot
from dotenv import load_dotenv

load_dotenv()

consumer_key = os.getenv("API_KEY")
consumer_secret = os.getenv("API_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

twitter_bot = TwitterBot(
    consumer_key, consumer_secret, access_token, access_token_secret
)

clientv1 = twitter_bot.get_twitter_v1()
clientv2 = twitter_bot.get_twitter_v2()

curr_season = 1
curr_ep = 1
curr_frame = 1


while True:
    current_time = datetime.now()

    if current_time.minute % 15 == 0:
        image_path = (
            f"images\\S{curr_season:02d}\\{curr_ep:02d}\\frame_{curr_frame}.jpg"
        )

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
                    break
                
        # Get media id of the newly uploaded image
        media_id = media.media_id
        
        # Get the total number of frames in the episodes
        current_dir = f"images\\S{curr_season:02d}\\{curr_ep:02d}"
        total_frames = len(os.listdir(current_dir))
        
        text = f"The Walking Dead - Season {curr_season:02d} Episode {curr_ep:02d} - Frame {curr_frame} of {total_frames}"
        
        # upload the tweet
        response = clientv2.create_tweet(text=text, media_ids=[media_id])
        print(text)
        print(f"https://twitter.com/walking_frames/status/{response.data['id']}")
        
        time.sleep(120)
        