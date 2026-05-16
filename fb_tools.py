import subprocess
import os
import pyfiglet
from colorama import Fore, init
import time
import requests
import re
import json
import argparse
import shutil

# Initialize Colorama
init(autoreset=True)

def print_colored_logo():
    """Generate and display the EIRSVi logo with color effects."""
    # Generate ASCII art for the logo "EIRSVi"
    logo = pyfiglet.figlet_format("EIRSVi", font="slant")
    
    # Center the logo in the terminal
    terminal_width = shutil.get_terminal_size().columns
    centered_logo = "\n".join(line.center(terminal_width) for line in logo.splitlines())

    # Colors for the gradient effect (cyber-like appearance)
    colors = [Fore.LIGHTCYAN_EX, Fore.CYAN, Fore.MAGENTA, Fore.LIGHTMAGENTA_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTBLUE_EX]

    # Apply a glowing effect to each character in the logo
    print("\n")  # Add spacing before the logo
    for i, char in enumerate(centered_logo):
        if char.strip():  # Apply color only to non-space characters
            print(colors[i % len(colors)] + char, end='', flush=True)
            time.sleep(0.01)  # Slight delay to create a glowing effect
        else:
            print(char, end='', flush=True)
    print("\n")  # New line after the logo

def print_welcome():
    """Display welcome message and tool information."""
    # Call the function to print the colored EIRSVi logo
    print_colored_logo()
    
    # Welcome message
    welcome_message = f"{Fore.LIGHTBLUE_EX}Welcome to the Facebook Tools Suite! \n"
    terminal_width = shutil.get_terminal_size().columns
    centered_message = welcome_message.center(terminal_width)
    print(centered_message)

    # Updated GitHub and social links
    developer_info = f"Support us {Fore.LIGHTGREEN_EX}@eirsvi "
    centered_developer = developer_info.center(terminal_width)
    print(centered_developer)

    social_links = f"{Fore.LIGHTRED_EX} GitHub | X | YouTube \n"
    centered_social_links = social_links.center(terminal_width)
    print(centered_social_links)
    
    print()  # Add an extra newline for spacing

def create_videos_directory():
    """Create a Videos directory in the user's home folder if it doesn't exist."""
    # Get the user's home directory (works on both Windows and Linux)
    home_dir = os.path.expanduser("~")
    
    # Create the Videos directory path
    videos_dir = os.path.join(home_dir, "Videos")
    
    # Create the directory if it doesn't exist
    if not os.path.exists(videos_dir):
        try:
            os.makedirs(videos_dir)
            print(f"{Fore.LIGHTGREEN_EX}Created Videos directory at: {videos_dir}")
        except Exception as e:
            print(f"{Fore.LIGHTRED_EX}Error creating Videos directory: {e}")
            # Fall back to home directory if Videos can't be created
            videos_dir = home_dir
    
    return videos_dir

def format_profile_url(profile_input):
    """Format the profile input into a proper Facebook URL."""
    # Check if it's already a full URL
    if profile_input.startswith(("http://", "https://")):
        return profile_input
    else:
        # It's just a username, convert to a profile URL
        return f"https://www.facebook.com/{profile_input}"

# Function 1: Download Facebook Videos
def download_video():
    """Download videos from Facebook."""
    print(f"\n{Fore.LIGHTBLUE_EX}=== Facebook Video Downloader ===")
    print(f"{Fore.YELLOW}This tool downloads videos from Facebook URLs or profiles.")
    print(f"{Fore.YELLOW}Example URL: {Fore.LIGHTYELLOW_EX}https://www.facebook.com/zuck/videos/10101858403890501")
    
    # Create Videos directory and get its path
    videos_dir = create_videos_directory()
    
    # Prompt user for the video URL
    url = input(f"\n{Fore.LIGHTCYAN_EX}Enter the FB video URL: {Fore.RESET}").strip()

    if not url:
        print(f"{Fore.LIGHTRED_EX}Error: No URL provided.")
        return

    # Generate the output file name in the Videos directory
    output_file = os.path.join(videos_dir, '%(title)s.%(ext)s')

    try:
        # Command to download video using yt-dlp
        print(f"{Fore.YELLOW}Downloading video to: {videos_dir}")
        subprocess.run(['yt-dlp', '-o', output_file, url], check=True)
        print(f"{Fore.LIGHTGREEN_EX}Video downloaded successfully to {Fore.LIGHTYELLOW_EX}{videos_dir}")
    except subprocess.CalledProcessError as e:
        print(f"{Fore.LIGHTRED_EX}Error downloading video: {e}")
    except FileNotFoundError:
        print(f"{Fore.LIGHTRED_EX}Error: yt-dlp not found. Please install it with 'pip install yt-dlp'")

