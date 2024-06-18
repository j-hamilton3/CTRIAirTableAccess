from airtable import Airtable
import requests
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Replace 'baseKey' and 'table name' with appropriate values
base_key = 'apphf38ldaaUbUExb'
table_name = 'tblVfGpBk27WnNufK'
api_key = os.environ['AIRTABLE_API_KEY']

# Initialize the Airtable client
airtable = Airtable(base_key, table_name, api_key=api_key)

# Retrieve all data from the 'Main View' and store it in 'table_data'
try:
    table_data = airtable.get_all()
    print("Data retrieved successfully.")
    print(table_data)
except requests.exceptions.HTTPError as e:
    print(f"An error occurred: {e}")
