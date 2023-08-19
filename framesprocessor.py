import cv2
import os

VIDEO_PATH = "videos"
IMAGE_PATH = "images"
EXTENSION = "mkv"
TARGET_FPS = 1

def process(season, episode):
    video = f"{VIDEO_PATH}/S{season}e{episode}.{EXTENSION}"
    capture = cv2.VideoCapture(video)
    fps = round(capture.get(cv2.CAP_PROP_FPS))
    
    skip = round(fps, TARGET_FPS)
    curr_frame = 0
    frame_made = 0
    while True:
        success, frame = capture.read()
        
        if not success:
            return
        
        if curr_frame % skip == 0:
            frame_made += 1
            exists = os.path.isdir(f"{IMAGE_PATH}/S{season}/{episode}")
            
            if not exists:
                os.mkdir(f"{IMAGE_PATH}/S{season}/{episode}")
                
            name = f"{IMAGE_PATH}/{episode}/frame_{frame_made}.jpg"
            cv2.imwrite(name, frame)
        curr_frame += 1

if __name__ == "__main__":
    season = int(input("Season: "))
    eps = len(os.listdir("videos"))
    
    for ep in range(1, eps+1):
        process(f"{season:02d}",f"{ep:02d}" )

