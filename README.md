# Internet Speed Twitter Bot

## Overview

This is a Python script that checks your internet speed using Speedtest.net and tweets at your internet service provider if the speed falls below the promised values.

## Prerequisites

- Python 3.x
- Selenium
- Chrome WebDriver
- Twitter Account

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/InternetSpeedTwitterBot.git
    ```

2. Install the required packages:

    ```bash
    pip install selenium
    ```

3. Download Chrome WebDriver and update the `PATH` variable with the location of the WebDriver.

## Usage

1. Open `main.py` and update the following variables:

    ```python
    PROMISED_DOWN = 100  # Replace with your promised download speed
    PROMISED_UP = 100    # Replace with your promised upload speed
    TWITTER_EMAIL = "your_twitter_email@example.com"    # Replace with your Twitter email
    TWITTER_PASSWORD = "your_twitter_password"           # Replace with your Twitter password
    ```

2. Run the script:

    ```bash
    python main.py
    ```

## Class: InternetSpeedTwitterBot

### Methods

#### `get_internet_speed()`

Gets the current internet speed using Speedtest.net.

#### `login_twitter(email, password)`

Logs in to Twitter using the provided email and password.

#### `tweet_at_provider(email, password)`

Logs in to Twitter and tweets at the internet service provider about the current internet speed.

## Disclaimer

Use this script responsibly. Ensure compliance with Twitter's terms of service.
