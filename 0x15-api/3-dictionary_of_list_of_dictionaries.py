#!/usr/bin/python3
"""Extend your Python script to export data in the JSON format.
    Requirements:
        - Records all tasks that are owned by this employee
        - Format must be: { "USER_ID": [{"task": "TASK_TITLE", "completed":
            TASK_COMPLETED_STATUS, "username": "USERNAME"},
            {"task": "TASK_TITLE", "completed":
            TASK_COMPLETED_STATUS,
            "username": "USERNAME"}, ... ]}
            File name must be: todo_all_employees.json
"""

import json
import requests


def main():
    """DOC"""

    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    data_export = {}
    for user in users:
        id = user["id"]
        user_url = url + f"todos?userId={id}"
        todo_list = requests.get(user_url).json()

        data_export[id] = [
            {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": user.get("username"),
            }
            for todo in todo_list
        ]

    return data_export


if __name__ == "__main__":
    data_export = main()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(data_export, jsonfile, indent=4)
