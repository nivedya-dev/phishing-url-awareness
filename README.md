# Phishing URL Awareness Checker

## Overview
Phishing is a common scam where attackers send fake links to trick people into giving away passwords, credit card numbers, or personal info
I built this simple Python tool for my Cybersecurity Internship to inspect link text and flag obvious warning signs—like hidden `@` symbols or strange IP addresses—without ever opening or visiting the link.

## Features
- Flags `@` symbols that try to hide the true destination
- Warns if a link is suspiciously long (over 100 characters)
- Detects raw IP address numbers used instead of normal domain names
- Flags URLs with way too many dots or subdomains (5 or more).
- Detects Punycode (`xn--`) markers used to mimic real letter names
- Flags unencrypted plain HTTP connections
- **Interactive Menu**: Runs in a loop so you can test multiple links without restarting the script every time
- **Crash Prevention**: Handles broken or invalid link text smoothly without stopping the program

## Requirements
Python 3.10 or higher. Uses standard built-in Python tools (`re` and `urllib.parse`), so no extra installation is needed

## How to Run
Open your terminal in the project folder and run

```run
python phishing_checker.py
Result:
- Uses an IP address instead of a familiar domain.
- Uses HTTP. HTTPS alone does not prove trust.

Never enter passwords from unexpected links.