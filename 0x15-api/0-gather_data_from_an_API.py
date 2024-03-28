#!/usr/bin/python3
"""API usage"""
import json
import requests
import sys


def API():
    """Get user name and undone tasks list"""
    # getting user name
    baseUrl = "https://jsonplaceholder.typicode.com/"
    usersUrl = baseUrl + "users/" + sys.argv[1]
    tasksUrl = baseUrl + "todos"
    with requests.get(usersUrl) as marko:
        polo = marko.json()
        name = polo["name"]

    # Getting tasks list
    with requests.get(tasksUrl) as marko:
        polo = marko.json()
        tasks = 0
        done = 0
        toDo = []
        for elem in polo:
            if elem["userId"] == int(sys.argv[1]):
                tasks = tasks + 1
            if (elem["userId"] == int(sys.argv[1]) and
                    elem["completed"] is True):
                done = done + 1
                toDo.append(elem["title"])
    print("Employee {} is done with tasks({}/{}):".format(name, done, tasks))
    for task in toDo:
        print("\t", task)


if __name__ == "__main__":
    API()
