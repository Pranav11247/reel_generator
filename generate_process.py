import os
from text_to_audio import text_to_speech
import subprocess


def convert_text_to_audio(folder):
    print(folder)
    with open(f"user_uploads/{folder}/desc.txt", "r") as f:
        text = f.read()
        text_to_speech(text, folder)


def create_reel(folder):
    print(folder)
    command = (
        f'ffmpeg -y -f concat -safe 0 '
        f'-i user_uploads/{folder}/input.txt '
        f'-i user_uploads/{folder}/audio.mp3 '
        f'-vf "scale=1080:1920:force_original_aspect_ratio=decrease,'
        f'pad=1080:1920:(ow-iw)/2:(oh-ih)/2:black" '
        f'-c:v libx264 -c:a aac -shortest -r 30 -pix_fmt yuv420p '
        f'static/reels/{folder}.mp4'
    )
    subprocess.run(command, shell=True, check=True)


def king():
    with open("done.txt", "r") as f:
        done_folders = f.readlines()
    folders = os.listdir("user_uploads")
    done_folders = [f.strip() for f in done_folders]
    for folder in folders:
        if folder not in done_folders:
            convert_text_to_audio(folder)
            create_reel(folder)
            with open("done.txt", "a") as f:
                f.write(folder + "\n")
