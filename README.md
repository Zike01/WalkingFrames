# Walking Frames

some text

## Installation
```
git clone ''
cd WalkingFrames
pip install -r requirements.txt
```

## Usage

### Frames processor
Create a video folder (input) and images folder (output). This can be anywhere on your computer.

Open framesprocessor.py and set the VIDEO_PATH and IMAGE_PATH at the top of the file.

Make sure the EXTENSION matches the extension of the video files

Paste videos in video folder and organise the folders like so:

All videos must have the same naming convention (S0Xe0X) or otherwise the program will not work.

- Run framesprocessor.py
- Enter the current season you wish to process
- Wait for output images to appear in the image folder.
- Repeat for every season

### Twitter API
Create a .env file and set up the constants.

Create a Twitter developer account and open the [developer dashboard](https://developer.twitter.com/en/portal/dashboard)

Create new app

In settings make sure you set up user authentication (write only). This will allow you to post your tweets.

Go to Keys and tokens and generate the tokens required for authentication.

Paste the newly generated values in the .env file. In case you lose these values they can be regenerated at any time through the developer portal.

[Tweepy Documentation](https://docs.tweepy.org/en/stable/)

### Main Script
All you need to do here is change the TITLE constant to the name of the TV Show/movie you wish to post. You can also change the tweet caption on line 67.

### Task Scheduler
Find a way to schedule your script to run every X minutes. For windows you can use task scheduler:

For free accounts you can only post 50 tweets/day, or roughly 1 tweet every 30 minutes.
