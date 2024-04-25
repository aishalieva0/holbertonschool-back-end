#!/usr/bin/python3
"""exports data in the CSV format"""

import csv
import requests
import sys


def export_to_csv(user_id):
    base_url = "https://jsonplaceholder.typicode.com"
    user_endpoint = f"{base_url}/users/{user_id}"
    todo_endpoint = f"{base_url}/todos?userId={user_id}"

    user_res = requests.get(user_endpoint)
    user_data = user_res.json()
    user_name = user_data.get("name")
    user_id = user_data.get("id")

    todos_res = requests.get(todo_endpoint)
    todos_data = todos_res.json()

    file_name = f"{user_id}.csv"

    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            completed = task["completed"]
            title = task["title"]
            writer.writerow([user_id, user_name, completed, title])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit()
    try:
        id = int(sys.argv[1])
        export_to_csv(id)
    except ValueError:
        sys.exit()
