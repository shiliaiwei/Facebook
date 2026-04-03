# Facebook Tools Suite

## Summary

Facebook Tools Suite is a Python-based command-line application that provides three essential utilities for Facebook content interaction. The script uses yt-dlp for video operations and web scraping techniques for ID extraction. It offers a menu-driven interface with colorful terminal output powered by colorama and pyfiglet libraries.

## How It Works

The application operates through a main menu system that executes three core functions:

1. **Video Downloader**: Uses yt-dlp subprocess calls to download Facebook videos from provided URLs. The downloaded files are automatically saved to the user's Videos directory with original titles and formats preserved.

2. **ID Finder**: Performs HTTP requests to Facebook profile pages and uses regex pattern matching to extract numeric user IDs from the page HTML content. It searches for the userID field in the page source and returns the numeric identifier.

3. **Video Details Lookup**: Executes yt-dlp in JSON dump mode to retrieve comprehensive metadata about Facebook videos including title, uploader, upload date, duration, view count, available formats, description, and thumbnail URL.

The script initializes with a colorized ASCII art logo display and maintains a continuous loop until the user chooses to exit.

## How to Use

### Installation Requirements

Install required dependencies before running:

```bash
pip install pyfiglet colorama requests yt-dlp
```

### Running the Application

Execute the script from command line:

```bash
python fb_tools.py
```

### Menu Options

After launching, select from four options:

**Option 1 - Download Facebook Video**
- Select option 1 from the menu
- Enter the complete Facebook video URL
- Video downloads automatically to your Videos folder
- Example URL format: https://www.facebook.com/username/videos/123456789

**Option 2 - Find Facebook User ID**
- Select option 2 from the menu
- Enter either a Facebook username or complete profile URL
- The numeric Facebook ID displays in the terminal
- Example inputs: "zuck" or "https://www.facebook.com/zuck"

**Option 3 - Lookup Video Details**
- Select option 3 from the menu
- Enter the Facebook video URL
- Displays comprehensive information including title, uploader, date, duration, views, formats, description, and thumbnail URL

**Option 4 - Exit**
- Terminates the application

Press Enter after each operation to return to the main menu or press 'q' to quit.

## Where to Use

This tool can be used in various scenarios:

- **Content Archiving**: Download Facebook videos for personal backup or offline viewing
- **Research and Analysis**: Gather video metadata for social media research projects
- **User Identification**: Find numeric Facebook IDs required for API calls or developer tools
- **Content Management**: Batch video information collection for content curation
- **Educational Purposes**: Learn about web scraping and API interaction techniques

The tool works on any system with Python installed including Windows, Linux, and macOS.

## Why Use This Tool

- **Convenience**: Single interface for multiple Facebook operations without browser navigation
- **Automation**: Command-line access enables scripting and batch processing capabilities
- **Information Access**: Retrieve video details not readily visible in the Facebook interface
- **Offline Access**: Download videos for viewing without internet connectivity
- **Developer Utility**: Obtain numeric user IDs needed for Facebook API development
- **Educational Value**: Demonstrates practical implementation of web scraping and subprocess management

## Technical Implementation

### Code Structure

The application consists of the following key functions:

- `print_colored_logo()`: Generates animated ASCII art display with gradient color effects
- `print_welcome()`: Shows welcome message and social media links
- `create_videos_directory()`: Creates Videos folder in user home directory if not exists
- `format_profile_url()`: Normalizes profile input to proper Facebook URL format
- `download_video()`: Handles video download operations using yt-dlp
- `find_facebook_id()`: Extracts numeric user ID through regex pattern matching
- `lookup_video_details()`: Retrieves and formats comprehensive video metadata
- `display_menu()`: Presents menu options and validates user input
- `main()`: Orchestrates the application flow and handles the event loop

### Dependencies

- **subprocess**: Executes external yt-dlp commands
- **os**: Handles file system operations and path management
- **pyfiglet**: Generates ASCII art for logo display
- **colorama**: Provides cross-platform colored terminal output
- **time**: Controls animation timing effects
- **requests**: Performs HTTP requests for ID extraction
- **re**: Executes regex pattern matching operations
- **json**: Parses video metadata from yt-dlp output
- **argparse**: Command-line argument parsing infrastructure

### External Tool

- **yt-dlp**: YouTube downloader fork supporting multiple platforms including Facebook

## Owner and Attribution

**Original Script Author**: EIRSVi (srievi@tuta.io)

**Repository Maintainer**: [shiliaiwei](https://github.com/shiliaiwei)

**Repository URL**: https://github.com/shiliaiwei/Facebook

## Support and Contact

- **GitHub**: [@eirsvi](https://github.com/eirsvi)
- **X (Twitter)**: [@eirsvi](https://twitter.com/eirsvi)
- **YouTube**: [EIRSVi Channel](https://youtube.com/eirsvi)

## Version Information

- **Current Version**: 1.0.0
- **Last Updated**: 2026-04-03

## Important Disclaimer

This tool is intended for educational and personal use only. Users must comply with Facebook's Terms of Service and respect intellectual property rights. The tool should not be used to download copyrighted content without proper authorization. Users are solely responsible for their actions and any legal consequences resulting from misuse of this software.

## License

This project is provided as-is for educational purposes. Users should review Facebook's terms of service and applicable copyright laws before using this tool.
