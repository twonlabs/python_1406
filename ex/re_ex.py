# 정규 표현식: 문자열에서 특정한 규칙이나 패턴을 가진 데이터를 추출, 검색, 치환하기 위한 표현 방식
# 문자열 검색 / 데이터 추출 / 문자열 치환 / 입력값 검사 / 데이터 정제
import re

print('=== 정규 표현식 ===')

text = '내 혈압은 120mmHg 입니다'
print('120' in text)

# 정규표현식
pattern = r'\d+'
result = re.findall(pattern, text)
print(result)

# 이메일 형식 간단히 찾기
'''
data = '이메일은 twonlabs@naver.com 입니다'

email_pattern = r'\w+@\w+\.\w+'
emails = re.findall(email_pattern, data)
print(emails)
'''
print('=== 정규 표현식 : re모듈 주요 함수 ===')
# re.findall()
# re.

print('=== 정규 표현식 : 문자열 치환(replace 대신 re.sub) ===')

text2 = '가격은 12000원 입니다'

# 숫자 제거

print('=== 정규식 vs 일반 문자열 비교 ===')

text = ' 몸무게