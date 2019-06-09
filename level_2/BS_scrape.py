#!/usr/bin/python3
"""
Module that scrapes hodor level_1 voting site for the
hidden key
"""
import requests
import bs4


def scrape_for_key():
    """
    A function that will scrape the poll website for the
    DOM element that contains the hidden key for the cookie
    """

    res = requests.get('http://158.69.76.135/level1.php')
    res.raise_for_status()
    # create beatiful soup object from response
    bs_obj = bs4.BeautifulSoup(res.text, features="lxml")
    elems = bs_obj.select('input[type="hidden"]')
    return(elems[0].attrs['value'])

if __name__ == '__main__':
    scrape_for_key()
