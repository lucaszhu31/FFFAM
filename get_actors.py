from dotenv import load_dotenv
import os
import sys
from apify_client import ApifyClient

# Windows consoles default to cp1252, which can't print emoji in captions
sys.stdout.reconfigure(encoding="utf-8")

load_dotenv()

# Initialize the ApifyClient with the Apify API token from .env
token = os.getenv("APIFY_TOKEN")
if not token:
    raise SystemExit("APIFY_TOKEN not set in .env")
client = ApifyClient(token)

# Prepare the Actor input
run_input = {
    "resultsType": "posts",
    "directUrls": ["https://www.instagram.com/sumsmcgill/"],
    "resultsLimit": 10,
}

# Run the Actor and wait for it to finish
run = client.actor("apify/instagram-scraper").call(run_input=run_input)
if run is None:
    raise SystemExit("Actor run failed to start")

# Fetch and print Actor results from the run's dataset (if there are any)
print(f"💾 Check your data here: https://console.apify.com/storage/datasets/{run.default_dataset_id}")
for item in client.dataset(run.default_dataset_id).iterate_items():
    print(item)
