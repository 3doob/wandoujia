# -*- coding: utf-8 -*-
from urllib import request
# from tool.parser import bs4_paraser
import random

def get_TCtrack(url):
    url_rand = "{:}?rand={:}".format(url, random.randint(10000, 99999))
    # msg.header3(" Start download ...")
    req = request.Request(url_rand)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36')

    with request.urlopen(req) as f:
        print('Status:', f.status, f.reason)
        for k, v in f.getheaders():
            if k == 'Date':
                print('%s: %s' % (k, v))
        Data = f.read().decode('utf-8')[1:-1]

    # wztf-196117 is [],no data
    if Data:
        res = Data
    else:
        res = []
    return res
