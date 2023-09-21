import cv2
import os


# -----------------CONSTANTS-------------------#
VIDEO_PATH = ""
IMAGE_PATH = ""
TARGET_FPS = 1
# ---------------------------------------------#


def process(file):
    video = f"{VIDEO_PATH}/{file}"
    capture = cv2.VideoCapture(video)
    fps = round(capture.get(cv2.CAP_PROP_FPS))

    curr_frame = 0
    frame_count = 0
    while True:
        success, frame = capture.read()

        if not success:
            break

        # Only save the image if the current frame is divisible by the fps of the original video
        # This way only 1 frame is processed per second

        if curr_frame % fps == 0:
            frame_count += 1
            episode = int(file.split(".")[0].split("e")[1])
            exists = os.path.isdir(f"{IMAGE_PATH}/S{season:02d}/{episode:02d}")

            if not exists:
                os.makedirs(f"{IMAGE_PATH}/S{season:02d}/{episode:02d}")

            name = f"{IMAGE_PATH}/S{season:02d}/{episode:02d}/frame_{frame_count}.jpg"
            cv2.imwrite(name, frame)
        curr_frame += 1
    capture.release()


if __name__ == "__main__":
    season = int(input("Season: "))
    eps = os.listdir(f"{VIDEO_PATH}/S{season:02d}")
    for ep in eps:
        process(ep)
