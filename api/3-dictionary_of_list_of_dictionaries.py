#!/usr/bin/python3
"""exports data in the JSON format"""

import json
import requests


def export_to_json():
    base_url = "https://jsonplaceholder.typicode.com"
    user_endpoint = f"{base_url}/users/"

    user_data = requests.get(user_endpoint).json()

    all_tasks = {}
    for user in user_data:
        user_id = user["id"]
        user_name = user["username"]

        todo_endpoint = f"{base_url}/todos?userId={user_id}"
        todos_data = requests.get(todo_endpoint).json()

        tasks = [
            {
                "username": user_name,
                "task": task["title"],
                "completed": task["completed"],
            }
            for task in todos_data
        ]

        all_tasks[user_id] = tasks

    with open("todo_all_employees.json", "w") as f:
        json.dump(all_tasks, f)


if __name__ == "__main__":
    export_to_json()
