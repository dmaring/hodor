#!/usr/bin/python3
"""
Module that scrapes hodor level_1 voting site for the
hidden key
"""
from PIL import Image
from io import BytesIO
from captcha import read_captcha
import requests
import bs4
import tempfile
import os
from os import path
from parse_cookies import parse_cookies

def scrape():
    """
    A function that will scrape the poll website for the
    DOM element that contains the hidden key for the cookie
    and the text from the captcha image
    """


    s = requests.Session()
    res = s.get('http://158.69.76.135/level4.php')
    cookies = parse_cookies(res.cookies)
    res.raise_for_status()
    res_image = s.get('http://158.69.76.135/captcha.php')
    # create beautiful soup object from response
    bs_obj = bs4.BeautifulSoup(res.text, features='html.parser')
    fp = tempfile.TemporaryFile()
    fp.write(res_image.content)
    captcha_text = read_captcha(fp)
    fp.close()
    hidden = bs_obj.select('input[type="hidden"]')
    ret_dict = {
        'value': hidden[0].attrs['value'],
        'captcha': captcha_text,
        'cookies': cookies
    }
    s.close()

    return(ret_dict)


if __name__ == '__main__':
    scrape()
