# Facebook Tools Suite

A command-line Python toolkit that provides three utilities for interacting with Facebook content: downloading videos, finding user IDs, and looking up video details.

## What It Does

The script runs an interactive menu in the terminal. The user picks one of three tools and follows the prompts. No configuration file is needed. All output appears directly in the terminal.

Tool 1 - Download Facebook Video: The user provides a Facebook video URL. The script calls yt-dlp internally to download the video and saves it to a Videos folder in the user's home directory. The folder is created automatically if it does not exist.

Tool 2 - Find Facebook User ID: The user provides a Facebook username or profile URL. The script sends an HTTP GET request to that profile page with the requests library, then uses a regular expression to extract the numeric userID value embedded in the page source. The numeric ID is printed to the terminal.

Tool 3 - Lookup Video Details: The user provides a Facebook video URL. The script calls yt-dlp with the --dump-json flag to retrieve structured metadata for the video, parses the JSON response, and prints the title, uploader, upload date, duration, view count, available formats, thumbnail URL, and description.

## How It Works

The script is built entirely in Python. It uses the subprocess module to run yt-dlp as an external process, the requests module to fetch web pages, the re module for regular-expression matching, and the json module to parse yt-dlp output. The colorama library adds color to terminal output and pyfiglet renders the ASCII art logo on startup. The main loop shows the menu after each tool finishes and exits when the user chooses option 4 or presses q.

## Requirements

- Python 3.7 or later
- yt-dlp (install with: pip install yt-dlp)
- requests (install with: pip install requests)
- colorama (install with: pip install colorama)
- pyfiglet (install with: pip install pyfiglet)

## How to Use

1. Install the required packages listed above.
2. Run the script: python fb_tools.py
3. The EIRSVi logo appears and the main menu is displayed.
4. Enter a number from 1 to 4 to select a tool.
5. Follow the on-screen prompt to enter a URL or username.
6. After each tool finishes, press Enter to return to the menu or q to quit.

Example for downloading a video:
- Select option 1
- Paste the Facebook video URL when prompted
- The downloaded file appears in ~/Videos/

Example for finding a user ID:
- Select option 2
- Enter zuck or https://www.facebook.com/zuck
- The numeric Facebook ID is printed

Example for video details:
- Select option 3
- Paste a Facebook video URL that contains /videos/ in the path
- Metadata such as title, duration, and view count is printed

## Where to Use It

This tool runs on any system that supports Python 3 and a terminal: Linux, macOS, and Windows. It is intended for local use on a personal machine. It does not run as a server and does not expose any network interface.

## Why Use It

Facebook does not provide an official public API for downloading videos or retrieving user IDs from profile pages. This tool automates the manual steps a user would otherwise do in a browser, making the process faster and scriptable from the command line.

## Owner

Script authored and maintained by EIRSVi.

Repository maintained by shiliaiwei. GitHub profile: https://github.com/shiliaiwei

## Disclaimer

This tool is for educational purposes only. Users are responsible for complying with Facebook's terms of service and applicable laws when using this tool.
