#!/usr/bin/python3
"""
Checks student output for returning info from REST API
"""

import requests
import sys


def main():
    """ doc """
    id = sys.argv[1]
    url = f'https://jsonplaceholder.typicode.com/'
    users = f'users?id={id}'
    todos = f'todos?userId={id}'
    done  = f'{todos}&copletetd=true'
    notdone = f'{todos}&copletetd=false'
    user_resp = requests.get(f'{url}{users}').json()
    Name = user_resp[0].get("name")
    
    task_req = requests.get(f'{url}{todos}').json()
    task_res = requests.get(f'{url}{done}').json()
    completed = len(task_req)
    comp_t = len(task_res)

    print(f'Employee {Name} is done with tasks({completed}/{comp_t}):')
    for task in task_res:
        print("\t "+task.get("title"))


if __name__ == "__main__":
    main()
