#!/usr/bin/python3
"""Gather data from an API"""

import requests
import sys

if __name__ == '__main__':
    user_id = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(user_id)

    user_info = requests.get(user_url).json()
    todos_info = requests.get(todos_url).json()

    employee_name = user_info.get("name")
    done_tasks = [task for task in todos_info if task.get("completed")]
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(done_tasks), len(todos_info)))
    for task in done_tasks:
        print("\t {}".format(task.get("title")))
