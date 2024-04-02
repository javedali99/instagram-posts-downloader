# Instagram Posts Downloader

The `instagram-posts-downloader` is a Python utility designed to facilitate the efficient downloading of Instagram posts, including images and videos, from publicly accessible or followed private user accounts. This script, developed with Python and leveraging the `Instaloader` module, offers a streamlined approach to archiving Instagram content from specified users directly to your local storage.

## Features

- **Easy to Use**: Simple setup and execution process.
- **Comprehensive Downloading**: Downloads all posts, including photos and videos, from the specified user account.
- **Robust Error Handling**: Gracefully handles common errors, such as non-existent profiles or access issues with private accounts.

## Prerequisites

Before deploying the Instagram Posts Downloader, ensure your system meets the following requirements:

- Python 3.x installed on your device.
- The Instaloader module installed in your Python environment. If not present, it can be installed via pip with the following command:

```bash
pip install instaloader
```

## Installation

To install the Instagram Posts Downloader, execute the following steps:

1. Clone the repository to your preferred local directory:

```bash
git clone https://github.com/javedali99/instagram-posts-downloader.git
```

2. Navigate into the cloned repository's directory:

```bash
cd instagram-posts-downloader
```

## Configuration and Usage

Follow these detailed steps to configure and utilize the Instagram Posts Downloader:

1. Open the `insta_downloader.py` script in a text editor of your choice.
2. Search for the line `username = 'username_here'`.
3. Replace `'username_here'` with the actual Instagram username of the profile from which you wish to download posts.
4. Save the modifications and close the editor.
5. Execute the script with the following command:

```bash
python insta_downloader.py
```

The script will commence the download process, saving all posts from the specified Instagram account into a directory named after the username, located in your current working directory.

## Exception Handling

The script includes advanced exception handling mechanisms to address and inform the user about potential issues:

- **ProfileNotExistsException**: Notifies the user if the specified Instagram username does not exist.
- **PrivateProfileNotFollowedException**: Alerts the user if the targeted profile is private and they haven't been granted access.
- **General Exceptions**: Catches and reports unforeseen errors, ensuring the user is informed of any issues during the execution process.

## Disclaimer

This tool is intended for educational and personal use only. Users should adhere to Instagram's Terms of Service and respect the privacy and copyright of the content owners. Unauthorized use or distribution of downloaded content is strictly prohibited.

