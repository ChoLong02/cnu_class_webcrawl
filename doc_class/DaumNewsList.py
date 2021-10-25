import pprint
import requests
from bs4 import BeautifulSoup

url = 'https://news.daum.net/breakingnews/digital'
result = requests.get(url)

soup = BeautifulSoup(result.text, 'html.parser')
title_list = soup.select('ul.list_news2 a.link_txt')
# pprint.pprint(link_list)

for i, title in enumerate(title_list):
    new_url = title['href']
    result = requests.get(new_url)
    doc = BeautifulSoup(result.text, 'html.parser')

    title = doc.select('h3.tit_view')[0].get_text()
    contents = doc.select('section p')

    print('■■ {}번 ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■'.format(i+1))
    print('# URL: {}'.format(new_url))
    print('# 뉴스 제목: {}'.format(title))
    contents.pop(-1) # 기자 정보 삭제
    content = ''
    for info in contents:
        content += info.get_text()
    print('# 뉴스 본문: {}'.format(content))

