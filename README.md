# WordPress Login Flooder (DDoS)

A simple Python script to flood a WordPress login page with fake credentials using multithreading in order to DDoS the site.

## Features

- Cycles through random, anonymous proxies from the scraped proxy list using the `fp` library to obfuscate true IP
- Generates fake IP addresses, user agents, and credentials using the `faker` library
- Sends spoofed `X-Forwarded-For`, `Fastly-Client-IP`, and `CF-Connecting-IP` headers to further obfuscate (Note: this will only work if server WAF/VCL is misconfigured and doesn't drop incoming headers)
- Utilizes the `requests` library to make POST requests to the specified login page URL
- Uses the `termcolor` library to print success and error messages in different colors
- Runs indefinitely with multiple threads concurrently to increase the rate of DDoS attempts

## Requirements

Using `pip install`

- `requests`
- `termcolor`
- `faker`
- `fp` (free-proxy)

## Usage

`python wp_login_flooder.py`

Enter the URL to the WordPress login page when prompted. The script will then continuously flood the login page with fake credentials using 100 concurrent threads. Successful login attempts and errors will be reported in the console.

**Note: This script is for educational purposes only and should not be used for malicious activities. The author is not responsible for any damages or consequences that may result from using this script.**
