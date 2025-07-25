import requests
from bs4 import BeautifulSoup

def get_jobs():
    url = "https://www.freelancer.com/jobs"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    job_list = []

    for job_card in soup.select("div.JobSearchCard-item"):
        title_tag = job_card.select_one("a.JobSearchCard-primary-heading-link")
        if title_tag:
            title = title_tag.text.strip()
            link = "https://www.freelancer.com" + title_tag['href']
            job_list.append({
                "title": title,
                "link": link,
                "source": "freelancer.com"
            })

    return job_list
