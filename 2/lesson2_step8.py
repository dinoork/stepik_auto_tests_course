from selenium import webdriver
from selenium.webdriver.common.by import By
import os 
import time

try: 
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("alex")
    
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("aaaa")
        
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("email@mail.ru")
    
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    
    attachFile = browser.find_element(By.ID, "file")    
    attachFile.send_keys(file_path)
    
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    
    time.sleep(1)
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()    