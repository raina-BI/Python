# Automate File Segregation

This Python program automates the process of segregating files into specific folders based on their file type. It monitors a designated directory for new files and categorizes them into folders such as images, videos, audio files, and documents.

---

## Features
- Monitors a folder (e.g., `Downloads`) for newly added files.
- Automatically moves files to categorized directories based on their extensions or MIME types.
- Supports the following categories:
  - **Image Files**: `.jpg`, `.jpeg`, `.png`
  - **Video Files**: `.mp4`, `.mov`, `.avi`
  - **Audio Files**: `.mp3`, `.wav`
  - **Document Files**: `.ppt`, `.csv`, `.pdf`, `.txt`
- Creates new directories dynamically if they do not exist.

---

## Requirements
- Python 3.x
- The following Python libraries:
  - `os`
  - `shutil`
  - `time`
  - `magic` (for MIME type detection)
  - `watchdog` (for file monitoring)

Install required libraries:
```bash
pip install python-magic watchdog
