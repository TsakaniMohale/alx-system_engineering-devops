#!/usr/bin/python3
"""API usage"""
import json
import requests


def API():
    """Build a JSON file with id, username, task, and task status"""
    # Setting URLs
    baseUrl = "https://jsonplaceholder.typicode.com/"
    tasksUrl = baseUrl + "todos"
    emplUrl = baseUrl + "users"

    def emna(a):
        """Returns the user name from the user URL"""
        # Setting the URL
        usersUrl = baseUrl + "users/" + str(a)
        # Fetches the required data and isolates the name
        with requests.get(usersUrl) as marko:
            polo = marko.json()
            name = polo.get("username")
            return str(name)

    # Fetchs the number of the users
    emplNumb = None
    with requests.get(emplUrl) as marko:
        polo = marko.json()
        emplNumb = len(polo)
    # Getting tasks list
    with requests.get(tasksUrl) as marko:
        polo = marko.json()
        userdic = {}
        for num in range(1, emplNumb + 1):
            undone = []
            for user in polo:
                if user["userId"] == num:
                    undone.append({"username": emna(num),
                                   "task": user.get("title"),
                                   "completed": user.get("completed")})
            userdic[num] = undone

    # Writing file
    fileName = "todo_all_employees.json"
    with open(fileName, "a") as file:
        file.write(json.dumps(userdic))


if __name__ == "__main__":
    API()
