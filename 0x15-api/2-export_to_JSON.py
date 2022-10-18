#!/usr/bin/python3
"""
For a given employee ID, export to JSON information about TODO list progress
"""

if __name__ == '__main__':
    import requests
    import json
    from sys import argv

    r = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                     format(argv[1]))
    username = r.json().get('username')

    r = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                     format(argv[1]))
    data = r.json()

    export = {}
    export['{}'.format(argv[1])] = []
    for task in data:
        export['{}'.format(argv[1])].append({
            'task': task.get('title'),
            'completed': task.get('completed'),
            'username': username
        })

    with open('{}.json'.format(argv[1]), 'w') as outfile:
        json.dump(export, outfile)
