from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://quotes.toscrape.com/')

MAX_PAGES = 3

current_page = 1

results = []

while current_page <= MAX_PAGES:
    print(f"=== {current_page}페이지 수집 중 ===")

    quote_block = driver.find_elements(By.CLASS_NAME, 'quote')

        for block in quote_block:
        quote_text = block.find_element(By.CLASS_NAME, 'text').text
        author = block.find_element(By.CLASS_NAME, 'author').text

        tag_elements = block.find_elements(By.CLASS_NAME, 'tag')

        tags = [t.text for t in tag_elements]

        result.append({
            'page' : 1
            'quote' : quote_text,
            'author' : author,
            'tags' : tags
        })

    next_buttons = driver.find_elements(By.CSS_SELECTOR, 'li.next a')

    if not next_buttons:
        print('다음 페이지가 없어 종료합니다.')
        break


    next_buttons[0].click()

    current_page += 1

    print('최종 수집 개수 :', len(results))

driver.quit()

