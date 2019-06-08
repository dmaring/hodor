#!/usr/bin/python3
"""
This script votes 1024 times on the Holberton School
Hodor php site
"""
import requests


def hodor_vote():
    hheaders = {'Content-type': 'application/x-www-form-urlencoded'}
    hdata = 'id=675&holdthedoor=Submit+Query'
    hurl = 'http://158.69.76.135/level0.php'

    for i in range(1024):
        req = requests.request('POST', hurl, data=hdata, headers=hheaders)
        if req.status_code != 200:
            print(req.status_code)


if __name__ == '__main__':
    hodor_vote()
