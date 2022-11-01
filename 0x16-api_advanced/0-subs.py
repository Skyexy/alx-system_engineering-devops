#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers
"""

def number_of_subscribers(subreddit):
  res = requests.get("https://oauth.reddit.com/r/programming/about")
