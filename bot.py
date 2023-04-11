import os
import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager as CM
from selenium.common.exceptions import NoSuchElementException

TIMEOUT = 15

options = webdriver.ChromeOptions()

bot = webdriver.Chrome(executable_path=CM().install(), options=options)

top_cities = [
    "Mont Saint Michel",
    "St Malo",
    "Bayeux",
    "Le Havre",
    "Rouen",
    "Paris",
    "Amiens",
    "Lille",
    "Strasbourg",
    "Chateau du Haut Koenigsbourg",
    "Colmar",
    "Eguisheim",
    "Besancon",
    "Dijon",
    "Annecy",
    "Grenoble",
    "Lyon",
    "Gorges du Verdon",
    "Bormes les Mimosas",
    "Cassis",
    "Marseille",
    "Aix en Provence",
    "Avignon",
    "Uzes",
    "Nimes",
    "Aigues Mortes",
    "Saintes Maries de la mer",
    "Collioure",
    "Carcassonne",
    "Ariege",
    "Toulouse",
    "Montauban",
    "Biarritz",
    "Bayonne",
    "La Rochelle"
]

hotels = []

for city in top_cities:
    bot.get('https://www.booking.com/')

    WebDriverWait(bot, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH, '//*[@id="onetrust-accept-btn-handler"]'))).click()

    time.sleep(10)

    location_element = bot.find_element(By.XPATH, '//*[@id="ss"]')
    location_element.send_keys(city)

    search_button = bot.find_element(
        By.XPATH, '//*[@id="frm"]/div[1]/div[4]/div[2]/button')

    time.sleep(0.4)

    search_button.click()

    def check_exists_by_xpath(element, xpath):
        try:
            element.find_element(By.XPATH, xpath)
        except NoSuchElementException:
            return False
        return True

    NEXT_XPATH = '//*[@id="search_results_table"]/div[2]/div/div/div/div[4]/div[2]/nav/div/div[3]/button[not(@disabled)]'
    while True:
        hotels_elements = bot.find_elements(
            By.XPATH, '//*[@id="search_results_table"]/div[2]/div/div/div/div[3]/div[@data-testid="property-card"]')
        for el in hotels_elements:
            url = ''
            name = ''
            score = 0
            if check_exists_by_xpath(el, 'div[1]/div[2]/div/div[1]/div[1]/div/div[1]/div/h3/a'):
                url = el.find_element(
                    By.XPATH, 'div[1]/div[2]/div/div[1]/div[1]/div/div[1]/div/h3/a').get_attribute('href')
            if check_exists_by_xpath(el, 'div[1]/div[2]/div/div[1]/div[1]/div/div[1]/div/h3/a/div[1]'):
                name = el.find_element(
                    By.XPATH, 'div[1]/div[2]/div/div[1]/div[1]/div/div[1]/div/h3/a/div[1]').get_attribute('innerText')
            if check_exists_by_xpath(el, 'div[1]/div[2]/div/div[1]/div[2]/div/a/span/div/div[1]'):
                score = float(el.find_element(
                    By.XPATH, 'div[1]/div[2]/div/div[1]/div[2]/div/a/span/div/div[1]').get_attribute('innerText').replace(',', '.'))
            hotel = {
                'name': name,
                'url': url,
                'score': score,
                'city': city,
                'description': ''
            }
            hotels.append(hotel)
        if check_exists_by_xpath(bot, NEXT_XPATH):
            bot.find_element(By.XPATH, NEXT_XPATH).click()
        else:
            break
        time.sleep(10)

    print(hotels)
    print(len(hotels))
