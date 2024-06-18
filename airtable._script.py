from airtable import Airtable
import requests
import os
from dotenv import load_dotenv
import json

# Load environment variables from the .env file.
load_dotenv()

base_key = 'apphf38ldaaUbUExb'
table_name = 'tblVfGpBk27WnNufK'
api_key = os.environ['AIRTABLE_API_KEY']

airtable = Airtable(base_key, table_name, api_key=api_key)

try:
    table_data = airtable.get_all() # Consider accessing specific views later.
    print("Data retrieved successfully.")
    print(json.dumps(table_data, indent=2))
except requests.exceptions.HTTPError as e:
    print(f"An error occurred: {e}")
