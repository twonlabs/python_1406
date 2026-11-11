# 요소 찾는 방법 3가지
# - 태그 이름(TAG_NAME)
# - 
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://quotes.toscrape.com/')

# 태그 이름
# - html 태그(divm span, a등)요소로 찾기
div_elements = driver.find_elements(By.TAG_NAME, 'div')
print('TAG_NAME으로 찾은 div 태그 개수 :', len(div_elements))

# class로 요소 찾기(CLASS_NAME)
# - html에서 class='text'처럼 지정된 class이름으로 요소 찾기
# - Selenium에서 가장 자주 사용하는 방식 중 하나
# - class에 공백이 포함된 경우(ex: class="a b")는 CLASS_NAME으로 바로 찾기 어려움
first_quote_text = driver.find_element(By.CLASS_NAME, 'text')
print('\n CLASS_NAME으로 찾은 첫 번째 명언 :', first_quote_text.text)

# id로 요소 찾기(ID)
# - id는 보통 페이지에서 '유일'하게 존재
# - 정확하게 찾고 싶을 때 가장 안정
element = driver.find_element(By.ID, 'username')
print('\nID로 찾은 요소의 태그 이름 :', element.tag_name)

# find_element vs find_elements
# - find_element : 요소 1개만 찾음(없으면 에러 발생)
# - find_elements : 요소 여러 개를 찾고 리스트로 반환(없으면 빈 리스트)

one_quote_block = driver.find_element(By.CLASS_NAME, 'quote')
any_quote_block = driver.fine_element(By.CLASS_NAME, 'quote')

print('\nfine_element로 찾은 qoute 블록 1개 :', type(one_puote_block))
print('\nfine_elements로 찾은 qoute 블록 개수 :', len(many_puote_block))

# xPath

# xPath로 첫 번째 명언 검색
xpath_quote_text = driver.find_element(
    By, XPTATH,
    "//div[@class='quote']/span[@class='text']"
)

print('\nxPath로 찾은 첫번째 명언 :', xpath_quote_text.text)
driver.quit()
