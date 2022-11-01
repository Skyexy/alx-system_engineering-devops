#!/usr/bin/python3
import requests
"""
queries the Reddit API and returns the number of subscribers
"""

def recurse(subreddit, hot_list=[], after=''):
    try:
        base_ulr = "https://www.reddit.com/r/{}/hot.json?after={}".format(subreddit, after)
        res = requests.get(base_ulr, headers = {'User-agent': 'custom'}, allow_redirects=False)
        if after is None:
            return hot_list
        for thread in res.json().get('data').get('children'):
            hot_list+=[thread.get('data').get('title')]
        after = res.json().get('data').get('after')
        recurse(subreddit, hot_list, after)
        return hot_list
    except:
        return (None)
