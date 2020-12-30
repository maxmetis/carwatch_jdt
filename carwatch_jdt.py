# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 09:19:45 2020

@author: Johnny Tsai
"""

import requests
from bs4 import BeautifulSoup

headers = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4122.7 Mobile Safari/537.36'}

def tire_news():
        url_watch = 'https://car.watch.impress.co.jp/category/tyre/'

        response_watch = requests.get(url_watch, headers=headers)
        response_watch.raise_for_status()
        soup_watch = BeautifulSoup(response_watch.text, 'lxml')
        data = soup_watch.find('section', class_='list')
        
        title = [title_item.text for title_item in data.find_all('p', class_='title')][:4]          
        link = [link_item.find('a').get('href') for link_item in data.find_all('p', class_='title')][:4]
        img_watch_item = 'https://car.watch.impress.co.jp/include/common/p01/images/logo/car.1200.png'
        img = [img_watch_item for i in range(3)]

        url_jdt = 'https://www.jdt-news.co.jp/category/news/'
    
        response_jdt = requests.get(url_jdt, headers=headers)
        response_jdt.raise_for_status()
        soup_jdt = BeautifulSoup(response_jdt.text, 'lxml')
        data_jdt = soup_jdt.find('div', class_='main-slider')

        title = title + [title_jdt_item.text for title_jdt_item in data_jdt.select('.slider-title')]
        link = link + [link_jdt_item.get('href') for link_jdt_item in data_jdt.select('.slider-title a')]
        img = img + [img_jdt_item.get('src').split('?')[0] for img_jdt_item in data_jdt.select('.slides img')]

        return title, link, img

    
print(tire_news())       
