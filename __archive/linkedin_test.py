import requests
from pprint import pprint

company_link = 'https://www.linkedin.com/voyager/api/entities/companies/2652230'

with requests.session() as s:

    # cookies 
    s.cookies['li_at'] = "AQEDASXVJN4CNAydAAABhjL1IzkAAAGGe4eYe00AtPtgvLKf7R0YSEPHlu3iRGt9MdVNc8VEfjGmJKtAayBYqUxn97DK1t0TL6Y0viH4xTlmVWDwkrLnok_dFJXVma62ZEhVYNBcoL9nrEC0oAaJ2rbe"
    s.cookies["JSESSIONID"] = "ajax:2527024484187025441"
    # headers
    s.headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",
        "csrf-token": s.cookies["JSESSIONID"].strip('"')
    }


    # fetch
    # response = s.get(company_link)

    # fetch
    response = s.get(
        url   ="https://www.linkedin.com/voyager/api/search/hits", 
        params= {
            'decorationId': 'com.linkedin.voyager.deco.jserp.WebJobSearchHitLite-17',
            'count': 7,
            'filters': 'List(company->1185|88295|83259|164218|10419580,originToLandingJobPostings->3477568451|3468533894|3478683353|3475938408|3294495368|3333507194|3131334795|3458274795|3464990946,geoUrn->urn:li:fs_geo:92000000,resultType->JOBS)',
            'origin': 'JOB_SEARCH_PAGE_OTHER_ENTRY',
            # 'originToLandingJobPostings': 'List(3477568451,3468533894,3478683353,3475938408,3294495368,3333507194,3131334795,3458274795,3464990946)',
            # 'q': 'jserpFilters',
            # 'queryContext': 'List(primaryHitType->JOBS,spellCorrectionEnabled->true)',
            'start': 0,
            # 'topNRequestedFlavors': 'List(HIDDEN_GEM,IN_NETWORK,SCHOOL_RECRUIT,COMPANY_RECRUIT,SALARY,JOB_SEEKER_QUALIFIED,PRE_SCREENING_QUESTIONS,SKILL_ASSESSMENTS,ACTIVELY_HIRING_COMPANY,TOP_APPLICANT)',
        }
    )
    pprint(response.text, indent=4)
    pprint(response.json(), indent=4)

# JSESSIONID:""ajax:2527024484187025441""
# li_at:"AQEDASXVJN4CNAydAAABhjL1IzkAAAGGe4eYe00AtPtgvLKf7R0YSEPHlu3iRGt9MdVNc8VEfjGmJKtAayBYqUxn97DK1t0TL6Y0viH4xTlmVWDwkrLnok_dFJXVma62ZEhVYNBcoL9nrEC0oAaJ2rbe"
# https://www.linkedin.com/jobs/search/?f_C=1185%2C88295%2C83259%2C164218%2C10419580&geoId=92000000&origin=COMPANY_PAGE_JOBS_CLUSTER_EXPANSION&originToLandingJobPostings=3477568451%2C3468533894%2C3478683353%2C3475938408%2C3294495368%2C3333507194%2C3131334795%2C3458274795%2C3464990946&lipi=urn%3Ali%3Apage%3Ad_flagship3_company%3BbdKWA8OBTjeEB3WkvBzERw%3D%3D

