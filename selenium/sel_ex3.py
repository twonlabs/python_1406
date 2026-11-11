from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://quotes.toscrape.com/')

result = []

quote_blocks = driver.find_elements(By.CLASS_NAME, 'quote')

for block in quote_blocks:
    quote_text = block.find_element(By.CLASS_NAME, 'text').text
    author = block.find_element(By.CLASS_NAME, 'author').text

    tag_elements = block.find_elements(By.CLASS_NAME, 'tag')

    tags = [t.text for t in tag_elements]
    # tags = []
    # for t in tag_elements :
    #   tags.append(t.text)

    result.append({
        'page' : 1
        'quote' : quote_text,
        'author' : author,
        'tags' : tags
    })

    print(f'{author} : {quote_text} / tag: {tags}')

print('현재까지 수집된 개수 :', len(results))

driver.quit()
