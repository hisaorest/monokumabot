import os
import sys
import requests

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

# Customize this message however you like
MESSAGE = "Good morning, everyone! ☀️"

def send_message():
    if not BOT_TOKEN or not CHAT_ID:
        print("Error: BOT_TOKEN or CHAT_ID environment variable is missing.")
        sys.exit(1)

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": MESSAGE,
    }

    response = requests.post(url, data=payload, timeout=10)

    if response.status_code == 200:
        print("Message sent successfully.")
    else:
        print(f"Failed to send message: {response.status_code} {response.text}")
        sys.exit(1)

if __name__ == "__main__":
    send_message()
