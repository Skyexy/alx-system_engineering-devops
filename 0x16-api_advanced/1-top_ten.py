#!/usr/bin/python3
"""
queries the Reddit API and prints the titles
"""
import requests

def top_ten(subreddit):
    try:
        base_ulr = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
        res = requests.get(base_ulr, headers = {'User-agent': 'custom'}, allow_redirects=False)
        for x in range(10):
            print (res.json()['data']['children'][x]['data']['title'])
    except:
        print (None)
