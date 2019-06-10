#!/usr/bin/python3
"""
Function that parses cookie object and returs a dict
of cookies
"""

def parse_cookies(c_obj):

    cookies_list = []
    input_list = str(c_obj).split()
    for item in input_list:
        if "=" in item:
            cookies_list.append(item)
    return_dict = {}
    for cookie in cookies_list:
        temp_list = cookie.split('=')
        return_dict[temp_list[0]] = temp_list[1]

    return(return_dict)
