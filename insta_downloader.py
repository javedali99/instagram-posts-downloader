"""

A script to download Instagram posts from a specified user account using the Instaloader module.

Author: Javed Ali (javedali28@gmail.com)
Date: April 2, 2024

This script provides a straightforward way to download all posts (images and videos) from a specified Instagram user account. 
It utilizes the Instaloader library to interface with Instagram, fetching and downloading posts directly to the local filesystem.

Usage:
    1. Install Instaloader if you haven't already: `pip install instaloader`
    2. Modify the 'username' variable in the __main__ section to the target Instagram username.
    3. Execute this script with Python.

Requirements:
    - Python 3.x
    - Instaloader

License:
    - MIT License

NOTE: This script is intended for educational and personal use. Please respect the privacy and copyright of Instagram users and comply with Instagram's terms of use.

"""

import instaloader

def download_instagram_posts(username):
    """
    Downloads all posts from the specified Instagram user account.

    Attempts to download all Instagram posts from the given username. It handles several common issues,
    including non-existent profiles and private profiles. For private profiles, the user running the script
    must be an approved follower and logged in via Instaloader.

    Parameters:
    - username (str): The username of the Instagram account from which to download posts.

    Exceptions:
    - ProfileNotExistsException: Raised if the specified username does not exist.
    - PrivateProfileNotFollowedException: Raised if the profile is private and the user is not followed.
    - Exception: Catches other general exceptions that may occur.

    Returns:
    - None
    """
    # Create an instance of the Instaloader class
    L = instaloader.Instaloader()

    try:
        # Attempt to load the profile using the given username
        profile = instaloader.Profile.from_username(L.context, username)

        # Iterate through and download all posts from the profile
        for post in profile.get_posts():
            L.download_post(post, target=profile.username)
        print(f"Successfully downloaded all posts from {username}.")

    # Handle case where the profile does not exist
    except instaloader.exceptions.ProfileNotExistsException:
        print(f"The profile {username} does not exist. Please check the username and try again.")
    # Handle case where the profile is private and the user is not followed
    except instaloader.exceptions.PrivateProfileNotFollowedException:
        print(f"The profile {username} is private. You need to follow this account and login with your Instagram credentials.")
    # Handle other general exceptions
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # The Instagram account you want to download pictures from. Replace 'username_here' with the actual username.
    username = 'username_here'
    download_instagram_posts(username)
