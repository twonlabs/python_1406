import requests as req
from bs4 import BeautifulSoup

request_headers = {
}

response = req.get('https://news.naver.com', request_headers)
# print(response)

soup = BeautifulSoup(response.text, 'html.parer')

content = soup.select('.cnf_news_item')
print(content[0].text)

print('== class로 선택, 반복문으로 텍스트 출력')
for c in content:
    print(c.text)
    