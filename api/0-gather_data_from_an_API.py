#!/usr/bin/python3

import requests
import sys


def get_todo_progress(user_id):
    base_url = "https://jsonplaceholder.typicode.com"
    user_endpoint = f'{base_url}/users/{user_id}'
    todo_endpoint = f'{base_url}/todos?userId={user_id}'

    user_res = requests.get(user_endpoint)
    user_data = user_res.json()
    user_name = user_data.get('name')

    todos_res = requests.get(todo_endpoint)
    todos_data = todos_res.json()

    completed_tasks = [task for task in todos_data if task['completed']]
    num_completed_tasks = len(completed_tasks)
    num_total_tasks = len(todos_data)

    print(f'Employee {user_name} is done with task\
({num_completed_tasks}/{num_total_tasks}):')
    for task in completed_tasks:
        print(f"\t{task['title']}")


if __name__ == "__main__":
    id = sys.argv[1]
    get_todo_progress(id)
