#!/usr/bin//env python3

from bs4 import BeautifulSoup
import requests
import time

print("Put unfamilier skills")

unfamilier_skill = input(">")

print(f"filtering out {unfamilier_skill}")

def find_jobs():
    html_text= requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text

    soup = BeautifulSoup(html_text, 'lxml')

    jobs = soup.find_all('li',class_ = 'clearfix job-bx wht-shd-bx')

    for index, job in enumerate(jobs):
        published_date = job.find('span',class_='sim-posted').span.text
        if 'few' in published_date:
            company_name = job.find('h3',class_='joblist-comp-name').text.replace(" ","")
            skills = job.find('span',class_='srp-skills').text.replace(" ","")
            more_info = job.header.h2.a['href']
            if unfamilier_skill not in skills:
                with open(f'{index}.txt','w') as f:

                    f.write(f"Company Name: {company_name.strip()} \n")
                    f.write(f"Skills: {skills.strip()} \n")
                    f.write(f"More Information: {more_info} \n")

                    print(f"FIle saved : {index}")

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f"waiting {time_wait} seconds...")
        time.sleep(time_wait *60)
