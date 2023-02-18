from bs4 import BeautifulSoup
import requests


def search(company: str = "", title: str = "", location: str = "", bypass=False):

    # memoize title
    query = title

    # lower case params
    title = title.lower()
    company = company.lower()

    # guard-clause for params
    assert company or title, "Missing 'One-Of' -> 'company' or 'title' "

    # joining search keywords
    keywords: str = " ".join([company, title])

    # start-index for pagination
    start: int = 0 
    page:  int = 0
    # memoized-list for allJobs
    allJobs: list = []

    # While loop (with break condition)
    while True:

        # loop here
        r = requests.get("https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search",
            params= {
                'keywords': keywords,#peloton%20android
                'location': location,          #United%20States
                'start'   : str(start),        #0  
            }
        )
        print(f"{page}: {r.url}")

        # page as BS4 class-object
        jobsRaw = BeautifulSoup(r.text,'html.parser')\
                    .find_all('div', class_='base-card relative w-full hover:no-underline focus:no-underline base-card--link base-search-card base-search-card--link job-search-card')
        
        if not jobsRaw:
            break
        
        # parse all html tags (jobs)
        for job in jobsRaw:
            job_title = job.find('h3', class_='base-search-card__title').text.strip()
            job_company = job.find('h4', class_='base-search-card__subtitle').text.strip()
            job_location = job.find('span', class_='job-search-card__location').text.strip()
            job_link = job.find('a', class_='base-card__full-link')['href']

            # cast to dict
            jobSet : dict = {
                'title':    job_title,
                'company':  job_company,
                'location': job_location,
                'link':     job_link
            }

            if company and company not in jobSet["company"].lower():
                break 

            # append all valid jobs
            allJobs.append(jobSet)

        # increment start by 25
        start += 25
        page  += 1

    # end if title not needed
    if not title or bypass:
        return allJobs

    # remove incorrect titles
    tokens = title.split(" ")
    # match jobs to title
    allJobs = [ 
        singleJob for singleJob in allJobs 
            if set(tokens).issubset(set(singleJob["title"].lower().replace(","," ").replace("(", " ").split(" ")))]

    # add query for indexing
    allJobs = [ {**{"query": query}, **singleJob} for singleJob in allJobs]
    
    return allJobs