# Function 2: Find Facebook User ID
def find_facebook_id():
    """Find a Facebook user ID from username or profile URL."""
    print(f"\n{Fore.LIGHTBLUE_EX}=== Facebook ID Finder ===")
    print(f"{Fore.YELLOW}This tool finds the numeric ID of a Facebook user from their username or profile URL.")
    print(f"{Fore.YELLOW}Example: {Fore.LIGHTYELLOW_EX}zuck {Fore.RESET}or {Fore.LIGHTYELLOW_EX}https://www.facebook.com/zuck")
    
    # Prompt for username or URL
    username_input = input(f"\n{Fore.LIGHTCYAN_EX}Enter FB username or profile URL: {Fore.RESET}").strip()
    
    if not username_input:
        print(f"{Fore.LIGHTRED_EX}Error: No username or profile URL provided.")
        return

    # Extract username from URL if needed
    if "facebook.com/" in username_input:
        username = username_input.split("facebook.com/")[1].split("/")[0].split("?")[0]
    else:
        username = username_input
    
    # Construct the full Facebook URL
    url = f"https://www.facebook.com/{username}"

    try:
        # FB Identification
        print(f"{Fore.YELLOW}Fetching profile details, please wait...")
        byte_obj = b'"userID":"([0-9]+)"'
        id_req = re.compile(byte_obj)
        page = requests.get(url)
        fb_list = id_req.findall(page.content)

        if fb_list:
            # Decoding the user ID from the list of bytes
            fbid = fb_list[0].decode()
            print(f"\n{Fore.LIGHTGREEN_EX}[*] The Facebook ID for {Fore.LIGHTYELLOW_EX}{username}{Fore.LIGHTGREEN_EX} is: {Fore.LIGHTYELLOW_EX}{fbid}")
        else:
            print(f"\n{Fore.LIGHTRED_EX}[!] No Facebook ID found. Check if the username is correct.")
    except Exception as e:
        print(f"\n{Fore.LIGHTRED_EX}[!] Error: {e}")

# Function 3: Lookup Video Details
def lookup_video_details():
    """Lookup and display details about a Facebook video."""
    print(f"\n{Fore.LIGHTBLUE_EX}=== Facebook Video Details Lookup ===")
    print(f"{Fore.YELLOW}This tool fetches and displays detailed information about Facebook videos.")
    print(f"{Fore.YELLOW}Example URL: {Fore.LIGHTYELLOW_EX}https://www.facebook.com/zuck/videos/10101858403890501")
    
    # Prompt for video URL
    url = input(f"\n{Fore.LIGHTCYAN_EX}Enter the Facebook video URL to lookup details: {Fore.RESET}").strip()

    if not url:
        print(f"{Fore.LIGHTRED_EX}Error: No URL provided.")
        return

    # Validate that the URL is a video URL
    if not any(k in url for k in ["/videos/", "/watch", "/reel/"]):
        print(f"{Fore.LIGHTRED_EX}Error: The URL provided does not appear to be a valid Facebook video URL.")
        print(f"{Fore.YELLOW}A valid Facebook video URL should contain '/videos/', '/watch', or '/reel/' in the path.")
        print(f"{Fore.YELLOW}Example: https://www.facebook.com/username/videos/123456789")
        return

    # Use yt-dlp to fetch video details in JSON format
    try:
        print(f"{Fore.YELLOW}Fetching video details, please wait...")
        
        # Use --no-playlist to ensure we only get info for the specific video
        result = subprocess.run([
            'yt-dlp', '--dump-json', '--no-playlist', url
        ], capture_output=True, text=True, check=True)

        # Check if we got any output
        if not result.stdout.strip():
            print(f"{Fore.LIGHTRED_EX}Error: No data returned for this video. It may be private or unavailable.")
            return

        video_details = json.loads(result.stdout)

        # Extract relevant details
        title = video_details.get("title", "N/A")
        uploader = video_details.get("uploader", "N/A")
        upload_date = video_details.get("upload_date", "N/A")
        duration = video_details.get("duration_string", "N/A")
        view_count = video_details.get("view_count", "N/A")
        description = video_details.get("description", "N/A")
        thumbnail = video_details.get("thumbnail", "N/A")
        formats = video_details.get("formats", [])
        
        # Get available formats/qualities
        available_formats = []
        if formats:
            for fmt in formats:
                if fmt.get("format_note") and fmt.get("ext"):
                    format_info = f"{fmt.get('format_note')} ({fmt.get('ext')})"
                    if format_info not in available_formats:
                        available_formats.append(format_info)

        # Format upload date if available
        if upload_date != "N/A" and len(upload_date) == 8:
            upload_date = f"{upload_date[0:4]}-{upload_date[4:6]}-{upload_date[6:8]}"

        # Print video details in a formatted table
        print(f"\n{Fore.LIGHTBLUE_EX}Video Details:")
        print("-" * 60)
        print(f"{Fore.LIGHTGREEN_EX}{'Title':<15}:{Fore.RESET} {title}")
        print(f"{Fore.LIGHTGREEN_EX}{'Uploader':<15}:{Fore.RESET} {uploader}")
        print(f"{Fore.LIGHTGREEN_EX}{'Upload Date':<15}:{Fore.RESET} {upload_date}")
        print(f"{Fore.LIGHTGREEN_EX}{'Duration':<15}:{Fore.RESET} {duration}")
        print(f"{Fore.LIGHTGREEN_EX}{'View Count':<15}:{Fore.RESET} {view_count}")
        print(f"{Fore.LIGHTGREEN_EX}{'Thumbnail URL':<15}:{Fore.RESET} {thumbnail}")
        
        # Print available formats if any
        if available_formats:
            print(f"{Fore.LIGHTGREEN_EX}{'Available Formats':<15}:{Fore.RESET}")
            for fmt in available_formats:
                print(f"  - {fmt}")
        
        # Print description with proper formatting
        print(f"{Fore.LIGHTGREEN_EX}{'Description':<15}:{Fore.RESET}")
        if description != "N/A":
            # Wrap description text for better readability
            for line in description.split('\n'):
                print(f"  {line}")
        else:
            print("  N/A")
        print("-" * 60)

    except subprocess.CalledProcessError as e:
        print(f"{Fore.LIGHTRED_EX}Error fetching video details: {e}")
        
        # Provide more helpful error messages based on common issues
        if "This video is unavailable" in str(e.stderr):
            print(f"{Fore.YELLOW}The video may be private, deleted, or not accessible.")
        elif "Unsupported URL" in str(e.stderr):
            print(f"{Fore.YELLOW}The URL format is not supported. Make sure it's a direct Facebook video URL.")
        elif "Unable to extract" in str(e.stderr):
            print(f"{Fore.YELLOW}Unable to extract video information. The video might be protected or the URL is incorrect.")
        
        # Suggest a solution
        print(f"{Fore.CYAN}Try using a direct link to a Facebook video that contains '/videos/' in the URL.")
        print(f"{Fore.CYAN}Example: https://www.facebook.com/username/videos/123456789")
        
    except json.JSONDecodeError as e:
        print(f"{Fore.LIGHTRED_EX}Error decoding video details: {e}")
        print(f"{Fore.YELLOW}The response from Facebook couldn't be properly parsed.")
    except FileNotFoundError:
        print(f"{Fore.LIGHTRED_EX}Error: yt-dlp not found. Please install it with 'pip install yt-dlp'")
    except Exception as e:
        print(f"{Fore.LIGHTRED_EX}Unexpected error: {e}")
        print(f"{Fore.YELLOW}Please check your internet connection and try again.")

