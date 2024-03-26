#!/usr/bin/python3
"""This is the first task of API"""
import json
import requests
import sys


if __name__ == "__main__":
    """This starts our code"""
    users = "https://jsonplaceholder.typicode.com/users/" + sys.argv[1]
    task = "https://jsonplaceholder.typicode.com/todos"
    totTask = 0
    over = 0
    done = []
    Name = None
    with requests.get(users) as marko:
        polo = marko.json()
        Name = polo["name"]
    with requests.get(task) as marko2:
        polo2 = marko2.json()
        for elem in polo2:
            if elem["userId"] == int(sys.argv[1]):
                totTask = totTask + 1
            if (elem["userId"] == int(sys.argv[1]) and
                    elem["completed"] is True):
                over = over + 1
                done.append(elem["title"])
    print("Employee {} is done with tasks({}/{})".format(Name, over, totTask))
    for item in done:
        print("\t{}".format(item))
