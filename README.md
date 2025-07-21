# Login Honeypot

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

---

## MITRE ATT&CK Techniques Covered

This login honeypot project is designed to detect and log unauthorized login attempts, which relate to the following MITRE ATT&CK techniques:

- **T1110 — Brute Force:** Detects repeated attempts to guess usernames and passwords.
- **T1078 — Valid Accounts:** Monitors usage of valid credentials by attackers.
- **T1201 — Password Guessing:** Focuses on repeated password guessing attempts as a sub-technique of brute force.

By capturing these activities, this honeypot helps in analyzing attacker behavior related to credential access and unauthorized system entry attempts.
