#!/usr/bin/python3
import requests
import sys

def main():
    api_url = "https://jsonplaceholder.typicode.com/users/{}".format(sys.argv[1])
    response = requests.get(api_url)
    name = response.json().get('name')
    
    r = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                     format(sys.argv[1]))
    total_numof_task = len(r.json())
    task_done = 0
    
    for i in  r.json():
        if i.get('completed') == "True":
            task_done += 1
    print("\nEmployee {} is done with tasks({}/{})\n")
    print(r.json())
    print(task_done)
if __name__ == "__main__":
    main()
