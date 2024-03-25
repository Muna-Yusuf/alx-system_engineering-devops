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
import re

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            id = int(sys.argv[1])
            req = requests.get('{}/users/{}'.format(url, id)).json()
            task_req = requests.get('{}/todos'.format(url)).json()
            emp_name = req.get('name')
            tasks = list(filter(lambda x: x.get('userId') == id, task_req))
            completed_tasks = list(filter(lambda x: x.get('completed'), tasks))
            print(
                'Employee {} is done with tasks({}/{}):'.format(
                    emp_name,
                    len(completed_tasks),
                    len(tasks)
                )
            )
            if len(completed_tasks) > 0:
                for task in completed_tasks:
                    print('\t {}'.format(task.get('title')))
