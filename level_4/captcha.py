#!/usr/bin/python3
"""
Module to convert captcha images to text
"""

import pytesseract
from PIL import Image


def read_captcha(path):
    my_image = Image.open(path)
    return(pytesseract.image_to_string(my_image))
