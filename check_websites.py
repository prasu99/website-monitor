import requests
import os

webhook_url = os.environ["SLACK_WEBHOOK"]
websites = {
    "USAT": "https://usat.example.com",
    "Site2": "https://site2.com",
    "Site3": "https://site3.com",
    "Site4": "https://site4.com",
    "Site5": "https://site5.com"
}

def check_websites():
    status_messages = []
    for name, url in websites.items():
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                status_messages.append(f"✅ {name} site is good")
            else:
                status_messages.append(f"⚠️ {name} site returned {response.status_code}")
        except Exception as e:
            status_messages.append(f"❌ {name} site is down ({str(e)})")

    message = "\n".join(status_messages)
    send_to_slack(message)

def send_to_slack(text):
    payload = {"text": text}
    requests.post(webhook_url, json=payload)

check_websites()
