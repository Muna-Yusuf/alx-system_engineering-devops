#!/usr/bin/python3
"""Extend your Python script to export data in the JSON format.
    Requirements:
        - Records all tasks that are owned by this employee
        - Format must be: { "USER_ID": [{"task": "TASK_TITLE", "completed":
            TASK_COMPLETED_STATUS, "username": "USERNAME"},
            {"task": "TASK_TITLE", "completed":
            TASK_COMPLETED_STATUS,
            "username": "USERNAME"}, ... ]}
            File name must be: USER_ID.json
"""

import json
import requests
import sys


def main():
    """DOC"""

    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(id)).json()
    username = user.get("username")
    params = {"userId": id}
    todos = requests.get(url + "todos", params).json()

    data_export = {
        id: [
            {
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            }
            for t in todos
        ]
        }
    with open("{}.json".format(id), "w") as jsonfile:
        json.dump(data_export, jsonfile, indent=4)


if __name__ == "__main__":
    main()
