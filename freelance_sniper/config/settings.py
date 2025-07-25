import os
from dotenv import load_dotenv

# Get absolute path to the project root (2 levels above this file)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
dotenv_path = os.path.join(BASE_DIR, '.env')

# Load environment variables from .env
load_dotenv(dotenv_path)

# Telegram bot credentials: supports both TELEGRAM_* and BOT_*
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN") or os.getenv("BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID") or os.getenv("CHAT_ID")

# Keywords used to filter job titles
KEYWORDS = [
    "python",
    "automation",
    "scraping",
    "ai",
    "selenium",
    "bot",
    "API"
]
