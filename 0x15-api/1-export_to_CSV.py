#!/usr/bin/python3
"""Using what you did in the task #0, extend your Python..
   script to export data in the CSV format."""

import csv
import requests
import sys


def main():
    id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + "users/{}".format(id)).json()
    username = user.get("username")

    todos = requests.get(url + "todos", params={"userId": id}).json()
    with open("{}.csv".format(id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [id, username, t.get("completed"), t.get("title")]
         ) for t in todos]


if __name__ == "__main__":
    main()
