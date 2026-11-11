# requests 모듈 => 웹페이지를 요청하고 응답 데이터를 받을 수 있음
import requests as req
response = req.get('https://naver.com/')

print(response)

'''
# 대표적인 HTTP 상태 코드
- 200: 요청 성공
- 301, 302: 다른 url로 이동
- 403: 접근 거부
- 404: 요청한 페이지 없음
- 500: 서버 내부 오류
'''

html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
