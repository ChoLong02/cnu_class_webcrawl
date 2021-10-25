import pprint
import requests
from bs4 import BeautifulSoup

url = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code=191559&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page=1'

result = requests.get(url)
doc = BeautifulSoup(result.text, 'html.parser')

review_list = doc.select('div.score_result > ul > li')
for i, one in enumerate(review_list):
    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')

    # review 정보 수집
    review_select = one.select('div.score_reple > p > span')
    j = 0
    if len(review_select) == 2:
        j = 1
    review = review_select[j].get_text().strip()

    # review 정보 수집
    score = one.select('div.star_score > em')[0].get_text()

    # 작성자(닉네임) 정보 수집
    original_writer = one.select('div.score_reple dt > em')[0].get_text().strip()
    idx_end = original_writer.find('(')
    writer = original_writer[:idx_end]

    # Date 정보 수집
    original_date = one.select('div.score_reple dt > em')[1].get_text()
    print('# Review: {}'.format(review))
    print('# Score: {}'.format(score))
    print('# Writer: {}'.format(writer))
    print('# Date: {}'.format(original_date))

