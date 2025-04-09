import requests
import os

websites = {
    "USAT": "https://www.usatoday.com/money/blueprint/",
    "Forbes Travel Insurance": "https://travelinsurance.advisorjourney.forbes.com/search/",
    "Forbes AU": "https://www.forbes.com/advisor/au/",
    "Forbes IT": "https://www.forbes.com/advisor/it/",
    "Forbes CA": "https://www.forbes.com/advisor/ca/"
}

def check_sites():
    messages = []
    for name, url in websites.items():
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                messages.append(f"✅ {name} site is good")
            else:
                messages.append(f"❌ {name} site returned status code {response.status_code}")
        except requests.RequestException as e:
            messages.append(f"❌ {name} site is down ({e})")
    return "\n".join(messages)

def send_to_slack(message):
    webhook_url = os.environ["SLACK_WEBHOOK"]
    payload = {"text": message}
    requests.post(webhook_url, json=payload)

if __name__ == "__main__":
    message = check_sites()
    print(message)
    send_to_slack(message)

