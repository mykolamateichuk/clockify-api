import os

import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://api.clockify.me"

WORKSPACE_ID = "65c5cc8ce1fdd92b156c0c08"
PROJECT_ID = "65c5ccbc477532599ac3a4f4"

HEADERS = {
    "X-Api-Key": os.getenv("CLOCKIFY_API_KEY", "")
}

response = requests.get(f"{BASE_URL}/api/v1/workspaces/"
                        f"{WORKSPACE_ID}/projects/{PROJECT_ID}/tasks", headers=HEADERS)

task_list = [task["name"] for task in response.json()]

for task in reversed(task_list):
    print(task)
