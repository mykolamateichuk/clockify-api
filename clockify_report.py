import os

import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://api.clockify.me"

WORKSPACE_ID = "65c5cc8ce1fdd92b156c0c08"
PROJECT_ID = "65c5ccbc477532599ac3a4f4"
USER_ID = "65c5cc8ce1fdd92b156c0c07"

HEADERS = {
    "X-Api-Key": os.getenv("CLOCKIFY_API_KEY", "")
}

tasks = (
    requests.get(f"{BASE_URL}/api/v1/workspaces/{WORKSPACE_ID}"
                 f"/projects/{PROJECT_ID}/tasks", headers=HEADERS).json()
)

report_data = {
    "task_names": [],
    "task_durations": [],
    "task_start_times": [],
}


for index, task in enumerate(tasks):
    report_data["task_names"].append(task["name"])
    report_data["task_durations"].append(task["duration"])

    time_entries = (
        requests.get(f"{BASE_URL}/api/v1/workspaces/{WORKSPACE_ID}/user/"
                     f"{USER_ID}/time-entries",
                     headers=HEADERS).json()
    )

    for time_entry in time_entries:
        if time_entry["taskId"] == task["id"]:
            report_data["task_start_times"].append(
                time_entry["timeInterval"]["start"]
            )

            del time_entry

report_data["task_names"] = list(reversed(report_data["task_names"]))
report_data["task_durations"] = list(reversed(report_data["task_durations"]))
report_data["task_start_times"] = list(reversed(report_data["task_start_times"]))

tasks_by_date = {}

for task_start_time in report_data["task_start_times"]:
    if task_start_time[:10] not in tasks_by_date:
        tasks_by_date[task_start_time[:10]] = []

for index, task_start_time in enumerate(report_data["task_start_times"]):
    tasks_by_date[task_start_time[:10]].append(index)

for date in tasks_by_date.keys():
    print(date)
    print("************************************************")

    for task_index in tasks_by_date[date]:
        if task_index < len(tasks):
            task_duration = report_data["task_durations"][task_index]
            task_name = report_data["task_names"][task_index]

            print(f'{task_duration}'
                  f'{" " * (15 - len(task_duration) if task_duration else 11)}'
                  f'"{task_name}"')

    print("************************************************\n")
