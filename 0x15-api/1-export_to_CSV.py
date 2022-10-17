#!/usr/bin/python3
"""
For a given employee ID, return information about TODO list progress
"""

if __name__ == '__main__':
    import requests
    from sys import argv

    r = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                     format(argv[1]))
    name = r.json().get('username')
    
    res = requests.get('https://jsonplaceholder.typicode.com/todos/{}'.
                     format(argv[1]))
    filemane = argv[1].csv
    long = []
    for i in res.json():
        title = i.get('title')
        bool = i.get('completed"')
        subject = ["{}".format(argv[1]),"{}".format(name),"{}".format(bool),"{}".format(title)]
        long.append(subject)
        
    with open(filename, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(subject)
