"""
A script to download all pictures from an Instagram account.

Author: Javed Ali 
Email: javedali28@gmail.com
Date: April 2, 2024

This script allows users to download all posts (images and videos) from a specified Instagram
profile, whether public or private. For private profiles, the user must provide their own
Instagram credentials and must have been granted access to the private profile.

The script prompts the user for the Instagram username they wish to download content from.
If the profile is private, the user is asked if they need to log in and, if so, to provide
their Instagram username and password.

The script then uses the instaloader library to download all posts from the specified profile
into a folder named after the username in the current working directory.

Requirements:
- Python 3.x
- instaloader module (install with `pip install instaloader`)

Features:
- Supports downloading from public and private Instagram profiles.
- Requires user login for accessing private profiles, with support for two-factor authentication.
- Provides informative error messages for common issues like bad credentials or non-existent profiles.

Usage:
1. Ensure Python 3.x and Instaloader are installed on your system.
2. Run the script in a terminal or command prompt.
3. Follow the on-screen prompts to enter the target Instagram username and login credentials if necessary.

License: MIT License

NOTE: This script is intended for educational and personal use. Please respect the privacy and copyright of Instagram users and comply with Instagram's terms of use.
"""

# Import all required libraries
import instaloader
import getpass
import sys
import os

def get_credentials():
    """
    Prompts the user for their Instagram login credentials.

    Returns:
        tuple: A tuple containing the user's Instagram username and password.
    """
    username = input("Enter your Instagram username: ").strip()
    password = getpass.getpass("Enter your Instagram password: ").strip()
    return username, password

def download_posts(loader, profile):
    """
    Downloads all posts from the given Instagram profile using the specified loader.

    Args:
        loader (instaloader.Instaloader): An instance of the Instaloader class.
        profile (instaloader.Profile): The Instagram profile to download posts from.
    """
    # Create a directory with the same name as the Instagram profile
    os.makedirs(profile.username, exist_ok=True)
    
    # Download all posts from the profile
    for post in profile.get_posts():
        loader.download_post(post, target=profile.username)

def main():
    """
    The main function that orchestrates the entire process of downloading Instagram posts.
    """
    # Create an instance of the Instaloader class
    loader = instaloader.Instaloader()

    # Prompt for the Instagram profile to download from
    target_profile = input("Enter the Instagram username to download posts from: ").strip()

    # Check if the user wants to log in (required for private profiles)
    login_choice = input("Do you need to log in to download posts? (yes/no): ").strip().lower()
    
    if login_choice == 'yes':
        # Get the user's Instagram login credentials
        username, password = get_credentials()
        
        try:
            # Attempt to log in to Instagram
            loader.login(username, password)
            print("Login successful!")
        except instaloader.exceptions.BadCredentialsException:
            print("Error: Invalid Instagram username or password.")
            sys.exit(1)
        except instaloader.exceptions.TwoFactorAuthRequiredException:
            print("Error: Two-factor authentication is required.")
            sys.exit(1)
        except instaloader.exceptions.InvalidArgumentException:
            print("Error: Invalid argument provided.")
            sys.exit(1)
    
    try:
        # Retrieve the Instagram profile using the given username
        profile = instaloader.Profile.from_username(loader.context, target_profile)
        
        # Download all posts from the profile
        download_posts(loader, profile)
        
        print(f"All posts downloaded successfully from the profile: {target_profile}")
        
    except instaloader.exceptions.ProfileNotExistsException:
        print(f"Error: The profile '{target_profile}' does not exist.")
        
    except instaloader.exceptions.PrivateProfileNotFollowedException:
        print(f"Error: The profile '{target_profile}' is private and requires following.")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
