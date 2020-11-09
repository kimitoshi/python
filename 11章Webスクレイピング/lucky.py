#! /usr/bin/env python3
# lucky.py - Google検索結果をいくつか開く

import requests, sys, webbrowser, bs4

print('Googling...')
res  = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

#TODO: 上位検索結果のリンクを取得
soup = bs4.BeautifulSoup(res.text, 'lxml')
link_elems = soup.select('.r a')

#TODO：各結果をブラウザのタブで開く
num_open = min(5, len(link_elems))
for i in range(num_open):
    webbrowser.open('http://google.com' + link_elems[i].get('href'))
    
