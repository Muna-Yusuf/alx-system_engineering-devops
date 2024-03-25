#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID,
   returns information about his/her TODO list progress.

   Requirements:
    - You must use urllib or requests module.
    - The script must accept an integer as a parameter,
      which is the employee ID.
    - The script must display on the standard output the..
      employee TODO list progress in this exact format:

        - First line: Employee EMPLOYEE_NAME is done with...
          tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
            * EMPLOYEE_NAME: name of the employee.
            * NUMBER_OF_DONE_TASKS: number of completed tasks.
            * TOTAL_NUMBER_OF_TASKS: total number of tasks, which...
              is the sum of completed and non-completed tasks.
        - Second and N next lines display the title of completed tasks:
          TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE).
"""

import requests
import sys

url = 'https://jsonplaceholder.typicode.com/'


def check_tasks():
    id = sys.argv[1]
    user_resp = requests.get(url + "users/{}".format(id))
    user = user_resp.json()
    params = {"userId": id}
    task_req = requests.get(url + "todos", params=params)
    task_res = task_req.json()
    completed_task = []

    for task in task_res:
        if task.get("completed") is True:
            completed_task.append(task.get("title"))

    print("Employee {} is done with tasks({}/{}):".format(
                    user.get("name"),
                    len(completed_task),
                    len(task_res)
                ))
    for completed in completed_task:
        print("\t {}".format(completed))


if __name__ == "__main__":
    check_tasks(int(sys.argv[1]))
