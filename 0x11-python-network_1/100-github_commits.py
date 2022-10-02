#!/usr/bin/python3
"""
     a Python script that takes 2 arguments in order to
     list 10 commits (from the most recent to oldest)
     of the repository “rails” by the user “rails”
"""

import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == '__main__':
    repo = sys.argv[1]
    owner = sys.argv[2]

    url = "https://api.github.com/repos/{:s}/{:s}/commits".format(
        owner, repo)

    response = requests.get(url)

    commits = response.json()

    for commit in commits[:10]:
        sha = commit.get('sha')
        name = commit.get('commit').get('author').get('name')
        print("{}: {}".format(sha, name))
