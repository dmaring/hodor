#!/usr/bin/python3
"""
This script votes 1024 times on the Holberton School
Hodor php site
"""
import requests
from BS_scrape import scrape
from captcha import read_captcha

def hodor_vote():
    """
    function that will vote an aribtrary amount of times
    to the hodor online php poll
    """

    hheaders = {
        'Content-type': 'application/x-www-form-urlencoded',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 \
        Safari/537.36 Edge/12.246',
        'Referer': 'http://158.69.76.135/level3.php',
    }
    hdata = {
        'id': '675',
        'holdthedoor': 'Submit+Query',
    }
    hurl = 'http://158.69.76.135/level3.php'

    count = 0
    for i in range(1024):
        scrape_dict = scrape()
        hcookies = scrape_dict['cookies']
        hdata['key'] = scrape_dict['value']
        hdata['captcha'] = scrape_dict['captcha']
        req = requests.request('POST', hurl, data=hdata, headers=hheaders,
                               cookies=hcookies)
        req.raise_for_status()
        count += 1
        print(count)

if __name__ == '__main__':
    hodor_vote()
