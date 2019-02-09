from click_sub.subs_generator import *
import requests
from urllib.parse import urlparse


subs = {'sub1':generate_sub1(),
        'sub2':generate_sub2(),
        'sub3':generate_sub3(),
        'sub4':generate_sub4(),
        'sub5':generate_sub5()
        }
link = 'http://lawn.mobstra.com/go?id=591&hash=FG4crGUwMN'

""" Send request using link variable ang generated in subs_generator subs
"""
r = requests.get(link,subs)


def get_responce_url():
    return r.text


""" Get parsed response url and separate it on params
"""
parsed_url = urlparse(r.text)

""" Append click id from response(cutting '/')
"""


def apend_click_from_link():
    return parsed_url.path[1:]


def set_click_param():
    click = apend_click_from_link()
    return click
