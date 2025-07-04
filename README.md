# Flask Video Reel Generator

A Flask web application that generates vertical video reels by combining user-uploaded images with AI-generated speech from a text description. The app converts the description text to audio using the Murf API, merges it with images using FFmpeg, and produces a shareable video reel similar to Instagram Reels.

---

## Features

- Upload multiple images along with a short text description.
- Automatically convert text to speech using Murf AI.
- Create a vertical video reel (1080x1920) with synchronized audio.
- View all generated reels in a gallery.
- Unique uploads handled via UUID for isolation.

---

## Tech Stack & Libraries

- **Backend:** Python 3.x, Flask
- **Text-to-Speech:** Murf AI (via Murf Python SDK)
- **Video Processing:** FFmpeg
- **Utilities:** uuid, werkzeug (for secure file upload), requests, subprocess
- **Frontend:** HTML templates rendered with Flask (`index.html`, `create.html`, `gallery.html`)

  ------END-----

