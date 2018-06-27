# -*- coding: utf-8 -*-
from tool.UrlTrack import get_TCtrack
from tool.parser import bs4_paraser
from tool.item_parser import item_paraser
from tool.output import writeFile
if __name__ == "__main__":
    url = 'http://www.wandoujia.com/apps'
    TCtrack = get_TCtrack(url)
    lists = bs4_paraser(TCtrack)
    # print(TCtrack)
    for item in lists:
        TCtrack = get_TCtrack(item.get('Link'))
        list = item_paraser(TCtrack)
        item['item-details'] = list
        print(item)
    writeFile('./output', lists)
