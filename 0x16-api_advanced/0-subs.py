#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers
"""
import requests

def number_of_subscribers(subreddit):
    try:
        base_ulr = "https://www.reddit.com/r/{}/about.json".format(subreddit)
        res = requests.get(base_ulr, headers = {'User-agent': 'custom'}, allow_redirects=False)
        return (res.json()['data']['subscribers'])
    except:
        return (0)
