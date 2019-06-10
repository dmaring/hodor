#!/usr/bin/python3
"""
This script votes 1024 times on the Holberton School
Hodor php site
"""

import time
import requests
from BS_scrape import scrape
from captcha import read_captcha
from Proxies import ProxieList
from vote_num_scrape import scrape_vote_num


def hodor_vote():
    """
    function that will vote an aribtrary amount of times
    to the hodor online php poll
    """

    pl = ProxieList()
    hheaders = {
        'Content-type': 'application/x-www-form-urlencoded',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 \
        Safari/537.36 Edge/12.246',
        'Referer': 'http://158.69.76.135/level4.php',
    }
    hdata = {
        'id': '675',
        'holdthedoor': 'Submit+Query',
    }
    hurl = 'http://158.69.76.135/level4.php'
    timeout = 11

    target_votes = 98
    current_votes = scrape_vote_num()
    while current_votes < target_votes:
        scrape_dict = scrape()
        hproxy = dict(http="{}".format(pl.get_proxy()))
        hcookies = scrape_dict['cookies']
        hdata['key'] = scrape_dict['value']
        hdata['captcha'] = scrape_dict['captcha']
        try:
            req = requests.request('POST', hurl, data=hdata, headers=hheaders,
                                   cookies=hcookies, proxies=hproxy,
                                   timeout=timeout)
        except Exception as e:
            print(e)
            time.sleep(5)
            continue
        print(current_votes)
        # print(req.text)

if __name__ == '__main__':
    hodor_vote()
