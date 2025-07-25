import requests
from bs4 import BeautifulSoup

def get_jobs():
    url = "https://www.workana.com/jobs?category=it-programming"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    job_list = []

    for job_card in soup.select("article.project-item"):
        title_tag = job_card.select_one("a[href*='/job/']")
        if title_tag:
            title = title_tag.text.strip()
            link = "https://www.workana.com" + title_tag["href"]
            job_list.append({
                "title": title,
                "link": link,
                "source": "workana"
            })

    return job_list
