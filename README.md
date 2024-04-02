<p align="center">
    <img src="https://github.com/javedali99/instagram-posts-downloader/assets/15319503/232a67f6-49fc-48e4-85ff-c8526d54256b" alt="disaster" width="150" height="150">
  </a>
  <h1 align="center">Instagram Posts Downloader</h1>
</p>

<br>


The `insta_posts_downloader` is a Python script that allows you to easily download all posts, including images and videos, from any Instagram profile. Whether you want to backup your own Instagram content or save posts from your favorite influencers or friends, this script provides a convenient solution.

The main purpose of this script is to simplify the process of downloading Instagram posts in bulk. Instead of manually saving each post one by one, you can use this script to automate the download process and save time. This can be particularly useful in various scenarios, such as:

- Backing up your own Instagram posts for safekeeping
- Archiving posts from a specific Instagram profile for reference or analysis
- Collecting images and videos from Instagram for personal or professional projects

## Features

The Instagram Posts Downloader script comes with the following key features:

1. **Support for Public and Private Profiles**: The script allows you to download posts from both public and private Instagram profiles. For private profiles, you need to provide your own Instagram credentials and ensure that you have been granted access to the profile.

2. **Bulk Download**: With this script, you can download all posts from an Instagram profile at once, saving you the effort of manually downloading each post individually.

3. **Easy-to-Use Interface**: The script provides a user-friendly command-line interface that guides you through the process of entering the necessary information, such as the Instagram username and your login credentials (if required).

4. **Organized Download**: The downloaded posts are automatically saved in a directory named after the Instagram profile, keeping your downloads organized and easily accessible.

5. **Error Handling**: The script includes robust error handling to deal with common issues that may arise during the download process, such as invalid credentials, private profiles, or network errors. Informative error messages are provided to help you troubleshoot any problems.


## Requirements

To set up the Instagram Photo Downloader on your system, follow these steps:

- Python 3.10+
- `instaloader` module 

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/javedali99/instagram-posts-downloader.git
   ```

2. Navigate to the project directory:

   ```bash
   cd instagram-posts-downloader
   ```

3. Install the required dependencies:

   ```bash
   pip install instaloader
   ```

## Usage

Using the Instagram Posts Downloader script is straightforward. Simply follow these steps:

1. Run the script using Python:

   ```bash
   python insta_posts_downloader.py
   ```

2. When prompted, enter the Instagram username of the profile you want to download posts from:

   ```
   Enter the Instagram username to download posts from: username_here
   ```

3. If the profile is private and you need to log in to download posts, enter "yes" when prompted:

   ```
   Do you need to log in to download posts? (yes/no): yes
   ```

4. If you choose to log in, enter your Instagram username and password when prompted:

   ```
   Enter your Instagram username: your_username
   Enter your Instagram password: your_password
   ```

5. The script will start downloading all posts from the specified profile into a directory with the same name as the Instagram username.

6. Once the download is complete, you will see a success message:

   ```
   All posts downloaded successfully from the profile: username_here
   ```

## Notes

- This script is intended for educational purposes and should be used in compliance with Instagram's terms of service.
- Remember to use this script responsibly and always respect the privacy and intellectual property rights of others when downloading content from Instagram.
- Do not download or redistribute content without permission.
- Unauthorized use or distribution of downloaded content is strictly prohibited.
- If you encounter any issues or have questions, please open an issue on the GitHub repository.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

<!--
## Citations:
> Ali, J. (2024). Instagram posts downloader [Computer software]. GitHub. https://github.com/javedali99/instagram-posts-downloader
-->
