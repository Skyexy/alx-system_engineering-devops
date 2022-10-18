#!/usr/bin/python3
"""
For a given employee ID, return information about TODO list progress
"""

if __name__ == '__main__':
    import requests
    from sys import argv
    import csv

    r = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                     format(argv[1]))
    name = r.json().get('username')
    
    res = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                     format(argv[1]))
    long = []
    
    for lop in res.json():
        title = lop.get('title')
        subject = "{}".format(argv[1]),"{}".format(name),"{}".format(lop.get('completed"')),"{}".format(title)
        with open("{}.csv".format(argv[1]), 'w') as file:
            writer = csv.writer(file)
            writer.writerow(subject)
