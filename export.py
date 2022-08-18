from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import xlsxwriter
from webdriver_manager.chrome import ChromeDriverManager


def findofferusa():
    options = Options()
    options.headless = False
    driver = webdriver.Chrome(ChromeDriverManager().install())
    #/! REPLACE this link with the filters you need to use on mon-vie-via.businessfrance.fr
    driver.get('https://mon-vie-via.businessfrance.fr/en/offres/recherche?query=')
    time.sleep(1)
    #Click /accept cookies
    driver.find_element(By.ID, 'onetrust-accept-btn-handler').click()
    time.sleep(2)
    #We cath the number of results
    offersnumbertext = driver.find_element(By.XPATH,'//*[@id="__layout"]/div/main/section[2]/div[2]/p').text
    #Transform the text to keep only the int numer
    offersnumber = [int(i) for i in offersnumbertext.split() if i.isdigit()]

    # print result
    print("Number of offers : ", offersnumber[0])

    #We use it at a limit to know when wa have to stop
    nbannoncesmax = offersnumber[0]+1
    nbannonces = 0
    #We check that the max offers can't be overdue
    while nbannonces<nbannoncesmax:
        try:
            element = driver.find_element(By.CSS_SELECTOR, ".see-more-btn")
            driver.execute_script("arguments[0].click();", element)
            nbannonces = nbannonces+6
            #ensure that the click is not interpreted as a double-click
            time.sleep(0.2)
            print(nbannonces)
        except NoSuchElementException:
            print('End')
            nbannonces = nbannoncesmax
    time.sleep(1)

    #To get all locations
    offercity = driver.find_elements(By.CSS_SELECTOR, 'p.location')
    #To get all details
    annonces = driver.find_elements(By.CSS_SELECTOR, '.figure-item')
    #creating the excel workbook
    workbook = xlsxwriter.Workbook('export-vie.xlsx')
    worksheet = workbook.add_worksheet()
    #Define headers
    worksheet.write('A1', 'City')
    worksheet.write('B1', 'Details')
    row = 1
    for z in offercity:
        worksheet.write(row, 0, z.text)
        row += 1
    row=1
    for i in annonces:
        worksheet.write(row, 1, i.text)
        row += 1
    driver.quit()
    workbook.close()
findofferusa()
