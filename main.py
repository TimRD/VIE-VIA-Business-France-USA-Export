from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
import time
import requests
from selenium.common.exceptions import NoSuchElementException



def check_exists_by_xpath():
    try:
        driver.find_element_by_xpath('/html/body/div[1]/div/div/main/section[2]/section/a')
    except NoSuchElementException:
        return False
    return True
def findannonces():
    options = Options()
    options.headless = False
    # options.add_argument("--window-size=1920,1200")
    DRIVER_PATH = '/Users/timotheemarguier/Downloads/chromedriver'
    driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
    driver.get('https://mon-vie-via.businessfrance.fr/en/offres/recherche?query=&gerographicZones=2&countriesIds=62')
    time.sleep(1)
    driver.find_element_by_id('onetrust-accept-btn-handler').click()
    time.sleep(4)
    nbannoncesmax=312
    nbannonces = 0
    while nbannonces<nbannoncesmax:
        try:
            element = driver.find_element_by_css_selector(".see-more-btn")
            driver.execute_script("arguments[0].click();", element)
            nbannonces = nbannonces+6
            print(nbannonces)
        except NoSuchElementException:
            findepage = endconfirmed
            print('Fin de page')



    time.sleep(1)

    #if check_exists_by_xpath():
        #driver.find_element_by_xpath('/html/body/div[1]/div/div/main/section[2]/section/a').click()
        #print('le bouton existe')

    annonces = driver.find_elements_by_class_name('figure-item')
    annoncetitle = driver.find_elements_by_css_selector('p.location')
    #annonces = driver.find_elements_by_xpath('//*[@id="__layout"]/div/main/section[2]/section/article/div/div/div/div[1]/figure/figcaption/div[1]/p')


    for i in annonces:
        print (i.text)
        #print (i.driver.find_elements_by_css_selector('p.location').text)
        print('--------\n')

    for z in annoncetitle:
        print ('Title : ', z.text)
        #print (i.driver.find_elements_by_css_selector('p.location').text)
        print('--------\n')


    driver.quit()

findannonces()
