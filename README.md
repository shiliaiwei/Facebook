# Facebook Tools Suite

A small Python command-line tool that can download public Facebook videos, find a profile numeric ID, and print video details.

## What it does

- Download a Facebook video to your local Videos folder (uses yt-dlp)
- Find a user's numeric Facebook ID from a username or profile URL
- Display video details for a Facebook video URL (uses yt-dlp JSON output)

## How it works

- Menu-based CLI with three options.
- Download: runs yt-dlp via subprocess and saves to ~/Videos.
- ID lookup: fetches the profile page and extracts userID with a regex.
- Video details: runs yt-dlp --dump-json and prints selected fields.

## How to use

1. Install Python 3
2. Install dependencies:
   pip install yt-dlp requests pyfiglet colorama
3. Run:
   python fb_tools.py
4. Pick an option (1 to 3) and follow the prompts.

## Where you can use it

Run it locally on Windows, macOS, or Linux in a terminal.

## Notes

Educational use only. You are responsible for complying with Facebook terms and local laws.

## Owner

GitHub user shiliaiwei: https://github.com/shiliaiwei
