import jobs 
import time
import os

jobTitles = [
    "Cloud Engineer",
    "Cloud Architect",

    "Systems Engineer",
    "System Engineer",

    "Machine Learning",
    "ML",

    "Software Engineer",
    "Software Developer",
    "Trading Engineer",
    "Data Scientist",
    "Data Engineer",
    "Data Analyst",
    "Android",
    "Ios",
    "Web",
    "Developer",
    "Python",    
    "Java",      
    "Kotlin",    
    "Javascript",
    "React",     
]
# "New York", 
locations = ["Florida", "North Carolina", "California"]
for location in locations:
    for title in jobTitles:

        # search here
        inspect = jobs.search(
                # company="peloton",
                title=title,
                location=location,
            )

        # pandas import
        import pandas as pd
        # create folder location
        os.makedirs(f"{location}", exist_ok=True)
        # save to csv
        software = pd.DataFrame(inspect)
        software.to_csv(f"{location}/{title}.csv")
        # cooldown
        time.sleep(10)
    
    time.sleep(60)