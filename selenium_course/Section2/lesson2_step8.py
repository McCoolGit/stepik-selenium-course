from selenium import webdriver
import time
import os


current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)


    browser.find_element_by_name('firstname').send_keys('Maksim')
    browser.find_element_by_name('lastname').send_keys('Kulesh')
    browser.find_element_by_name('email').send_keys('me@me.by')
    browser.find_element_by_id('file').send_keys(file_path)
    browser.find_element_by_tag_name('button').click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()