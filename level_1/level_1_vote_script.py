#!/usr/bin/python3
"""
This script votes 4096 times on the Holberton School
Hodor php site
"""
import requests
from BS_scrape import scrape_for_key


def hodor_vote():
    """
    function that will vote an aribtrary amount of times
    to the hodor online php poll
    """

    hheaders = {
        'Content-type': 'application/x-www-form-urlencoded',
    }
    hdata = {
        'id': '675',
        'holdthedoor': 'Submit+Query',
    }
    hurl = 'http://158.69.76.135/level1.php'

    count = 0
    for i in range(4074):
        hkey = scrape_for_key()
        hcookies = {'HoldTheDoor': hkey}
        hdata['key'] = hkey

        req = requests.request('POST', hurl, data=hdata, headers=hheaders,
                               cookies=hcookies)
        req.raise_for_status()
        count += 1
        print(count)

if __name__ == '__main__':
    hodor_vote()
