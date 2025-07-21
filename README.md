# Fake Login Honeypot

This is a simple Flask-based honeypot that simulates a login page and logs all login attempts.

## Features
- Captures IP, timestamp, and credentials
- Minimal setup
- For educational and demonstration use only

## How to Run

1. Install Flask:
   ```
   pip install flask
   ```

2. Run the app:
   ```
   python app.py
   ```

3. Visit `http://localhost:5000` in your browser.

## Logs

All attempts are stored in `logs/credentials.log`.
