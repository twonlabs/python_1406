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