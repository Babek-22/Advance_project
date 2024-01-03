from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import time
import requests

chrome_driver_path = "/home/safex/chromedriver"

USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"


def open_moto_site():
    print("======================  başladıq =========================")
    
    url = 'https://newsdata.io/api/1/news?apikey=pub_33826c685cc44202364234109f368dbc7caab&q=crypto'
    response = requests.get(url)
    data = response.json() 
    all_data = data.get('results')

    # kommente aldim yazir amma istenilen kimi deyil
    # for data in all_data:
    #     with open(f'cavid_images/{data.get("title")}.png', "wb") as f:
    #         if data.get('image_url') != None:
    #             f.write(requests.get(data.get('image_url')).content)
    

    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    # options.add_argument('--headless')
    options.add_argument("--disable-dev-shm-usage")
    # ser = Service(executable_path="/home/taleh/Downloads/chromedriver/chromedriver")
    service = Service(executable_path="/home/advance_project/selenium/chromedriver")
    driver = webdriver.Chrome(options=options, service=service)

    driver.maximize_window()
    driver.get(
        "http://127.0.0.1:8000/en/admin/login/?next=/en/admin/"
    )
    time.sleep(2)
    username_input_xpath = '//*[@id="id_username"]'
    password_input_xpath = '//*[@id="id_password"]'
    login_button_xpath = '//*[@id="login-form"]/div[3]/input'

    username = 'admin'
    password = 'admin'

    username_input = driver.find_element(By.XPATH, username_input_xpath)
    username_input.send_keys(username)

    password_input = driver.find_element(By.XPATH, password_input_xpath)
    password_input.send_keys(password)

    login_button = driver.find_element(By.XPATH, login_button_xpath)
    login_button.click()
    time.sleep(2)

    news_button_xpath = '//*[@id="content-main"]/div[2]/table/tbody/tr[4]/th/a'
    news_button = driver.find_element(By.XPATH, news_button_xpath)
    news_button.click()
    time.sleep(2)

    for data in all_data:
        try:
            add_news_button_xpath = '//*[@id="content-main"]/ul/li/a'
            add_news_button = driver.find_element(By.XPATH, add_news_button_xpath)
            add_news_button.click()
            time.sleep(2)

            title_input_xpath = '//*[@id="id_title_en"]'
            title_input = driver.find_element(By.XPATH, title_input_xpath)
            title_input.send_keys(data.get('title'))

            description_input_xpath = '//*[@id="id_description_en"]'
            description_input = driver.find_element(By.XPATH, description_input_xpath)
            description_input.send_keys(data.get('description'))

            image_input_xpath = '//*[@id="id_image"]'
            image_input = driver.find_element(By.XPATH, image_input_xpath)
            image_path = data.get('image_url')
            if image_path == None:
                image_path = "/home/talehbe/BE Projects/motoscrapy/trend_scraper/1.png"
            else:
                image_path = requests.get(image_path).content
            image_input.send_keys(image_path)

            save_button_xpath = '//*[@id="news_form"]/div/div/input[1]'
            save_button = driver.find_element(By.XPATH, save_button_xpath)
            save_button.click()
            time.sleep(3)
        except:
            continue

    time.sleep(2000)





open_moto_site()