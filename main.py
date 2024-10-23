import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

browser = webdriver.Chrome()
parsed_data = []
url = "https://www.divan.ru/kazan/category/svet"

#Функция для добавления данных в parsed_data
def append_parsed_data(url):
    browser.get(url)
    time.sleep(3)

    lights = browser.find_elements(By.CSS_SELECTOR,"div._Ud0k")
    for light in lights:
        try:
            name = light.find_element(By.CSS_SELECTOR,"div.lsooF").find_element(By.TAG_NAME,'span').text
            price = light.find_element(By.CSS_SELECTOR,"div.q5Uds").find_element(By.TAG_NAME,"span").text
            price = float(price.strip())
            link = light.find_element(By.TAG_NAME,'a').get_attribute("href")
            link = url + link
        except:
            print("Произошла ошибка при парсинге")
            continue

        parsed_data.append([name,price,link])

#Функция для записи в файл
def write_data_to_csv(parsed_data,filename):
    with open(filename,'w',encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Название', 'Цена', 'Ссылка'])
        writer.writerows(parsed_data)

#Парсим данные с 4-х страниц сайта
append_parsed_data(url)
append_parsed_data(url+'/page-2')
append_parsed_data(url+'/page-3')
append_parsed_data(url+'/page-4')

#Записываем данные в файл
write_data_to_csv(parsed_data,'lights.csv')
