# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

def bs4_paraser(html):
    all_value = []
    value = {}
    soup = BeautifulSoup(html,'html.parser')
    all_li_item = soup.find_all('li',attrs={'class': 'card'})
    for r in all_li_item:
        value['Link'] = r.find('div' ,attrs={'class':'icon-wrap'}).a['href']
        value['img'] = r.find('div' ,attrs={'class':'icon-wrap'}).a.img['src']
        value['desc'] = r.find('div' ,attrs={'class':'app-desc'}).h2.a.string
        value['install-count'] = r.find('span',attrs={'class','install-count'}).string
        value['appM'] = r.find('div',attrs={'class','meta'}).find_all('span')[2].string
        value['comment'] = r.find('div',attrs={'class','comment'}).string
        value['downLoadLink'] = r.find('a',attrs={'class','install-btn'})['href']
        all_value.append(value)
        value = {}
    return all_value