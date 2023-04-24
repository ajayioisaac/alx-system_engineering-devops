#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

if len(sys.argv) != 2:
    print(f"Usage: python3 {sys.argv[0]} EMPLOYEE_ID")
    sys.exit(1)

employee_id = sys.argv[1]

url_base = "https://jsonplaceholder.typicode.com"
url_user = f"{url_base}/users/{employee_id}"
url_todos = f"{url_base}/todos?userId={employee_id}"

response_user = requests.get(url_user)
response_todos = requests.get(url_todos)

if response_user.status_code != 200 or response_todos.status_code != 200:
    print("Error: Failed to retrieve data from the API")
    sys.exit(1)

user_data = response_user.json()
todos_data = response_todos.json()

employee_name = user_data["name"]
total_tasks = len(todos_data)
completed_tasks = len([todo for todo in todos_data if todo["completed"]])
completed_tasks_titles = [todo["title"] for todo in todos_data if todo["completed"]]

print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
for title in completed_tasks_titles:
    print(f"\t {title}")