def display_menu():
    """Display the main menu and get user choice."""
    print(f"\n{Fore.LIGHTBLUE_EX}=== Facebook Tools Menu ===")
    print(f"{Fore.CYAN}1. {Fore.RESET}Download Facebook Video")
    print(f"{Fore.CYAN}2. {Fore.RESET}Find Facebook User ID")
    print(f"{Fore.CYAN}3. {Fore.RESET}Lookup Video Details")
    print(f"{Fore.CYAN}4. {Fore.RESET}Exit")
    
    while True:
        try:
            choice = input(f"\n{Fore.LIGHTCYAN_EX}Enter your choice (1-4) or 'q' to quit: {Fore.RESET}").strip()
            if choice.lower() in ['q', 'quit', 'exit']:
                return 4
            choice = int(choice)
            if 1 <= choice <= 4:
                return choice
            else:
                print(f"{Fore.LIGHTRED_EX}Invalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            print(f"{Fore.LIGHTRED_EX}Invalid input. Please enter a number or 'q' to quit.")

def main():
    """Main function to run the Facebook Tools Suite."""
    # Display welcome message
    print_welcome()
    
    while True:
        # Display menu and get user choice
        choice = display_menu()
        
        # Execute the chosen function
        if choice == 1:
            download_video()
        elif choice == 2:
            find_facebook_id()
        elif choice == 3:
            lookup_video_details()
        elif choice == 4:
            print(f"\n{Fore.LIGHTGREEN_EX}Thank you for using Facebook Tools Suite! Goodbye!")
            break
        
        # Ask if the user wants to continue
        continue_choice = input(f"\n{Fore.LIGHTCYAN_EX}Press Enter to return to the main menu or 'q' to quit: {Fore.RESET}").strip()
        if continue_choice.lower() == 'q':
            print(f"\n{Fore.LIGHTGREEN_EX}Thank you for using Facebook Tools Suite! Goodbye!")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Fore.LIGHTRED_EX}Program interrupted by user. Exiting...")
    except Exception as e:
        print(f"\n{Fore.LIGHTRED_EX}An unexpected error occurred: {e}") 