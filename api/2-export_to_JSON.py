#!/usr/bin/python3
"""exports data in the JSON format"""

import json
import requests
import sys


def export_to_csv(user_id):
    base_url = "https://jsonplaceholder.typicode.com"
    user_endpoint = f"{base_url}/users/{user_id}"
    todo_endpoint = f"{base_url}/todos?userId={user_id}"

    user_res = requests.get(user_endpoint)
    user_data = user_res.json()
    user_name = user_data.get("username")
    user_id = user_data.get("id")

    todos_res = requests.get(todo_endpoint)
    todos_data = todos_res.json()

    file_name = f"{user_id}.json"

    data = {
        user_id: [
            {
                "task": task["title"],
                "completed": task["completed"],
                "username": user_name,
            }
            for task in todos_data
        ]
    }

    with open(file_name, "w") as f:
        json.dump(data, f)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit()
    try:
        id = int(sys.argv[1])
        export_to_csv(id)
    except ValueError:
        sys.exit()
