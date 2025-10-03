import yt_dlp
import os
import subprocess

# Ask user for video URL
url = input("Enter the YouTube video URL: ")

# Ask user for destination folder
destination = input("Enter the destination folder path (e.g., C:\\Users\\DELL\\Downloads): ")

# Make sure the folder exists
if not os.path.exists(destination):
    os.makedirs(destination)
    print(f"Created destination folder: {destination}")

# Function to check if ffmpeg is installed
def ffmpeg_installed():
    try:
        subprocess.run(["ffmpeg", "-version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except FileNotFoundError:
        return False

# Configure yt-dlp options based on ffmpeg availability
if ffmpeg_installed():
    print("ffmpeg detected. Downloading best quality video + audio with merging...")
    ydl_opts = {
        "outtmpl": os.path.join(destination, "%(title)s.%(ext)s"),
        "format": "bestvideo+bestaudio/best",
        "merge_output_format": "mp4"
    }
else:
    print(" ffmpeg not detected. Falling back to best single-file MP4 download...")
    ydl_opts = {
        "outtmpl": os.path.join(destination, "%(title)s.%(ext)s"),
        "format": "best[ext=mp4]"
    }

# Download video
try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print(f"Video downloaded successfully to '{destination}'!")
except Exception as e:
    print(" An error occurred while downloading.")
    print("Error details:", e)
