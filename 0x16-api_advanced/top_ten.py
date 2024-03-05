#!/usr/bin/python3
"""One"""
import requests
import sys


if __name__ == "__main__":
    url = "https://www.reddit.com/r/{}/about.json".format(sys.argv[1])
    #url = 'https://www.reddit.com/r/{}/about.json'.format(sys.argv[1])
    response = requests.get(url)
    if response.status_code == 200:
        print(response.json())
