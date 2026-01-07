# yt — Opinionated YouTube Downloader (MP3 / MP4)

`yt` is a **minimal, opinionated command-line tool** built on top of `yt-dlp` that lets you download **highest-quality MP3 audio or MP4 video** using a single, clean command.

This project focuses on **automation, safety, and sane defaults** — not on bypassing platform rules or encouraging misuse.

---

## ✨ Key Features

- Single unified command:
  ```bash
  yt mp3 <url>
  yt mp4 <url>
  ```
- Always highest available quality
- Audio format locked to **MP3**
- Video format locked to **MP4**
- Automatic playlist detection & download
- Metadata embedding (title, artist, album, thumbnail)
- Smart output folder structure
- Auto-resume for interrupted downloads
- Overwrite protection (safe by default)
- Windows-safe filenames
- No configuration required

---

## 📁 Output Structure

Downloads are automatically organized as follows:

```
Downloads/
├── Audio/
│   └── Uploader/
│       └── Playlist Name/
│           └── Video Title.mp3
└── Video/
    └── Uploader/
        └── Playlist Name/
            └── Video Title.mp4
```

- Single (non-playlist) videos are placed inside a `Single` folder.
- Filenames are sanitized for Windows compatibility.

---

## 📦 Requirements

You must install the following dependencies **yourself**:

- **Python** 3.9 or newer
- **yt-dlp**
- **ffmpeg**

> This project does **not** bundle, redistribute, or modify third‑party binaries.

---

## 🔧 Installation

1. Clone or download this repository
2. Install dependencies:
   ```bash
   pip install -U yt-dlp
   ```
3. Install `ffmpeg` and ensure it is available in your PATH
4. Place `yt.py` and `yt.bat` in a folder included in your PATH
5. Verify installation:
   ```bash
   yt mp3 <url>
   ```

---

## ▶ Usage

Download audio:
```bash
yt mp3 https://www.youtube.com/watch?v=VIDEO_ID
```

Download video:
```bash
yt mp4 https://www.youtube.com/watch?v=VIDEO_ID
```

Download playlists:
```bash
yt mp3 <playlist-url>
yt mp4 <playlist-url>
```

Multiple URLs are also supported in a single command.

---

## 🧠 Design Philosophy

This tool is intentionally **opinionated**:

- No format selection flags
- No quality tuning options
- No GUI
- No background services

If you require fine-grained control, advanced filters, or experimental options, you should use `yt-dlp` directly.

---

## ⚠️ Legal & Ethical Notice (IMPORTANT)

This software is provided **for educational and personal use only**.

You are solely responsible for:
- How you use this tool
- What content you download
- Ensuring compliance with:
  - YouTube Terms of Service
  - Copyright laws applicable in your country
  - Platform-specific usage policies

The author **does not encourage, endorse, or support**:
- Copyright infringement
- Downloading content without proper authorization
- Circumventing paywalls, DRM, or access controls
- Redistributing protected or licensed material

---

## 🚫 Disclaimer of Liability

This project is provided **"as is"**, without warranty of any kind.

The author:
- Assumes **no responsibility** for misuse
- Is **not liable** for legal consequences arising from usage
- Does **not guarantee** continued compatibility with YouTube or any other platform

By using this software, **you accept full responsibility** for your actions.

---

## 📜 License

This project is released under the **MIT License**.

You are free to:
- Use
- Modify
- Distribute

As long as the original license and copyright notice are preserved.

---

## 🛠️ Credits

This project is built on top of the following open-source tools:

- yt-dlp — media extraction logic
- ffmpeg — media processing

All credit for extraction and download capabilities belongs to the upstream projects.

---

## 🔮 Future Roadmap (Optional)

- Channel watch mode
- Smart deduplication
- Chapter-based audio splitting
- Plugin system

---

## ❗ Final Note

This project exists to demonstrate **clean CLI design, automation, and safe defaults**.

It is **not intended** to replace or compete with `yt-dlp`.

If you find this tool useful, please consider supporting the original projects.
