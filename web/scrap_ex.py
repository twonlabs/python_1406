# requests 모듈 => 웹페이지를 요청하고 응답 데이터를 받을 수 있음
import requests as req
response = req.get('https://naver.com/')

print(response)
