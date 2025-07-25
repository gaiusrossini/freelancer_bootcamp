from scrapers import airdropslive, airdrops_io, airdropsmob, coinmarketcap
from core.collector import collect_and_store
from notifier.telegram import send_message
import schedule
import time
from datetime import datetime


def run_all_scrapers():
    all_airdrops = []

    for scraper in [airdropslive, airdrops_io, airdropsmob, coinmarketcap]:
        try:
            airdrops = scraper.get_airdrops()
            all_airdrops.extend(airdrops)
        except Exception as e:
            print(f"[runner] Error in {scraper.__name__}: {repr(e)}")

    new_airdrops = collect_and_store(all_airdrops)

    print(f"🔎 Total collected: {len(all_airdrops)}")
    if new_airdrops:
        print(f"🎯 We've found {len(new_airdrops)} new airdrops!")

        for airdrop in new_airdrops:
            msg = f"🚀 <b>{airdrop['title']}</b>\n🔗 {airdrop['link']}\n📡 Source: {airdrop['source']}"
            send_message(msg)
    else:
        print("😴 There's NO new airdrops.")


# === ⏰ DAILY SCHEDULER BLOCK === #
def job():
    print(f"\n=== Sniper job started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ===")
    run_all_scrapers()
    print("=== Job finished ===\n")


schedule.every().day.at("11:00").do(job)  # Change time here

print("📆 Sniper is scheduled to run daily at 11:00 AM.")

while True:
    schedule.run_pending()
    time.sleep(60)
