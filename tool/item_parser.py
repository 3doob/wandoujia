# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup


def item_paraser(html):
    value = {}
    soup = BeautifulSoup(html, 'html.parser')

    value['interactionCount'] = soup.find('i',attrs={'itemprop':'interactionCount'}).string if soup.find('i',attrs={'itemprop':'interactionCount'}) else ""
    value['love'] = soup.find('div',attrs={'class':'app-info-data'}).find_all('span')[1].i.string if soup.find('div',attrs={'class':'app-info-data'}).find_all('span')[1].i else ""
    value['comment-open'] = soup.find('a',attrs={'class':'comment-open'}).i.string if soup.find('a',attrs={'class':'comment-open'}).i else ""
    value['editorComment'] = soup.find('div',attrs={'class':'con'}).text if soup.find('div',attrs={'class':'editorComment-title'}) else ""
    overviews = soup.find('div',attrs={'class':'overview'}).find_all('img') if soup.find('div',attrs={'class':'overview'}).find_all('img') else ""
    value['overviews'] = []
    for i in overviews:
        value['overviews'].append(i['src'])
    value['itemprop'] = soup.find('div',attrs={'itemprop':'description'}).text if soup.find('div',attrs={'itemprop':'description'}) else ""
    return value