import os
import requests
from murf import Murf
from playsound import playsound  # optional, platform-dependent
from dotenv import load_dotenv
load_dotenv()
def text_to_speech(text, folder):
    # Set up Murf client
    api_key=os.getenv("api_key")
    client = Murf(api_key=api_key)

    # Generate speech
    res = client.text_to_speech.generate(
        text=text,
        voice_id="en-US-terrell",
    )

    # Save to user folder
    folder_name = f"user_uploads/{folder}"
    file_name = "audio.mp3"
    # os.makedirs(folder_name, exist_ok=True)

    audio_url = res.audio_file
    response = requests.get(audio_url)

    save_path = os.path.join(folder_name, file_name)
    with open(save_path, "wb") as f:  # <-- FIXED
        f.write(response.content)

    # print(f"Saved audio to: {save_path}")

    # # Optional: play the audio
    # try:
    #     playsound(save_path)
    # except Exception as e:
    #     print(f"Audio playback failed: {e}")

# Example test
# text_to_speech("i am pranav yes i am", "28cf4b7e-5755-11f0-bee9-d61bd5b9ad02")
