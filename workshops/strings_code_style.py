import re
import requests


def text_filter(link, pattern):
    print(link)
    res = requests.get(link)
    names_re = re.compile(pattern)
    k = re.findall(names_re, res.text)
    return k


def text_filter_wrapper(input_text):
    link, pattern = input_text.split()
    return text_filter(link, pattern)
