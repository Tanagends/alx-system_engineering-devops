#!/usr/bin/python3
"""a function that queries the Reddit API and returns the number of
subscribers for a given subreddit"""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = {"User-Agent": "Tanagends"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        return response.json().get('data').get("subscribers")
    else:
        return 0
