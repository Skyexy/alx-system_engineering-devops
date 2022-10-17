#!/usr/bin/python3
import requests
import sys

def main():
    api_url = "https://jsonplaceholder.typicode.com/todos/{}".format(sys.argv[1])
    response = requests.get(api_url)
    print("Employee {} is done with tasks({}/{})\n")
    print(response.json())
if __name__ == "__main__":
    main()
