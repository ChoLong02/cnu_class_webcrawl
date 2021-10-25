import pprint
import requests
from bs4 import BeautifulSoup

i = 0
for page_number in range(1, 3):
    url = 'https://news.daum.net/breakingnews/digital?page={}'.format(page_number)
    result = requests.get(url)

    soup = BeautifulSoup(result.text, 'html.parser')
    title_list = soup.select('ul.list_news2 a.link_txt')
    # pprint.pprint(link_list)

    for title in title_list:
        new_url = title['href']
        result = requests.get(new_url)
        doc = BeautifulSoup(result.text, 'html.parser')

        title = doc.select('h3.tit_view')[0].get_text()
        contents = doc.select('section p')

        i += 1 # 뉴스 Count
        print('■■ {}번 ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■'.format(i))
        print('# URL: {}'.format(new_url))
        print('# 뉴스 제목: {}'.format(title))

        contents.pop(-1) # 기자 정보 삭제
        content = ''
        for info in contents:
            content += info.get_text()
        print('# 뉴스 본문: {}'.format(content))