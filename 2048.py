from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048/')
htmlElem = browser.find_element_by_tag_name('html')
gameOverElem = browser.find_element_by_css_selector('div .game-container .game-message p')

while True:
    if gameOverElem.text == 'Game over!':
        print("Game over! Stopping program...")
        exit()
    else:
        htmlElem.send_keys(Keys.UP)
        htmlElem.send_keys(Keys.RIGHT)
        htmlElem.send_keys(Keys.DOWN)
        htmlElem.send_keys(Keys.LEFT)