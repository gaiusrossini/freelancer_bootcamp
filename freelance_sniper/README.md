Freelance Sniper Bot
A simple and powerful Python bot that scrapes and filters new freelance job listings from major platforms like Freelancer.com and Workana — and sends them to your Telegram in real time.

📌 Features

Scrapes recent jobs from:
https://www.freelancer.com/jobs
https://www.workana.com/jobs?category=it-programming

Filters jobs by keywords (e.g. "python", "automation", "ai")

Sends new jobs to Telegram (via bot)

Avoids duplicate notifications using a persistent history

Saves all filtered job data as structured JSON

Outputs filtered jobs to the terminal

Runs continuously in 15-minute cycles

Modular and easy to expand

🚀 How to Run
cd freelance_sniper
python -m freelance_sniper.main

🧪 Test Telegram
python freelance_sniper/test_telegram.py

🔐 Environment Setup
Create a .env file in the root directory with the following content:
BOT_TOKEN=your_telegram_bot_token
CHAT_ID=your_telegram_chat_id

📁 Project Structure
freelance_sniper/
├── scrapers/
│ ├── freelancer.py
│ └── workana.py
├── data/
│ ├── jobs.json
│ └── notified_jobs.json
├── config/
│ └── settings.py
├── telegram/
│ └── send_alert.py
├── main.py
├── test_telegram.py
└── README.md

🧠 Output Format
Each job is a dictionary like:
{
"title": "Job title here",
"link": "https://freelancer.com/project/...",
"source": "freelancer.com"
}

📦 Future Ideas

Detect project budgets and skill tags

Filter by region, experience level or payment type

Add support for Upwork, Guru, PeoplePerHour, etc.

Add daily/weekly summary digest via Telegram or email

Deploy with Docker and keep running 24/7

🧑‍💻 Author
Built by Gaius Rossini (personal programming bootcamp on a mission to earn first dollar globally as a freelance Python developer.)

