from apify_client import ApifyClient
import os
from dotenv import load_dotenv
load_dotenv()

apify_client = ApifyClient(os.getenv("APIFY_API_KEY"))

def linkedin_job_search(search_query, location="india", num_jobs=5):
    """Search for jobs on LinkedIn using Apify's LinkedIn Job Scraper."""
    input = {
        "title": search_query,
        "location": location,
        "num_jobs": num_jobs,
        "proxy":{
            "useApifyProxy": True,
            "apifyProxyGroups": ["RESIDENTIAL"],
        }
    }
    run = apify_client.actor("bebity/linkedin-jobs-scraper").call(run_input=input)
    job_results = apify_client.dataset(run["defaultDatasetId"]).list_items().items
    return job_results


def fetch_naukri_jobs(search_query, location = "india", rows=5):
    run_input = {
        "keyword": search_query,
        "maxJobs": 60,
        "freshness": "all",
        "sortBy": "relevance",
        "experience": "all",
    }
    run = apify_client.actor("wsrn5gy5C4EDeYCcD").call(run_input=run_input)
    jobs = list(apify_client.dataset(run["defaultDatasetId"]).iterate_items())
    return jobs