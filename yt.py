import sys
import subprocess
import shutil

def usage():
    print("""
Usage:
  yt mp3 <url>
  yt mp4 <url>

Rules:
  • Audio format: MP3 (highest quality)
  • Video format: MP4 (highest quality)
  • Playlists supported automatically
  • Metadata & thumbnails embedded
""")
    sys.exit(1)

if len(sys.argv) < 3:
    usage()

mode = sys.argv[1].lower()
urls = sys.argv[2:]

if mode not in ("mp3", "mp4"):
    print("Invalid mode. Use 'mp3' or 'mp4'.")
    sys.exit(1)

# Ensure yt-dlp exists
if not shutil.which("yt-dlp"):
    print("yt-dlp not found in PATH")
    sys.exit(1)

# Base command (shared)
cmd = [
    "yt-dlp",
    "--newline",
    "--progress",
    "--progress-template",
    "%(progress._percent_str)s | %(progress._speed_str)s | ETA %(progress._eta_str)s",
    "--continue",                 # auto-resume
    "--no-overwrites",             # overwrite protection
    "--embed-metadata",
    "--embed-thumbnail",
    "--add-metadata",
    "--restrict-filenames",
    "--windows-filenames",
]

if mode == "mp3":
    cmd += [
        "-f", "bestaudio",
        "-x",
        "--audio-format", "mp3",
        "--audio-quality", "0",
        "-o", "Downloads/Audio/%(uploader)s/%(playlist_title|Single)s/%(title)s.%(ext)s",
    ]

elif mode == "mp4":
    cmd += [
        "-f", "bv*+ba/b",
        "--merge-output-format", "mp4",
        "-o", "Downloads/Video/%(uploader)s/%(playlist_title|Single)s/%(title)s.%(ext)s",
    ]

cmd.extend(urls)

# Execute
subprocess.run(cmd)
