#!/usr/bin/python3
'''queries the reddit API and returns top ten hot posts in a subreddit'''
import requests


def top_ten(subreddit):
    '''returns the top ten reddit posts'''

    headers = {'User-Agent': 'Tanatswa'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        hot_posts = response.json().get('data').get('children')
        for i, _ in enumerate(hot_posts):
            if i < 9:
                print(hot_posts[i].get('data').get('title'))
            else:
                break
    else:
        print(None)
