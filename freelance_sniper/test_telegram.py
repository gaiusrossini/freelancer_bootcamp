from freelance_sniper.config.settings import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID
import requests

print("🔎 DEBUG")
print("TELEGRAM_TOKEN:", TELEGRAM_TOKEN)
print("TELEGRAM_CHAT_ID:", TELEGRAM_CHAT_ID)
print("Full URL:", f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage")

def send_test():
    message = "✅ Freelance Sniper is now fully operational!"
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }
    response = requests.post(url, data=data)
    print("Status:", response.status_code)
    print("Response:", response.text)

send_test()
