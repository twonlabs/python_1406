import requests as req
from bs4 import BeautifulSoup

response = req.get('https://news.naver.com', request_headers)
print(response)
