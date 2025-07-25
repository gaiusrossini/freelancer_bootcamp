import requests
import os
import json
from freelance_sniper.config.settings import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID

NOTIFIED_PATH = os.path.join(os.path.dirname(__file__), '../data/notified_jobs.json')

def load_notified_links():
    if not os.path.exists(NOTIFIED_PATH):
        return []
    with open(NOTIFIED_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_notified_links(links):
    with open(NOTIFIED_PATH, 'w', encoding='utf-8') as f:
        json.dump(links, f, indent=2, ensure_ascii=False)

def send_telegram_alert(jobs):
    if not jobs:
        return

    notified_links = load_notified_links()
    new_jobs = [job for job in jobs if job['link'] not in notified_links]

    if not new_jobs:
        print("🔕 No new jobs to notify.")
        return

    message = "🚨 New Freelance Jobs:\n\n"
    for job in new_jobs[:10]:
        message += f"🔹 {job['title']}\n🔗 {job['link']}\n🧭 {job['source']}\n\n"

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "disable_web_page_preview": True
    }

    response = requests.post(url, data=payload)
    if response.status_code != 200:
        print("⚠️ Telegram send error:", response.text)
        return

    # Save newly notified links
    all_links = notified_links + [job['link'] for job in new_jobs]
    save_notified_links(all_links)
    print(f"✅ Sent {len(new_jobs)} new job(s) to Telegram.")
