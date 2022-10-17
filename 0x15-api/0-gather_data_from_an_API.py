#!/usr/bin/python3
import requests
def main():
    api_url = 'https://jsonplaceholder.typicode.com/todos/1'
    response = requests.get(api_url)
if __name__ == "__main__":
    
