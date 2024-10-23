import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

browser = webdriver.Chrome()
parsed_data = []
url = "https://www.divan.ru/kazan/category/svet"

#Функция для добавления данных в parsed_data
def append_parsed_data(url):
    print("Start parsing")
    browser.get(url)
    # time.sleep(5)

    lights = browser.find_elements(By.CSS_SELECTOR,"div._Ud0k")
    for light in lights:
        try:
            name = light.find_element(By.CSS_SELECTOR,"div.lsooF").find_element(By.TAG_NAME,'span').text
            price = light.find_element(By.CSS_SELECTOR,"div.q5Uds").find_element(By.TAG_NAME,"span").text
            price = price.strip('руб.') #убираем символы руб
            price = "".join(price.split()) #убираем пробел между разрядами: 20 100 -> 20100
            price = float(price) #переводим в число
            link = light.find_element(By.TAG_NAME,'a').get_attribute("href")
            # print([name, price, link])
        except:
            print("Произошла ошибка при парсинге")
            continue
        parsed_data.append([name,price,link])
    print("Finish parsing of one page")

#Функция для записи в файл
def write_data_to_csv(parsed_data,filename):
    with open(filename,'w',encoding='utf-16') as file:
        writer = csv.writer(file)
        writer.writerow(['Название', 'Цена', 'Ссылка'])
        writer.writerows(parsed_data)
    print("File was written")

#Парсим данные с 4-х страниц сайта
append_parsed_data(url)
append_parsed_data(url+'/page-2')
append_parsed_data(url+'/page-3')
append_parsed_data(url+'/page-4')
browser.quit()

#Записываем данные в файл
write_data_to_csv(parsed_data,'lights.csv')
