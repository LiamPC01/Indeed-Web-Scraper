import requests
from bs4 import BeautifulSoup

URL = "https://uk.indeed.com/jobs?q=programmer&l=Norwich&from=searchOnHP&vjk=ef16af20be95a5b6"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="mosaic-provider-jobcards")
job_elements = results.find_all("td", class_="resultContent")

for job_element in job_elements:
    title_element = job_element.find("h2", class_="jobTitle")
    company_element = job_element.find("span", class_="companyName")
    location_element = job_element.find("div", class_="companyLocation")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()

