from scrapers.freelancer import get_jobs as get_freelancer_jobs
from scrapers.workana import get_jobs as get_workana_jobs
from config.settings import KEYWORDS
from telegram.send_alert import send_telegram_alert
import json
import time

def save_jobs(jobs, filename="data/jobs.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(jobs, f, indent=2, ensure_ascii=False)

def filter_jobs(jobs):
    filtered = []
    for job in jobs:
        title_lower = job['title'].lower()
        if any(keyword in title_lower for keyword in KEYWORDS):
            filtered.append(job)
    return filtered

def main():
    freelancer_jobs = get_freelancer_jobs()
    workana_jobs = get_workana_jobs()

    all_jobs = freelancer_jobs + workana_jobs
    filtered_jobs = filter_jobs(all_jobs)

    save_jobs(filtered_jobs)

    print(f"Filtered jobs found: {len(filtered_jobs)}")
    for job in filtered_jobs:
        print(f"[{job['source']}] {job['title']}\n{job['link']}\n")

    send_telegram_alert(filtered_jobs)

if __name__ == "__main__":
    while True:
        print("🔄 Checking for new jobs...")
        main()
        print("⏳ Waiting 15 minutes...\n")
        time.sleep(900)